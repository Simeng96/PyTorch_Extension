## SUMMARY
We implemented the High Order Convolution Module based on PyTorch and optimized its performance using PyTorch’s C++ and CUDA extension. We experimented our implementations with NVIDIA Tesla K80. Our implementation with PyTorch’s C++ extension is about 2x faster for forward and more than 10x faster for backward compared to basic Python implementation on GPU. And our implementation with PyTorch’s CUDA extension is more than 20x faster for forward and 100x faster for backward compared to basic Python implementation on GPU. 

## PROPOSAL
[Proposal](https://github.com/Simeng96/Lightweight-CNN-Framework/blob/master/proposal.pdf)

## CHECKPOINT
[Checkpoint](https://github.com/Simeng96/Lightweight-CNN-Framework/blob/master/checkpoint.pdf)

## FINAL REPORT
[Final](https://github.com/Simeng96/PyTorch_Extension/blob/master/Final%20Report.pdf)

## CODE
[python/](https://github.com/Simeng96/PyTorch_Extension/tree/master/code/python) folder contains the original high order convolution model built on PyTorch extension (nn.Module)  

[cpp/](https://github.com/Simeng96/PyTorch_Extension/tree/master/code/cpp) folder contains a python wrapper and uses c++ to implement the critical part of the high order convolution model  

[cuda/](https://github.com/Simeng96/PyTorch_Extension/tree/master/code/cuda) folder contains a python wrapper and a c++ wrapper and uses CUDA to implement the critical part of the high order convolution model  
