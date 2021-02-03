# Elephants

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/b/bf/African_Elephant_%28Loxodonta_africana%29_male_%2817289351322%29.jpg/440px-African_Elephant_%28Loxodonta_africana%29_male_%2817289351322%29.jpg" alt="An elephant" width="120" align="left">

The [African elephant](https://en.wikipedia.org/wiki/African_elephant) (Loxodonta) is a genus comprising two living elephant species, the African bush elephant (L. africana) and the smaller African forest elephant (L. cyclotis). Both are social herbivores with grey skin, but differ in the size and color of their tusks and in the shape and size of their ears and skulls.

Both species have been listed as vulnerable on the IUCN Red List since 2004, and are threatened by habitat loss and fragmentation. Poaching for the illegal ivory trade is a threat in several range countries as well.

## Dataset information

We provide two datasets. The first one consists of 314 annotated calls with labels such as call type, caller name, call context, caller sex, caller age and field notes. You can find this dataset on Internet Archive [here](https://archive.org/details/elephant_rumbles).

The second dataset that we make available consists of 737 unlabeled African elephant rumbles. It can be downloaded from Internet Archive from [this location](https://archive.org/details/elephant_rumbles_unlabeled).

The original dataset collected and annotated by [ElephantVoices](https://www.elephantvoices.org/) can be found [here](https://archive.org/details/elephants_raw). The preprocessing steps that we have taken in constructing the two datasets are documented in [99_Data_Preprocessing](https://github.com/earthspecies/library/blob/main/elephants/99_Data_Preprocessing.ipynb).

## Table of contents

1. [How to download the dataset](https://github.com/earthspecies/library/blob/main/macaques/01_Download_Dataset.ipynb).
2. [How to construct PyTorch dataloaders for classification](https://github.com/earthspecies/library/blob/main/macaques/02_Create_PyTorch_DataLoaders.ipynb).