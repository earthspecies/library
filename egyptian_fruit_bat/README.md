Exploring Egyptian Fruit Bat Vocalizations
===

This repo can serve as a brief introduction to working with the [Egyptian fruit bat datasets](https://www.nature.com/articles/sdata2017143). The full dataset contains ~300k vocalization samples,
~90k of which are annotated. The data are split up into three lumps, one set containing everything from the source 
(found [here](https://archive.org/details/egyptian_fruit_bat)) another containing just the annotations 
(found [here](https://archive.org/details/egyptian_fruit_bat_annotated)), and another containing a small subset of the 
annotated data (found [here](https://archive.org/details/egyptian_fruit_bat_annotated_tiny)). The larger two datasets are quite
large even in a zipped archive format (~100GiB and ~40GiB) and have to be accessed using 7zip (since the files were 7zipped from the Figshare source). The script `efb_context_labeler.ipynb` shows how to download the data locally using `wget` and `7z`. 

In the script `efb_context_labeler.ipynb`, we train a resnet model to predict
the context of a vocalization interaction from a subset of the annotated dataset. 

The scripts `bat_spectrogram_tuner.ipynb` and `rainbow-ification_exploration.ipynb` demonstrate some methods of representing audio signals as images in the context of machine learning.

The file `relevant_file_info.zip` contains the metadata, annotations, and file information for the vocalization data should anyone need it.

The script `bat_file_handler_sandbox.py` is the sandbox of functions and processes used to disperse the larger dataset into smaller chunks (hopefully no one will need to work through this script, and it's only included for posterity/clarity)


