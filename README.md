# Play Hangman with CNTK

by Mary Wahl, Fidan Boylu Uz, Katherine Zhao

In the classic children's game of Hangman, a player's objective is to identify a hidden word of which only the number of letters is originally revealed. In each round, the player guesses a letter of the alphabet: if it's present in the word, all instances are revealed; otherwise one of the hangman's body parts is drawn in on a gibbet. The game ends in a win if the word is entirely revealed by correct guesses, and ends in loss if the hangman's body is completely revealed instead. To assist the player, a visible record of all guessed letters is typically maintained.

For this project, we trained a neural network to play Hangman by appropriately guessing letters in a partially or fully obscured word. The network receives as input a representation of the word (total number of characters, the identity of any revealed letters) as well as a list of which letters have been guessed so far. It returns a guess for the letter that should be picked next. This repo shows our method for training the network with Microsoft's [Cognitive Toolkit (CNTK)](https://github.com/Microsoft/CNTK) and validating its performance on a withheld test set, as well as operationalizing the model for gameplay on an Azure Web App.

## Outline

- [Training](#train)
   - [Prerequisites](#trainprereq)
   - [Sample code (contained in Jupyter Notebook)](#traincode)
- [Operationalization](#op)
   - [Prerequisites](#opprereq)
   - [Deploying an Azure Web App](#deploy)

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

## Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
