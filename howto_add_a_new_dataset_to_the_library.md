

| Work In Progress |
| --- |
| This document is under construction. |

# **How To Add a New Dataset to the Earth Species Library**

This document outlines steps to take to add a new dataset to the Library. Datasets come in various shapes and sizes. These steps describe the most likely approach when adding a new dataset. However, some changes to the procedure may be necessary to address the intricacies of specific datasets. 


## Find a suitable dataset.

One of the aims for the ESP library is to increase access to [bioacoustic](https://en.wikipedia.org/wiki/Bioacoustics) datasets (predominantly audio though multimodality is encouraged) for machine learning. Many of the datasets are public domain, shared by researchers who study animals.

For example, in this [paper](https://journals.plos.org/plosone/article?id=10.1371/journal.pone.0112562#s5) about Giant Otter vocalizations (Mumm and Knörnschild, 2014), the authors shared audio recordings and annotations in the supplementary material. 

Annotations, which we refer to as labels, may describe vocalization type, individual speaker, behavior, or ecosystem. The Library also contains contributions from researchers directly collaborating with the Earth Species Project. 


## Download the dataset and perform exploratory analysis

Often data is entered manually by human annotators, which can be a painstaking and meticulous process. There could be misspellings or other inconsistencies that need to be corrected. 

*   How is the data organized? 
*   Do the labels follow a consistent format, or are there any issues? 
*   When you work on the preprocessed data, is it easy to load everything up?

For a set of guidelines for what an ML ready dataset might look like, please consult the document here [link to be added].

The results of this phase should be:

*   preprocessed dataset
*   a notebook portraying and explaining the rationale behind the steps applied to the data


## Dataset uploaded to Internet Archive

*   Package the dataset using this `zip -qr <name_of_archive>.zip annotations.csv <directory_to_include>` command.
*   upload to Internet Archive adding to the Earth Species Collection (include any relevant information as metadata, such as data license, etc)

## Create notebooks demonstrating how to download and work with the dataset

## Next steps

*   Add a ‘future work/potential next steps’ section to your README so that future collaborators can extend your work! If your models have room for growth, spell out the avenues down which people can explore and progress the research! If you have an abundance of ideas, be sure to jot them down so that you may inspire other people to pick up where you left off!

Congratulations! Now that you have submitted the PR, you can continue adding models and sharing your findings with the research community! Thank you for all your fantastic work!
