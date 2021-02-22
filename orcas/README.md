# Orcas

<img src="https://upload.wikimedia.org/wikipedia/commons/3/37/Killerwhales_jumping.jpg" alt="A macaque" width="120" align="left">

The [killer whale (Orcinus orca)](https://en.wikipedia.org/wiki/Killer_whale), also known as the orca, is a toothed whale belonging to the oceanic dolphin family, of which it is the largest member. Killer whales have a diverse diet, although individual populations often specialize in particular types of prey. Some feed exclusively on fish, while others hunt marine mammals such as seals and other species of dolphin. They have been known to attack baleen whale calves, and even adult whales. Killer whales are apex predators, as no animal preys on them. A cosmopolitan species, they can be found in each of the world's oceans in a variety of marine environments, from Arctic and Antarctic regions to tropical seas, absent only from the Baltic and Black seas, and some areas of the Arctic Ocean.

Killer whales are highly social; some populations are composed of matrilineal family groups (pods) which are the most stable of any animal species. Their sophisticated hunting techniques and vocal behaviours, which are often specific to a particular group and passed across generations, have been described as manifestations of animal culture.
s are the most widespread primate genus.


## Dataset information

This dataset comes from the [Orcasound Project](https://www.orcasound.net/). We share two versions of the dataset - one suited for classification and the other for other research tasks. The audio has been recorded with an SR of 44100 Hz.

The dataset intended for classification consists of 4 second examples, and contains 398 positive examples and 196 negative examples. It can be downloaded from Internet Archive [here](https://archive.org/details/orcas_classification).

The dataset suited for indexing into a recording consits of a single 30 minute long wave file. It comes with annotations that pinpoint each of the 398 calls in the recording (annotated by Scott Veirs). It can be downloaded from Internet Archive [here](https://archive.org/details/orcas_offsets).

## Table of contents

1. [How to download the dataset](https://github.com/earthspecies/library/blob/main/macaques/01_Download_Dataset.ipynb).
2. [How to construct PyTorch dataloaders for classification](https://github.com/earthspecies/library/blob/main/macaques/02_Create_PyTorch_DataLoaders.ipynb).
3. [How to construct PyTorch dataloaders for the cocktail party problem](https://github.com/earthspecies/library/blob/main/macaques/03_Construct_PyTorch_Dataloaders_for_CPP.ipynb).
