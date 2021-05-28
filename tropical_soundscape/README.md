# tropical soundscape

<img src="https://upload.wikimedia.org/wikipedia/commons/0/0d/Puerto_Rico_El_Yunque_1.jpg" width="120" align="left">

This dataset contains 4727 tropical soundscape recordings. A total of 24 bird and frog species have been identified to be present in this dataset.

These were collected from 733 sites in Puerto Rico, using Audiomoth recorders. The devices were programmed to record 1 minute of audio every 10 minutes for a total of 144 recordings per day at a sampling rate of 48 kHz. A small portion (~7%) of recordings were sampled at 44.1 kHz. 

64% of recordings with annotations came from 152 sites throughout the El Yunque National Forest. Recordings from other sites and older years were searched to increase the training sample size for certain species. 79% of recordings were collected in 2019, 14% in 2018, and 7% collected between 2015 and 2018.

This dataset was created from the train portion of data used for [the Rainforest Connection Species Audio Detection Kaggle competition](https://www.kaggle.com/c/rfcx-species-audio-detection/overview). We preprocess the data to make it more amenable to being fed into a DL pipeline.


## Dataset information

This dataset consists of 4727 audio files, each of 1-minute length. All audio has been recorded with a sampling rate of 48 kHz.

24 bird and frog species can be heard in the recordings. Both file level labels are provided, as well as information allowing to draw a bounding box surrounding a vocalization.

This dataset is available on [archive.org](https://archive.org/details/tropical_soundscape).

## Cite this collection
J. LeBien, M. Zhong, M. Campos-Cerqueira, et al., A pipeline for identification of bird and frog species in tropical soundscape recordings using a convolutional neural network, Ecological Informatics (2019), https://doi.org/10.1016/j.ecoinf.2020.101113

## Table of contents

1. [How to download the dataset](https://github.com/earthspecies/library/blob/main/tropical_soundscape/01_Download_Dataset.ipynb).
2. [Data Exploration](https://github.com/earthspecies/library/blob/main/tropical_soundscape/02_Data_Exploration.ipynb).
3. [Data Preprocessing](https://github.com/earthspecies/library/blob/main/tropical_soundscape/99_Data_Preprocessing.ipynb)

