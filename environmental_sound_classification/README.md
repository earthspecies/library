# envirornmental sound classification

The ESC-50 dataset is a labeled collection of 2000 environmental audio recordings suitable for benchmarking methods of environmental sound classification.

The dataset consists of 5-second-long recordings organized into 50 semantical classes (with 40 examples per class) loosely arranged into 5 major categories:

* Animals
* Natural soundscapes & water sounds
* Human, non-speech sounds
* Interior/domestic sounds
* Exterior/urban noises

Clips in this dataset have been manually extracted from public field recordings gathered by the Freesound.org project. The dataset has been prearranged into 5 folds for comparable cross-validation, making sure that fragments from the same original source file are contained in a single fold.

A more thorough description of the dataset is available in the [original paper](http://karol.piczak.com/papers/Piczak2015-ESC-Dataset.pdf). This dataset is shared on GitHub [at this location](https://github.com/karolpiczak/ESC-50).


## Dataset information

This dataset consists of 2000 5-second recordings. The recordings were sampled across 50 classes and the dataset is balanced - 40 recordings are provided for each of the classes.

All the recordings are single channel and have been recorded with a sampling rate of 44.1 kHz.

## Table of contents

1. [How to download the dataset](https://github.com/earthspecies/library/blob/main/environmental_sound_classification/01_Download_Dataset.ipynb).
2. [Data Exploration](https://github.com/earthspecies/library/blob/main/environmental_sound_classification/02_Data_Exploration.ipynb).
3. [Data Preprocessing](https://github.com/earthspecies/library/blob/main/environmental_sound_classification/99_Data_Preprocessing.ipynb)
