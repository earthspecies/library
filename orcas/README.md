# Orcas

<img src="https://upload.wikimedia.org/wikipedia/commons/4/43/Bonnet_macaque_%28Macaca_radiata%29_Photograph_By_Shantanu_Kuveskar.jpg" alt="An orca" width="120" align="left">

The [macaques](https://en.wikipedia.org/wiki/Macaque) inhabit ranges throughout Asia, North Africa, and Gibraltar. They are principally frugivorous (preferring fruit), although their diet also includes seeds, leaves, flowers, and tree bark. All macaque social groups are matriarchal, arranged around dominant females. Aside from humans (genus Homo), the macaques are the most widespread primate genus.

## Dataset information

This dataset comes from the [Orcasound Project](https://www.orcasound.net/). We share two versions of the dataset - one suited for classification and the other for other research tasks. The audio has been recorded with an SR of 44100 Hz.

The dataset intended for classification consists of 4 second examples, and contains 398 positive examples and 196 negative examples. It can be downloaded from Internet Archive here.

The dataset suited for indexing into a recording consits of a single 30 minute long wave file. It comes with annotations that pinpoint each of the 398 calls in the recording. It can be downloaded from Internet Archive here>

## Table of contents

1. [How to download the dataset](https://github.com/earthspecies/library/blob/main/macaques/01_Download_Dataset.ipynb).
2. [How to construct PyTorch dataloaders for classification](https://github.com/earthspecies/library/blob/main/macaques/02_Create_PyTorch_DataLoaders.ipynb).
3. [How to construct PyTorch dataloaders for the cocktail party problem](https://github.com/earthspecies/library/blob/main/macaques/03_Construct_PyTorch_Dataloaders_for_CPP.ipynb).
