Exploring Egyptian Fruit Bat Vocalizations:
===
This repository can serve as a brief introduction to working with the [Egyptian fruit bat datasets](https://www.nature.com/articles/sdata2017143). The full dataset contains ~300k vocalization samples,
~90k of which are annotated. A brief description of the scripts above can be found in the list below, with more discussion on the objectives and results of the notebooks in the 'Explorations and Results' section. 

* In the script `efb_context_labeler.ipynb`, we train a resnet model to predict
the context of a vocalization interaction from a subset of the annotated dataset. 

* The scripts `bat_spectrogram_tuner.ipynb` and `rainbow-ification_exploration.ipynb` demonstrate some methods of representing audio signals as images in the context of machine learning.

* The file `relevant_file_info.zip` contains the metadata, annotations, and file information for the vocalization data should anyone need it.

* The script `bat_file_handler_sandbox.py` is the sandbox of functions and processes used to disperse the larger dataset into smaller chunks.

* The script `efb_vocalization_PCA.ipynb` delves into the clustering of bat vocalizations, and investigates the distances between clusters labeled by different contexts. 

* The notebook `efb_context_labeler_pos_enc .ipynb` is a more custom extension of the original context labeling model, exploring the use of stronger positional encoding compared to 'rainbow-ification'. 

* The notebook `efb_context_labeler_pos_enc_comparison.ipynb` just compares convolutional models with and without positional encoding. 

* In the notebook `efb_voc_comp_unet.ipynb`, a custom dynamic unet with positional encoding was trained to complete bat vocalizations given a truncated call (WIP).

* The notebook `efb_vae.ipynb` explores a custom autoencoding architecture, with the hopes of probing the embedding layers for further clustering analysis (WIP).





The Data:
===
The original bat vocalization data was recorded and labeled by [Yossi Yovel](http://www.yossiyovel.com/index.php/publications) and his team. This data set must have taken an incredible amount of work, with 300k unique vocalizations recorded and 90k labeled annotations, and we are so thankful to be able to use it! You can view the original paper publishing the data [here](https://www.nature.com/articles/sdata2017143). 

The data are split up into three lumps, one set containing everything from the source, another containing just the annotations, and another containing a small subset of the annotated data. The larger two datasets are quite large even in a zipped archive format (so be prepared to wait!) and have to be accessed using 7zip (since the files were 7zipped from the Figshare source). The script `efb_context_labeler.ipynb` shows how to download the data locally using `wget` and `7z`. 

1. The full vocalization dataset can be found [here](https://archive.org/details/egyptian_fruit_bat) (~200 GiB unzipped)

2. The full set of annotated vocalizations can be found [here](https://archive.org/details/egyptian_fruit_bat_annotated) (~125 GiB unzipped)

3. A "tiny" subset of the annotated vocalizations can be found [here](https://archive.org/details/egyptian_fruit_bat_annotated_tiny) (~10 GiB unzipped)

All of the subsets of the original data are split up in the same way:
```
Egyptian_fruit_bat_unzipped
├── Annotations.csv
├── better_annotations.csv
├── FileInfo.csv
├── files101/
├── files102/
├── files103/
├── files104/
├── files105/
├── files106/
├── files201/
├── files202/
├── files203/
├── files204/
├── files205/
├── files206/
├── files207/
├── files208/
├── files209/
├── files210/
├── files211/
├── files212/
├── files213/
├── files214/
├── files215/
├── files216/
├── files217/
├── files218/
├── files219/
├── files220/
├── files221/
├── files222/
├── files223/
└── files224/
```

The directories `files###` are where the WAV-type audio vocalizations are stored, and the csv's are where the file info and annotations can be found. The file `better_annotations.csv` does not actually make the annotations any better than they already are, it simply joins the information contained in the original `Annotations.csv` with the file information in `FileInfo.csv`. (Joining the file ID and annotations for each file with the file name and path so that we can more easily grab the annotations for each file) 

Prat, Yosef; Taub, Mor; Pratt, Ester; Yovel, Yossi (2017): An annotated dataset of Egyptian fruit bat vocalizations across varying contexts and during vocal ontogeny. figshare. Collection. https://doi.org/10.6084/m9.figshare.c.3666502.v2


Explorations and Results:
===
The Egyptian fruit bat datasets record interactions between bats located in isolation chambers. The vocalizations typically occur between two bats, one labeled as the `emitter` and the other the `receiver`, and the labels for the vocalization samples were observed/generated from synchronized video recordings (You can peruse the metadata [here](https://ia903204.us.archive.org/view_archive.php?archive=/19/items/egyptian_fruit_bat_annotated/egyptian_fruit_bat_annotated.zip&file=Metadata.pdf)). The notebook `efb_context_labeler.ipynb` attempts to characterize the context (as labeled in the provided dataset) of a bat vocalization by studying the visual structure of the audio signal recorded during an interaction. Below is the "context" class label distribution for the `egyptian_fruit_bat_annotated_tiny` dataset: 

![alt text](https://github.com/oliver-adams-b/library/blob/main/egyptian_fruit_bat/images/class_dist_in_tiny.png)

The class labels counts / datasample counts for the tiny annotated dataset were augmented so there is more of an even distribution of labels. In the full annotated dataset, however, the class label distribution is greatly skewed with nearly 60% of class label counts being either `sleeping` or `feeding`. In the notebook `efb_context_labeler.ipynb`, the audio signals were augmented using the [CQ transform](https://en.wikipedia.org/wiki/Constant-Q_transform) and some simple time-color encoding, more information on the data augmentation and the thought that went into it can be found in the notebooks `bat_spectrogram_tuner.ipynb` and `rainbow-ification_exploration.ipynb`. The off-the-shelf model trained in `efb_context_labeler.ipynb` only achieved around 55% accuracy.

The low accuracy achieved by the model in `efb_context_labeler.ipynb` inspired further explorations into the clustering of the image-space of the bat vocalizations. Clustering analysis was carried out in the notebook `efb_vocalization_PCA.ipynb`, where PCA was applied to a random subset of CQ transformed bat vocalizations. The pairwise distance between embedded clusters with different context labels was measured, and it was found that in some cases the model has a harder time discerning between clusters whose approximate Jensen-Shannon distance was smaller (not too surprising that similar clusters are harder to distinguish, but the qualitative validation was nice). For reference, a t-SNE clustering of bat vocalizations labeled by context can be found below:

![alt text](https://github.com/oliver-adams-b/library/blob/main/egyptian_fruit_bat/images/context.png)

From here, more explorations were conducted on improving the 'rainbow-ification' by creating more custom models and layers to explore better ways of working with the data. A stronger form of 'rainbow-ification' (or just positional encoding) was developed and tested in the notebook `efb_context_labeler_pos_enc .ipynb`. A simple custom convolutional model was used to compare the positional encoding layer to the baseline (no positional encoding) in the notebook `efb_context_labeler_pos_enc_comparison.ipynb`, and it was observed that this flavor of positional encoding may improve model accuracy/understanding of the provided data.  

After the positional encoding layer showed some promise, it was put to good use in the notebooks `efb_voc_comp_unet.ipynb` and `efb_vae.ipynb`. In the notebook `efb_voc_comp_unet.ipynb`, a dyanmic unet was fed the first half of a bat vocalization and was tasked in completing the remainder of the vocalization (to some success). In the notebook `efb_vae.ipynb`, a simple autoencoder was explored with the hopes that the embedding layers may shed more light on the clustering of context labels (still a work in progress). 

Potential Next Steps:
===
* Some work could be done to mitigate the regularization of the model to improve model performance. For example: working with different subsets of the data, changing model architecture, or exploring different avenues of data augmentation. 

* In the research paper found [here](https://www.nature.com/articles/srep39419), a model was trained to predict 4 categories of vocalization context and achieved 50% accuracy, and it might be insightful to attempt to reproduce and potentially improve these results. 


