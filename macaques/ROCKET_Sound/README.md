radek has suggested working directly on the timeseries as another approach. I'd like to present a starter notebook that hits 97.3% classification accuracy using only conv1d, two simple pooling functions, and a Linear classifier...16,000 parameters.

The method is called ROCKET. You may have seen it already discussed in  https://forums.fast.ai/t/time-series-sequential-data-study-group/29686. The original code and paper can be found at https://github.com/angus924/rocket.  For those not familiar, here is a brief overview.

ROCKET extracts a set of features, typically several thousand numbers, from each timeseries sample (in this case the Macaque calls). The features are then run through a classifier to train the model to predict a category. The classifier (at least the ones I have seen used so far) is simply a linear combination of weights. Oguza's demo, the original paper, and my attached demo all use sklearn's RidgeClassifier. You could just as well use the more familiar Linear/softmax/Cross entropy/optimizer setup, even appending more layers.

The power of ROCKET, though, lies in its features. These are generated by running each sample through a large set of fixed conv1d's. Each conv1d has randomized weights centered on zero, and randomized biases. The output of each conv1d, a series itself, is then reduced to two numbers. The first is simply the maximum of the series. The second is the fraction of positive values in the series, the 'proportion of positive values' (ppv). In this way, each timeseries sample yields a list of numbers (features) that characterize it, of length two times the number of random convolutions. As with spectrogram images, it's these features that are sent to the classifier.

It is important to note that the weights and biases of the conv1d's are fixed. Contrary to our usual practice, they are not trained during the optimization of the classifier.

Getting into opinion and speculation, I think ROCKET effectively does a search of the space of conv1d's by using a large universe of random kernel lengths, weights, biases, dilations, and paddings. The classifier selects which of these conv1d's are predictive of the training samples. Rather than predesigning the architecture as we typically do, this approach finds the conv1d's that work best for the problem.

Such a search would be impossible using typical machine learning methods because most of its parameters are not differentiable wrt loss. Two non-linearities, both of which are also non-differentiable, then reduce the dimensionality of the conv1d outputs. IMO, there's great potential in this approach of using randomness to search the space of architectures and weights. You can find papers that suggest that the olfactory system's random connections work in a similar way. Also, see weight-agnostic architectures.
-----------------------------

Questions:

Why does one take fixed Conv1d layers and not learn their parameters instead?

I think the fundamental reason is that it is meant to be an entirely different approach than gradient descent. You make a huge number of cheap features (fixed, random) and let a simple linear classifier learn which ones are predictive. The usual ML methods can learn a kernel and a bias for a particular conv1d, but they cannot learn across kernel lengths and dilations. Those parameters are non-differentiable. The reduction to ppv and max is likewise non-differentiable. Therefore an optimizer can’t see the effect of varying bias and kernel weights.

You could think of ROCKET as a way to search a very large parameter space that gradient descent cannot traverse. In a manner, it searches across model architectures. Instead of pre-defining a model with fixed conv dilations and ppv thresholds, the method finds which ones work the best.
-------------------------------

Some further notes...
1) The various dilations of conv1d are able to extract the periodicities (frequencies) of the sounds, much as spectograms do. I think that's one reason ROCKET works well on this audio task. 

2) Although ROCKET looks computationally intensive, I find that most of the trained classification coefficients end up very small. (This is not my idea - I downloaded a notebook that shows this observation, but don't know who originally authored it.) It means those conv1d's could be eliminated, or replaced with different randomly sampled conv1d's that may turn out to work better. 

3) There's some special magic in the ppv non-linearity. Combined with conv1d, it is exceptionally good at classifying time series in general. Why is that so?
---

Notes on my second implementation (based on Ignacio Oguiza's ROCKET demo at https://github.com/timeseriesAI/timeseriesAI -thanks!)

First, run notebook saveSounds. It saves the Macaque calls and names into ~.fastai. These will be loaded by the following notebook.

Second, run notebook MacaqueROCKET for a demonstration of the ROCKET method. It requires fastai2 only for the last section. These notebooks are not tested on servers. They were run locally only.

The biggest issue was dealing with variable length samples. ROCKET is not limited to fixed length samples, but works most straightforwardly with them. There is already discussion of this issue in depth in the Time Series Sequential Data Study Group. One simple idea is to pad each sample with zeros to the same (longest) length. However doing so drastically alters the max and ppv measures, and empirically decreases accuracy.

The primary problem with using different length samples is when randomly chosen kernel length, padding, and dilation for conv1d yield different length outputs, all within one batch. Even more, what should be the max and ppv of a zero length conv1d output (short sample and large dilation)?

The issue is especially acute in PyTorch, because of course tensors have to be rectangular. I experimented extensively with conv1d to find out exactly how it handles padding with nans/zeros, when it errors out, etc. I think this ROCKET implementation is correct when samples are padded on the right with nan, even when the conv1d output is empty. It throws an error however when the input tensor input sample length dimension is too small for a particular conv1d.

In the end, I did not tackle this last problem. Instead, I limited the dilations so that the shortest sample is always valid for every conv1d. This measured nearly as accurate as including larger dilations. Perhaps it's because we are identifying voice timbres by frequencies and formants. Such frequencies are already captured by the smaller dilations. If you are looking for larger structures in a call - the meaning of bass notes for instance - the larger dilations would be needed.

---
Notes on the problem...

It's an easy one in the grand scheme. In essence, we are distinguishing voices. That can be done quite well using pitch and timbre alone, which both spectrograms and conv1d can extract. But both methods have difficulty detecting temporal patterns. Resnet detects features in an image, but does not know whether they are located in the upper left or lower right. ROCKET loses the time structure by pooling it away with ppv and max.

If the distant goal is to recognize the meaning of the calls, we will want to *ignore* pitch and timbre and focus on the call's structure along the time dimension. It will require some kind of time-aware architecture like an RNN. Just sayin' for now.

---
Directions and ideas (in case anyone is inspired)

- Replace the unused conv1d features with new random ones. Does accuracy keep improving?

- Do the most predictive conv1d's have certain characteristics in common? If so, we get a sense of how to design a model based on conv1d. Some interesting visualizations are shown.

- Find a better way to adapt ROCKET to time series with different lengths. Right now the space of dilations assumes the series has a fixed length. Many conv1d's with large dilations remain unused because they do not apply to short samples. Is there a way to better distribute the conv1d's to match the distribution of sample lengths? In fact, changing the distribution of the dilations DOES help. See comments in rockersound1.py.

- With a typical Linear/Cross entropy training on the features, would more layers find complex feature patterns that improve generalization?

- Make a more efficient implementation that skips the overhead of nn.conv1d. We could go directly to F.conv because we already know the parameters are safe.

Thanks for reading and for code corrections!