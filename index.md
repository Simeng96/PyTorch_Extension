## SUMMARY
We are going to implement a basic module (such as  LSTM) based on PyTorch and optimize its performance using PyTorch’s C++ and CUDA extension. 

## PROPOSAL
[Proposal](https://github.com/Simeng96/Lightweight-CNN-Framework/blob/master/proposal.pdf)

## CHECKPOINT
[Checkpoint](https://github.com/Simeng96/Lightweight-CNN-Framework/blob/master/checkpoint.pdf)

## CODE
[python/](https://github.com/Simeng96/PyTorch_Extension/tree/master/code/python) folder contains the original high order convolution model built on PyTorch extension (nn.Module)  

[cpp/](https://github.com/Simeng96/PyTorch_Extension/tree/master/code/cpp) folder contains a python wrapper and uses c++ to implement the critical part of the high order convolution model  

[cuda/](https://github.com/Simeng96/PyTorch_Extension/tree/master/code/cuda) folder contains a python wrapper and a c++ wrapper and uses CUDA to implement the critical part of the high order convolution model  
