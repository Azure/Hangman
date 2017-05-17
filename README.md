
# Input data

We trained and validated our model using words from Princeton University's [WordNet](http://wordnet.princeton.edu) database. Specifically, we downloaded the [tarballed version of WordNet 3.0](http://wordnetcode.princeton.edu/3.0/WordNet-3.0.tar.gz) and used all words (consisting only of alphabetic characters) from the following files from the tarball's `dict` subfolder:
- `data.adj`
- `data.adv`
- `data.verb`
- `data.noun`

We augmented this word set with a few company phrases like "Microsoft" and "CNTK". We randomly partitioned these words 80:20 to create training and validation sets of 44,503 and 11,226 words, respectively.

# Contributing

This project has adopted the [Microsoft Open Source Code of Conduct](https://opensource.microsoft.com/codeofconduct/). For more information see the [Code of Conduct FAQ](https://opensource.microsoft.com/codeofconduct/faq/) or contact [opencode@microsoft.com](mailto:opencode@microsoft.com) with any additional questions or comments.
