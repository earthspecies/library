# The Earth Species Project library

> curated audio datasets for animal research

* [zebra_finch](https://github.com/earthspecies/esp_library/tree/main/zebra_finch) - 3405 zebra finch calls classified across 11 call types. Additonal labels include name of individual making the vocalization and its age (chick or adult).
* [macaques](https://github.com/earthspecies/esp_library/tree/main/macaques) - 7285 macaque coo calls from 8 individuals (4 males and 4 females). There is a [collaborative tutorial](https://github.com/earthspecies/open_collaboration_on_audio_classification) of techniques to recover identity from voice.
* [giant otter](https://github.com/earthspecies/library/tree/main/giant_otter) - A tutorial demonstrating a complete ML pipeline applied to giant otter bioacoustics, beginning with data preprocessing, proceeding to load the data, and culminating in the construction and training of a CNN-based classifier capable of labeling giant otter vocalizations according to call type.
* [Egyptian fruit bats](https://github.com/earthspecies/library/tree/main/egyptian_fruit_bat)- Approximately 8k Egyptian fruit bat vocalizations classified on interaction context using fastai's pretrained resnet models. 

All datasets are accessible by issuing a single command from within the [fastai v2 library](https://github.com/fastai/fastai2).

## Available models

| dataset | architecture |
| :----------: |:-------------|
| giant otter | [conv2d classifier with an interactive gui](https://github.com/earthspecies/library/blob/main/giant_otter/cnn-classifier-pipeline.ipynb)|
|macaques|[conv1d classifier on raw audio](https://github.com/earthspecies/library/blob/main/macaques/fastai2_audio_conv1d.ipynb)|
|macaques|[xresnet18 classifier with fastai audio](https://github.com/earthspecies/library/blob/main/macaques/fastai2_audio_xresnet18.ipynb)|
|macaques|[pretrained resnet18 using fastai DataBlock api and error analysis](https://github.com/earthspecies/library/blob/main/macaques/introduction.ipynb)|
|macaques|[ROCKET model extracting information from raw audio using conv1d without training](https://github.com/earthspecies/library/blob/main/macaques/ROCKET_Sound/MacaqueROCKET.ipynb)|
|zebra finch|[pretrained resnet18 classifier with confusion matrix using fastai](https://github.com/earthspecies/library/blob/main/zebra_finch/example_of_working_with_the_dataset.ipynb)|
