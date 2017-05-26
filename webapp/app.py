import os
from flask import Flask, request, render_template
os.environ['PATH'] = r'D:\home\site\wwwroot\cntk;' + os.environ['PATH']
import cntk
import numpy as np

app = Flask(__name__)
wsgi_app = app.wsgi_app
model = cntk.load_model('D:\\home\\site\\wwwroot\\models\\hangman_model.dnn')

''' Helper functions for neural network evaluation '''
def encode_word(current_view):
    word = [26 if i == '_' else ord(i) - 65 for i in current_view]
    obscured_word = np.zeros((len(word), 27), dtype=np.float32)
    for i, j in enumerate(word):
        obscured_word[i, j] = 1
    return(obscured_word)

def encode_previous_guesses(letters_guessed):
    previous_guesses = np.zeros(26, dtype=np.float32)
    for i in letters_guessed:
        previous_guesses[ord(i) - 65] = 1
    return(previous_guesses)

def get_next_guess(current_view, letters_guessed):
    global model
    guess = model.eval({model.arguments[0]: encode_word(current_view),
                        model.arguments[1]: encode_previous_guesses(letters_guessed)})
    guess_letter = chr(65 + np.argmax(np.squeeze(guess)))
    return(guess_letter)


@app.route('/', methods=['GET'])
def sign_form():
    return render_template('index.html')

@app.route('/start', methods=['POST'])
def start():
	global num_chars, lives_remaining, current_view, letters_guessed

	# Initialize values for the new game
	num_chars = int(request.form['num_chars'])
	lives_remaining = 10
	current_view = ['_'] * num_chars
	letters_guessed = set([])
	
	# Get the model's guess (need to add CNTK code; hardcode for now)
	guess = get_next_guess(current_view, letters_guessed)
	letters_guessed.add(guess)

	# Display the page where the user can provide feedback.
	return render_template('start.html',
						   guess=guess,
						   lives_remaining=lives_remaining,
						   current_view=current_view,
						   letters_guessed=letters_guessed)

@app.route('/feedback', methods=['POST'])
def feedback():
	global num_chars, lives_remaining, current_view, letters_guessed

	# Parse feedback to get lives_remaining and current_view
	if len(request.form.getlist('present')) > 0:
		guess_result = 'correctly'
	else:
		guess_result = 'incorrectly'
		lives_remaining -= 1

	for i in request.form.getlist('present'):
		idx = int(i.split('letter')[1])
		current_view[idx] = str(request.form['last_guess']).upper()

	if lives_remaining == 0:
		return render_template('gameover.html',
							   guess=guess,
							   lives_remaining=lives_remaining,
							   current_view=current_view,
							   letters_guessed=letters_guessed)
	elif '_' not in current_view:
		return render_template('win.html',
							   guess=guess,
							   lives_remaining=lives_remaining,
							   current_view=current_view,
							   letters_guessed=letters_guessed)
	else:
		guess = get_next_guess(current_view, letters_guessed)
		letters_guessed.add(guess)
		return render_template('feedback.html',
							   guess_result=guess_result,
							   lives_remaining=lives_remaining,
							   guess=guess,
							   current_view=current_view,
							   letters_guessed=letters_guessed)

if __name__ == '__main__':
	HOST = os.environ.get('SERVER_HOST', 'localhost')
	try:
		PORT = int(os.environ.get('SERVER_PORT', '5555'))
	except ValueError:
		PORT = 5555
	app.run(HOST, PORT)