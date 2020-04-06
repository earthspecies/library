# Original PyTorch implementation by Oguiza.
# Adapted to variable length samples by Malcolm Mclean, 20200401, no joke.

# This is an unofficial Multivariate, GPU (PyTorch) implementation by Ignacio Oguiza - oguiza@gmail.com based on:
# Dempster, A., Petitjean, F., & Webb, G. I. (2019). ROCKET: Exceptionally fast and accurate time series classification using random convolutional kernels. arXiv preprint arXiv:1910.13051.
# GitHub code: https://github.com/angus924/rocket

import torch
import torch.nn as nn
import numpy as np
#import torch.nn.functional as F
import random

class ROCKET(nn.Module):
    def __init__(self, c_in, seq_len, n_kernels=10000, kss=[7, 9, 11]):
        
        '''
        ROCKET is a GPU Pytorch implementation of the original ROCKET methods generate_kernels and apply_kernels that can be used with univariate and multivariate time series.
        Input: is a 3d torch tensor of type torch.float32. When used with univariate TS, make sure you transform the 2d to 3d by adding unsqueeze(1)
        c_in: number of channels in (features). For univariate c_in is 1.
        seq_len: sequence length (is the last dimension of the input)
        '''
        super().__init__()
        kss = [ks for ks in kss if ks < seq_len]
        convs = nn.ModuleList()
        for i in range(n_kernels):
            ks = np.random.choice(kss)

            dilation = 2**np.random.uniform(0, np.log2((seq_len - 1) // (ks - 1)))  #Dilation from original paper
            # dilation = np.random.uniform(0, ((seq_len - 1) // (ks - 1)))  #Experiment with a different dilation distribution

            padding = int((ks - 1) * dilation // 2) if np.random.randint(2) == 1 else 0  #Padding from original paper
            # padding = 0         #Experiment with no padding

            weight = torch.normal(0, 1, (1, c_in, ks))
            weight -= weight.mean()
            bias = 2 * (torch.rand(1) - .5)  #bias uniform in [-1,1]

            layer = nn.Conv1d(c_in, 1, ks, padding=2 * padding, dilation=int(dilation), bias=True)
            layer.weight = torch.nn.Parameter(weight, requires_grad=False)
            layer.bias = torch.nn.Parameter(bias, requires_grad=False)
            convs.append(layer)
        self.convs = convs
        self.n_kernels = n_kernels
        self.kss = kss

        # Precalculate constants used in forward()
        self.negInf = torch.tensor(float('-inf')).cuda()
        self.defaultppv = 0.0            #Used for ppv when sample is too short to generate any output. Can try .5.

    def forward(self, x): #Modified for Macaque calls. Input batch is padded with nan.
        output = torch.empty((x.shape[0],2*self.n_kernels), device='cuda') #Pre-allocate output to evade two CUDA bugs.

        for i,cv in enumerate(self.convs):
            self.defaultmax = 0             #Used for ppv when sample is too short to generate any output.
            # Can try cv.bias.data[0] here, the value that conv1d would return on a zero input sample.

            try:
                out = cv(x)
            except RuntimeError as err:
                # print(sys.exc_info()[0], err)
                # This Runtime error means (we hope) that the conv1d's dilation and kernel are too big
                # to operate on this short tensor.
                # Had the conv1d succeeded, all the out's would have length zero, i.e.
                # an empty goodMask below.
                # Here construct ppv and max directly to indicate there's no conv1d output. And hope they always stay the same
                # as those constructed during 'else:' below.
                _ppv = torch.full(x.shape[:2], self.defaultppv, dtype=torch.float, device='cuda') #Seems to be better
                _max = torch.full(x.shape[:2], self.defaultmax, dtype=torch.float, device='cuda')
                # _max = torch.full(x.shape[:2], 0, dtype=torch.float, device='cuda')  #Maybe better than bias???
                #need to duplicate below

            else:
                # Oguiza's original _ppv here assumes that all series have the same length.
                # _ppv = torch.gt(out, 0).sum(dim=-1).float() / out.shape[-1]

                # Our series are packed into a tensor array and padded with nan at ends.
                # Here we deduce the actual convolution length returned for each row (timeseries sample).
                # conv1d, with no dilation, outputs -inf when if hits a nan.
                # Perversely, when a dilation is specified, it outputs nan when it hits a nan.
                # We have to handle both cases.
                # Amazingly, torch.isfinite(), detects both.

                goodMask = torch.isfinite(out)          #The values returned by conv1d.
                nGood = goodMask.sum(dim=-1)            #Number of usable values in each timeseries of the batch

                # Set the undefined values to -inf and use tensor max.
                out[~goodMask] = self.negInf
                _max = out.max(dim=-1).values #max of each timeseries
                # When there are no good values, max is -inf. In this case, set the max to zero or to the conv bias.
                _max[nGood == 0] = self.defaultmax  #was 0.0. Using bias (which would be the max of a constant series) improves accuracy.

                # Get the positive fraction using some arithmetic tricks.
                # Some of the conv1d outputs are ALL -inf or nan. This creates a division by zero.
                nGood[nGood==0] = 1  #Trick to set _ppv for undefined samples without causing /0 error
                _ppv = (torch.gt(out*goodMask, 0).sum(dim=-1)).float() / nGood.float()
                _ppv[nGood==0] = self.defaultppv     #Let's see if .5 as "no value" improves accuracy. Yes.

            # Defective CUDA software throws a CUDA error erratically when using cat(), a bug that has been reported for several years.
            # The first attempt to fix eliminates the error, but wrong data is unpredictably copied into output (nan's).
            # Next attempt is to preallocate output and copy row by row. It works.
            output[:,2*i] = _max[:,0]
            output[:,2*i+1] = _ppv[:,0]

        return output

# Local copy of fastai's accuracy() to avoid dependency on fastai.
def accuracyCopy(input, targs):
    "Computes accuracy with `targs` when `input` is bs * n_classes."
    n = targs.shape[0]
    input = input.argmax(dim=-1).view(n, -1)
    targs = targs.view(n, -1)
    return (input == targs).float().mean()
