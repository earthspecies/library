# Bird songs

<img src="https://upload.wikimedia.org/wikipedia/commons/a/a7/RedcrestedTuraco.jpg" alt="A bird" width="120" align="left">

[Birds](https://en.wikipedia.org/wiki/Bird) are a group of warm-blooded vertebrates constituting the class Aves, characterised by feathers, toothless beaked jaws, the laying of hard-shelled eggs, a high metabolic rate, a four-chambered heart, and a strong yet lightweight skeleton. Birds live worldwide and range in size from the 5.5 cm (2.2 in) bee hummingbird to the 2.8 m (9 ft 2 in) ostrich. There are about ten thousand living species, more than half of which are passerine, or "perching" birds. Bird vocalizations are highly varied, containing natural variation across a range of timescales.


## Dataset Information

This dataset consists of songs and calls of multiple bird species (87 distinct labels). It was collected by [BIOTOPE](http://www.biotope.fr/) society and shared for the [Neural Information Processing Scaled for Bioacoustics: NIPS4B](http://sabiod.univ-tln.fr/nips4b/challenge1.html), a bird song competition which asked participants to identify which of 87 sound classes of birds and their ecosystem are present in 1000 continuous wild recordings from different places in Provence, France. 

The training set consists of 687 audio files, with multiple labels per recording, recorded by automated monitoring units (SM2 System) with a sampling rate of 44100 Hz. Recording length varies from just above 1 second to just above 5 seconds.

This dataset can be downloaded from Internet Archive [here](https://archive.org/download/bird_songs).

## Table of contents

1. [How to download the dataset](https://github.com/earthspecies/library/blob/main/bird_songs/01_Download_Dataset.ipynb).
2. [How to construct PyTorch dataloaders for classification](https://github.com/earthspecies/library/blob/main/bird_songs/02_Create_PyTorch_DataLoaders.ipynb).

