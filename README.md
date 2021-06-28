# An Introduction

Fieldwork is an essential component of the work to decode non-human language and communication.  Collectively, biologists have lifetimes of invaluable observations from the field, but most of these recordings – scattered across cloud storage, hard drives, old tapes, and hidden servers – may be difficult to access. Further, bioacoustic recordings often include a medley of biophony, geophony, and anthropophony which make it hard to get to a starting point where you can begin experimentation. And, commonly, datasets are hand-labelled which may lead to human error. The Earth Species Library is an open and free repository that pulls together all of these incredible observations, documents them, and makes them ready for machine learning.   

A major roadblock in translating animal communication is having enough of the right kinds of data with the right kinds of annotations. No matter how advanced the algorithm, the quality of what they learn derives from the quality of the data from which they learn. It is often a well-tailored dataset, with well-tailored annotations, that is the driving force behind advanced machine learning breakthroughs. 

Fieldwork can be very challenging, requiring great passion, teamwork, perserverance and grit. We are very grateful to scientists for this work, which is essential for our mission to decode non-human communication and language. Thank you.

# Datasets

The Earth Species Library is a diverse collection of multi-modal (primarily acoustic) datasets meant to train increasingly complex machine learning models across the wide array of data and species.  These datasets are available to the public, easily downloadable, and preprocessed for machine learning. Some repositories include some initial deep learning experiments with instructions for how to reproduce the results. There are many more data sets that we have not yet been able to make public. We hope to do so in the future.

### Examples 

| Name  | Description | Notes |
| ------------- | ------------- | ------------ |
| [Bird Song](https://github.com/earthspecies/library/tree/main/bird_songs) | 686 recordings of bird vocalizations with 87 labels. | Includes a PyTorch dataloaders for classification.  |
| [Egyptian Fruit Bat](https://github.com/earthspecies/library/tree/main/egyptian_fruit_bat)  | 300,000 unique vocalizations recorded and 90k labeled annotations.  | Included is predicting interaction context using a pretrained resnet model. |
| [Giant Otter](https://github.com/earthspecies/library/tree/main/giant_otter) | 441 recordings among 22 distinct vocalization types. | Includes a classifier. |
| [Macaques Monkeys](https://github.com/earthspecies/library/tree/main/macaques) | 7285 macaque coo calls from 8 individuals (4 males and 4 females) | Includes a [tutorial](https://github.com/earthspecies/open_collaboration_on_audio_classification) to predict identity from voice. |

For an up-to-date list of the publicly available the datasets, visit [here](https://github.com/earthspecies/library). 
