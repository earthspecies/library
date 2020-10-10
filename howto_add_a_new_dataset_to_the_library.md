

| Work In Progress |
| --- |
| This document is under construction. |

# How To Add a New Dataset to the ESP Library

This document outlines steps to take to add a new dataset to the library. Datasets come in various shapes and sizes. These steps describe the most likely approach when adding a new dataset. However, some changes to the procedure may be necessary to address the intricacies of specific datasets. 

1. Find a suitable dataset.

One of the aims for the ESP library is to increase access to [bioacoustic](https://en.wikipedia.org/wiki/Bioacoustics) datasets (predominantly audio though multimodality is encouraged) for machine learning. Many of the datasets are public domain, shared by researchers who study animals. For example, in this [2014 paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0112562#s5) about Giant Otter vocalizations, authors Christina A. S. Mumm and Mirjam Knörnschildm shared their audio recordings and annotations (labels) in the supplementary material. These labels may describe the vocalization type, individual speaker, behavior, or ecosystem. The ESP Library also contains contributions from researchers directly collaborating with the Earth Species Project. For a list of datasets in the latter category, or to share a dataset, please consult the document here. [link to be added].

What makes for a good data set? Some factors to consider: Quanitity of the data, quality of recordings (is there background noise? multipe overlapping speakers? length of each vocalization), existance and quality of annotations, the licensce under which the data is shared.

For a list of potential data sets to add to the ESP Library please consult the document here [link to be added].

2. Download the dataset and perform exloratory analysis

How is the data organized? Do the labels follow a consistent format, or are there any issues? To note, often data is entered manually by human annotators, which can be a painstaking and meticulous process. There could be misspellings or other inconsistencies that need to be corrected.

When you work on the preprocessed data, is it easy to load everything up?

For a set of guidelines for what an ML ready dataset might look like, please consult the document here [link to be added].
The results of this phase should be:

  - preprocessed dataset
  - a notebook portraying and explaining the rationale behind the steps applied to the data
  
3. Dataset uploaded to Internet Archive

  - Package the dataset using this [ need to figure this out ] command.
  - verify that untar_data from fastai works with the archive (test it locally)
  - upload to Internet Archive (is there anything one should pay attention to here? I am not sure) 
    - From personal experience trying to get large datasets onto Archive, make sure you first upload a small selection of the data and verify that the data is accessible using `untar_data()` -- if it isn't, make sure you have zipped the file and contents correctly, and make sure you run a zip file checker (the command `!zip -T` on my Jupyter notebook did the trick). The zip file checker will tell you if there are any corrupted files that need to be either deleted or zipped again. 
    - Also make sure that the Archive entry is compliant with the licensing of the dataset, appropriately cites the authors, and is descriptive. 

  - Package the dataset using this [ need to figure this out ] command.
  - verify that `untar_data` from fastai works with the archive (test it locally)
  - upload to Internet Archive (is there anything one should pay attention to here? I am not sure)

4. Add the dataset to fastai

Here are the steps to open the PR, add the hash to verify data integrity (I can't reproduce this from the top of my head - will work on this)

5. Open a PR for the ESP library

Clone the ESP library. Create a directory with the name of the new dataset. Place the notebook showing the data preprocessing in it. Create a notebook showing how to load the data and construct a simple model. Add a brief description of the dataset to the README.md and link it to any models that you are making available from the table in the README. Commit changes and open a PR to the ESP library.

6. Next steps
  - Add a ‘future work/potential next steps’ section to your README so that future collaborators can extend your work! If your models have room for growth, spell out the avenues down which people can explore and progress the research! If you have an abundance of ideas, be sure to jot them down so that you may inspire other people to pick up where you left off!
  
Congratulations! Now that you have submitted the PR, you can continue adding models and sharing your findings with the research community! Thank you for all your fantastic work!
