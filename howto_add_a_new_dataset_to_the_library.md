

| Work In Progress |
| --- |
| This document is under construction. |

# How To Add a New Dataset to the ESP Library

This document outlines steps to take to add a new dataset to the library. Datasets come in various shapes and sizes. The steps below describe the steps you most likely will want to take when adding a new dataset. Some changes to the procedure might need to be made to address the intricacies of the specific dataset you are working on.

1. Find a suitable dataset.

The ESP library aims to share animal datasets (predominantly audio though mutlimodality is encouraged) that can be useful in bioacoustic research and conservationist efforts. The primary sources of our datasets are research datasets that have been put in the public domain (they can be found on the Internet) or direct contributions from collaborating researchers. For a list of datasets in the latter category please consult the document here [link to be added].

2. Download the dataset and perform exloratory analysis

How is the data organized? Do the lables follow a consistent format or are there any issues? Often data is entered manually by human annotators - maybe there are misspellings or other inconsistencies that need to be corrected.

When you work on the preprocessed data, is it easy to load everything up?

For a set of guidelines for what an ML ready dataset might look like, please consult the document here [link to be added].

The results of this phase should be:
  - preprocessed dataset
  - a notebook portraying and explaining the rational behind the steps that were applied to the data
  
3. Upload the dataset to Internet Archive

  - Package the dataset using this [ need to figure this out ] command.
  - verify that `untar_data` from fastai works with the archive (test it locally)
  - upload to Internet Archive (is there anything one should pay attention to here? I am not sure)

4. Add the dataset to fastai

Here are the steps to open the PR, add the hash to verify data integrity (I can't reproduce this from the top of my head - will work on this)

5. Open a PR for the ESP library

Clone the ESP library. Create a directory with the name of the new dataset. Place the notebook showing the data preprocessing in it. Create a notebook showing how to load the data and construct a simple model. Add a brief description of the dataset to the README.md and link to any models that you are making available from the table in the README. Commit changes and open a PR to the ESP library.

6. Next steps

Congratulations! Now that you have the submitted the PR, you can continue on adding models and sharing your findings with the research community! Thank you for all your amazing work!

-----------------

## Please note

We welcome your contributions. Throught the entire process, please stay in communication with us - we will be super excited to learn about the work that you are doing and are eager to help. If you need anything, please give us a shout. You can find us here [link or links to be added]

  
