# Elephants

<img src="https://en.wikipedia.org/wiki/File:African_Elephant_(Loxodonta_africana)_male_(17289351322).jpg" alt="An elephant" width="120" align="left">

The [African elephant](https://en.wikipedia.org/wiki/African_elephant) (Loxodonta) is a genus comprising two living elephant species, the African bush elephant (L. africana) and the smaller African forest elephant (L. cyclotis). Both are social herbivores with grey skin, but differ in the size and color of their tusks and in the shape and size of their ears and skulls.

Both species have been listed as vulnerable on the IUCN Red List since 2004, and are threatened by habitat loss and fragmentation. Poaching for the illegal ivory trade is a threat in several range countries as well.

## Dataset information

This dataset contains 7285 macaque coo calls from 8 individuals (4 males and 4 females) with labels at the individual level. 5756 vocalizations have been recorded with a sampling rate of 24414 Hz and 1529 with a sampling rate of 44100 Hz. The duration of wav files varies from 896 frames to 37308 frames (0.04s to 1.69s).

Data is available for download from Internet Archive as [a single zip file](https://archive.org/details/macaque_coo_calls). This is a version of the dataset that has been peprocessed by us to facilitate the application of machine learning techniques. The preprocessing steps that have been taken are documented in [99_Data_Preprocessing](https://github.com/earthspecies/library/blob/main/macaques/99_Data_Preprocessing.ipynb).

## Table of contents

1. [How to download the dataset](https://github.com/earthspecies/library/blob/main/macaques/01_Download_Dataset.ipynb).
2. [How to construct PyTorch dataloaders for classification](https://github.com/earthspecies/library/blob/main/macaques/02_Create_PyTorch_DataLoaders.ipynb).
3. [How to construct PyTorch dataloaders for the cocktail party problem](https://github.com/earthspecies/library/blob/main/macaques/03_Construct_PyTorch_Dataloaders_for_CPP.ipynb).

## Citations

This dataset has been collected and shared by Makoto Fukushima, Alex M. Doyle, Matthew
P. Mullarkey, Mortimer Mishkin and Bruno B. Averbeck under the [Distributed acoustic cues for caller identity in macaque vocalization](https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4806230/) paper. The original dataset can be downloaded from [Data Dryad](https://datadryad.org/stash/dataset/doi:10.5061/dryad.7f4p9). 
