Exploring Egyptian Fruit Bat Vocalizations:
===

This repository can serve as a brief introduction to working with the [Egyptian fruit bat datasets](https://www.nature.com/articles/sdata2017143). The full dataset contains ~300k vocalization samples,
~90k of which are annotated. 

* In the script `efb_context_labeler.ipynb`, we train a resnet model to predict
the context of a vocalization interaction from a subset of the annotated dataset. 

* The scripts `bat_spectrogram_tuner.ipynb` and `rainbow-ification_exploration.ipynb` demonstrate some methods of representing audio signals as images in the context of machine learning.

* The file `relevant_file_info.zip` contains the metadata, annotations, and file information for the vocalization data should anyone need it.

* The script `bat_file_handler_sandbox.py` is the sandbox of functions and processes used to disperse the larger dataset into smaller chunks.

The Data:
===

The data are split up into three lumps, one set containing everything from the source, another containing just the annotations, and another containing a small subset of the annotated data. The larger two datasets are quite large even in a zipped archive format (so be prepared to wait!) and have to be accessed using 7zip (since the files were 7zipped from the Figshare source). The script `efb_context_labeler.ipynb` shows how to download the data locally using `wget` and `7z`. 

1. The full vocalization dataset can be found [here](https://archive.org/details/egyptian_fruit_bat) (~200 GiB unzipped)

2. The full set of annotated vocalizations can be found [here](https://archive.org/details/egyptian_fruit_bat_annotated) (~125 GiB unzipped)

3. A "tiny" subset of the annotated vocalizations can be found [here](https://archive.org/details/egyptian_fruit_bat_annotated_tiny) (~10 GiB unzipped)

Explorations:
===

The Egyptian fruit bat datasets record interactions between bats located in isolation chambers. The vocalizations typically occur between two bats, one labeled as the `emitter` and the other the `receiver`, and the labels for the vocalization samples were observed/generated from synchronized video recordings (You can peruse the metadata [here](https://ia903204.us.archive.org/view_archive.php?archive=/19/items/egyptian_fruit_bat_annotated/egyptian_fruit_bat_annotated.zip&file=Metadata.pdf)). The notebook `efb_context_labeler.ipynb` attempts to characterize the "context" of a bat vocalization by studying the visual structure of the audio signal recorded during an interaction. Below is the "context" class label distribution for the `egyptian_fruit_bat_annotated_tiny` dataset: 

![alt text](https://github.com/oliver-adams-b/library/blob/main/egyptian_fruit_bat/images/class_dist_in_tiny.png)

The class labels counts / datasample counts for the tiny annotated dataset were augmented so that there is more of an even distribution of labels. In the full annotated dataset, however, the class label distribution is greatly skewed with nearly 60% of class label counts being either `sleeping` or `feeding`. The audio signals were augmented using the [CQ transform](https://en.wikipedia.org/wiki/Constant-Q_transform) and some simple time-color encoding, more information on the data augmentation and the thought that went into it can be found in the notebooks `bat_spectrogram_tuner.ipynb` and `rainbow-ification_exploration.ipynb`. Below is what a few vocalization samples look like before they are fed into the model: 

![alt text](https://github.com/oliver-adams-b/library/blob/main/egyptian_fruit_bat/images/batch_context_w_rainbows.png)

