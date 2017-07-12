# Play Hangman with CNTK

by Mary Wahl, Shaheen Gauher, Fidan Boylu Uz, Katherine Zhao

In the classic children's game of Hangman, a player's objective is to identify a hidden word of which only the number of letters is originally revealed. In each round, the player guesses a letter of the alphabet: if it's present in the word, all instances are revealed; otherwise one of the hangman's body parts is drawn in on a gibbet. The game ends in a win if the word is entirely revealed by correct guesses, and ends in loss if the hangman's body is completely revealed instead. To assist the player, a visible record of all guessed letters is typically maintained.

For this project, we trained a neural network to play Hangman by appropriately guessing letters in a partially or fully obscured word. The network receives as input a representation of the word (total number of characters, the identity of any revealed letters) as well as a list of which letters have been guessed so far. It returns a guess for the letter that should be picked next. This repo shows our method for training the network with Microsoft's [Cognitive Toolkit (CNTK)](https://github.com/Microsoft/CNTK) and validating its performance on a withheld test set, as well as operationalizing the model for gameplay on an Azure Web App.

## Outline

- [Training](#train)
   - [Prerequisites](#trainprereq)
   - [Sample code (contained in Jupyter Notebook)](#traincode)
- [Operationalization](#op)
   - [Prerequisites](#opprereq)
   - [Deploying an Azure Web App](#deploy)
   - [Web App Setup](#setup)
   - [Playing Hangman](#gameplay)

Note that it is not necessary to complete the "Training" section before completing the "Operationalization" section, as a sample trained model is provided.

<a name="train"></a>
## Training

<a name="trainprereq"></a>
### Prerequisites

You will need:
- A computer with a GPU (such as an Azure NC6 GPU DSVM)
- [CNTK 2.0 release candidate 2](https://github.com/Microsoft/CNTK/releases) (or later) installed in an Anaconda Python 3.5 environment able to run Jupyter Notebooks
- The [tarballed version](http://wordnetcode.princeton.edu/3.0/WordNet-3.0.tar.gz) of Princeton University's [WordNet](http://wordnet.princeton.edu) database, decompressed e.g. uzing [7zip](http://www.7-zip.org/download.html)
- The Jupyter notebook contained in the root directory of this repository

Note that the first two requirements can be satisfied by deploying a "Deep Learning toolkit for the DSVM" resource on Azure.

<a name="traincode"></a>
### Sample code (contained in Jupyter Notebook)

Load the Jupyter notebook -- `Train a Neural Network to Play Hangman.ipynb` -- from this repository in your CNTK Python 3.5 environment, and follow the instructions inside to complete the training and validation steps.

<a name="op"></a>
## Operationalization

<a name="opprereq"></a>
### Prerequisites
- An [Azure subscription](https://azure.microsoft.com/en-us/free/) for deploying an Azure Web App resource
- A cloned or downloaded local copy of this repository
   - We will refer to the location of this repository on your local computer as `<repo-filepath>`.
- The command line version of [Git](https://git-scm.com/downloads) installed locally
   - Git and shell commands will be written for a Windows operating system. However, you may be able to easily adapt these commands for Mac OS/Linux/UNIX.

<a name="deploy"></a>
### Deploying an Azure Web App

We will create an Azure Web App to serve a website containing our neural network. To deploy a web app:
1. Log into [Azure Portal](https://portal.azure.com).
1. Click the "+ New" button at upper-left.
1. In the search bar, type in "Web App" and press Enter.
1. In the search results, choose the "Web App" option published by Microsoft.
1. After reading the description in the pane that appears, scroll down and click the "Create" button.
1. In the "Web App Create" pane that appears:
   1. Choose a unique name for your web app.
   1. Select the appropriate Azure subscription.
   1. Choose a resource group for your web app. (We recommend creating a new resource group, so that you can easily delete it and the associated app service plan at the end of this tutorial.)
   1. Click on App Service plan. You may choose an existing plan, but we recommend that you create a new one as follows:
      1. Click the "+ Create New" button.
      1. Choose an appropriate name and location for the service plan, then click OK.
   1. Click "Create".

Deployment may take a few minutes to complete. To monitor deployment, navigate to your resource group by typing its name in the search bar at the top of the Azure Portal website. Refresh until the "App Service" resource (your web app) appears in the resource group contents.


<a name="setup"></a>
### Web App Setup

Once your web app's deployment is complete, navigate to its overview pane (e.g. by clicking on the "App Service" resource in your resource group). The steps below will install necessary Python packages on the web app and upload the model files and website code from your local computer.

#### Install the Python 3.5.2 x64 Extension

The web app comes with Python 2.7 and 3.4 (x86) available by default. We install Python 3.5 x64 to meet the requirements of CNTK.

1. In the search bar at the upper left of your web app's overview pane, type in "Extensions" and click on the search result.
1. Click the "+ Add" button.
1. Scroll through the list of extensions to find and click on "Python 3.5.3 x64".
1. Review and accept the legal terms by clicking "OK".
1. Click "OK" to initiate the installation of the extension.
1. After a moment, refresh the page to confirm that the extension has installed successfully. (You may receive an Azure notification that the installation timed out even if the install completes successfully.)

#### Configure Local Git Deployment

You will use local git deployment to deploy the code from a local folder to your web app. The first step in this process is to configure the settings on your web app.

1. In the search bar at the upper left of your web app's overview pane, type in "Deployment options" and click on the search result.
1. Click on "Choose Source" and select "Local Git Repository".
1. If you have not used local Git deployments on Azure previously, you will see a section that says "Setup connection" where you must choose a username and password for connecting to Azure via `git`.
    1. Note that these login credentials are distinct from your GitHub account, if you have one.
    1. Choose a username and password you will remember: the same login will be automatically associated with local Git deployments on Azure that you create in the future. (Note that you will have the option to change this login in the future.)
1. Click "OK". (There is no need to configure the Performance Test.)
1. Find the Git URL:
   1. In the search bar at the upper left of your web app's overview pane, type in "Properties" and click on the search result.
   1. Copy the value in the "GIT URL" field on the Properties pane and store it locally; you will use this value shortly.

Once the web app is configured, complete the steps below to configure git locally:
1. (Optional) If you trained your own NN using the Jupyter notebook in this repo and would like to use it on the website, copy your `hangman_model.dnn` file to the folder `<repo-filepath>\webapp\models` to overwrite our example model.
1. Open a command prompt (e.g. by clicking the Windows icon and typing "cmd").
1. Navigate to the `webapp` folder in your local copy of the git repository:
   ```cd <repo-filepath>\webapp```
1. Execute the commands below to create a local git repo and push a commit.
   ```
   git init
   git remote add azure <git-url-stored-earlier>
   git add .
   git commit -m"Install necessary Python packages"
   git push azure master
   ```
   
You will be asked to supply the git credentials you chose earlier. The push step will take a few minutes to run. When it completes, your website is ready for use!

<a name="gameplay"></a>
### Playing Hangman

To use your web app, navigate to `http://<your web app's resource name>.azurewebsites.net`. After a few seconds of initial loading, you should see a website asking you to choose a secret word for the neural network to guess. You're responsible for remembering the secret word, but you will need to tell the neural network how long the word is.

After specifying the length and clicking Submit, the neural network's first letter guess will be displayed. It's up to you to tell the neural network whether (and if so, where) the letter appears in the word. After providing this feedback, click Submit to begin the next round.

After each round, the neural network's lives remaining is updated, and the neural network makes another guess. Eventually the neural network either guesses the entire word or runs out of lives.

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
