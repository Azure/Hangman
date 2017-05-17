# Train a Neural Network to Play Hangman with CNTK

by Mary Wahl, Fidan Boylu Uz, Shaheen Gauher, Katherine Zhao

In the classic children's game of Hangman, a player's objective is to identify a hidden word of which only the number of letters is originally revealed. In each round, the player guesses a letter of the alphabet: if it's present in the word, all instances are revealed; otherwise one of the hangman's body parts is drawn in on a gibbet. The game ends in a win if the word is entirely revealed by correct guesses, and ends in loss if the hangman's body is completely revealed instead. To assist the player, a visible record of all guessed letters is typically maintained.

The goal of this project was to train a neural network to play Hangman by appropriately guessing letters in a partially or fully obscured word. The network receives as input a representation of the word (total number of characters, the identity of any revealed letters) as well as a list of which letters have been guessed so far. It returns a guess for the letter that should be picked next. This notebook shows our method for training the network with Microsoft's [Cognitive Toolkit (CNTK)](https://github.com/Microsoft/CNTK) and validating its performance on a withheld test set.

## Prerequisites

You will need:
- A computer with a GPU (such as an Azure NC6 GPU DSVM)
- [CNTK 2.0 release candidate 2](https://github.com/Microsoft/CNTK/releases) (or later) installed in an Anaconda Python 3.5 environment able to run Jupyter Notebooks
- The [tarballed version](http://wordnetcode.princeton.edu/3.0/WordNet-3.0.tar.gz) of Princeton University's [WordNet](http://wordnet.princeton.edu) database, decompressed e.g. uzing [7zip](http://www.7-zip.org/download.html)
- The Jupyter notebook contained in this repository
- (Optionally) the trained model contained in this repository, if you prefer not to train your own

Note that the first two requirements can be satisfied by deploying a "Deep Learning toolkit for the DSVM" resource on Azure.

## Get Started

Load the Jupyter notebook from this repository in your CNTK Python 3.5 environment, and you're all set!

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
