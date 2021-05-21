# An Introduction

![includes-data](https://img.shields.io/badge/includes%20data-yes-green)

Fieldwork is an essential component of the work to decode animal language and communication.  Collectively, biologists have lifetimes of invaluable observations from the field, but most of these recordings – scattered across hard drives, old tapes, and hidden servers – may be difficult to access. Further, bioacoustic recordings often include a medley of biophony, geophony, and anthropophony which make it hard to get to a starting point where you can begin experimentation. And, commonly, datasets are hand-labelled which may lead to human error. The Earth Species Library is an open and free repository that pulls together all of these incredible observations, documents them, and makes them ready for machine learning.

# Acknowledgements

A major roadblock in translating animal communication is having enough of the right kinds of data with the right kinds of annotations. No matter how advanced the algorithm, the quality of what they learn derives from the quality of the data from which they learn. It is often a well-tailored dataset, with well-tailored annotations, that is the driving force behind advanced machine learning breakthroughs.

Fieldwork can be very challenging, requiring great passion, teamwork, perserverance and grit. We are very grateful to scientists for this work, which is essential for our mission to decode animal communication and language. Thank you.

# Datasets

The Earth Species Library is a diverse collection of multi-modal (primarily acoustic) datasets meant to train increasingly complex machine learning models across the wide array of data and species.  These datasets are available to the public, easily downloadable, and preprocessed for machine learning. Some repositories include some initial deep learning experiments with instructions for how to reproduce the results.

### Examples
* [bird songs](https://github.com/earthspecies/library/tree/main/bird_songs): 686 recordings of bird vocalizations with 87 labels. Construction of PyTorch dataloaders for classification.
* [Egyptian fruit bats](https://github.com/earthspecies/library/tree/main/egyptian_fruit_bat)- 300,000 unique vocalizations recorded and 90k labeled annotations. Classified on interaction context using fastai's pretrained resnet models.
* [giant otter](https://github.com/earthspecies/library/tree/main/giant_otter) - 441 recordings among 22 distinct vocalization types. Complete ML pipeline applied to giant otter bioacoustics, beginning with data preprocessing, proceeding to load the data, and culminating in the construction and training of a CNN-based classifier.
* [macaques](https://github.com/earthspecies/library/tree/main/macaques) - 7285 macaque coo calls from 8 individuals (4 males and 4 females). There is a [collaborative tutorial](https://github.com/earthspecies/open_collaboration_on_audio_classification) of techniques to recover identity from voice.

For a complete up-to-date list of all of the datasets available, visit [here](https://github.com/earthspecies/library).
