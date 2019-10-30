## SUMMARY
We are going to implement a Lightweight Framework for Convolutional Neural Network training and inferencing using C++ and CUDA.

### BACKGROUND
Convolutional Neural Network is a class of deep neural network used for visual or speech related tasks. A detailed explanation can be found in [http://yann.lecun.com/exdb/publis/pdf/lecun-bengio-95a.pdf](http://yann.lecun.com/exdb/publis/pdf/lecun-bengio-95a.pdf). The most tricky part of the Convolutional Neural Network is Convolution Layer. The algorithm of performing a forward calculation and backward propagation on a tensor (a high dimension matrix) is shown as follows. 

Pseudo code for forward passing (by Prof. Bhiksha Raj) 
![image](https://github.com/Simeng96/Lightweight-CNN-Framework/blob/master/image/1.png)

Pseudo code for backward propagation (by Prof. Bhiksha Raj) 
![image](https://github.com/Simeng96/Lightweight-CNN-Framework/blob/master/image/2.png)

From the above pseudo code, we can see that there exists potential of parallelism in both channel dimension and spatial dimensions. In this project, we aim to fully explore the parallel strategy to let the convolutional calculation more efficient with respect to variable tensor size, which is common in real-world Convolutional Neural Network. 

### CHALLENGE
1. The computation requirement and memory requirement vary a lot with respect to tensor size and the number of parameters. It is hard to come up with a universal strategy to accommodate for different tasks. 
2. Efficient memory handling is tricky when the amount of computation varies. We will use different levels of memory (Cache and Main Memory) when faced with different kinds of tasks. 
3. To implement a framework for CNN, we have to implement all the components which are necessary to run a model, including image preprocessing functions provided in OpenCV, data-loader and optimizer(such as SGD and Adam). If time is limited, we are going to focus more on components that are related to parallel programming and the system should not necessarily be end to end. 
4. Error handling is tricky when there are nesty memory-related or cache-related bugs in CUDA, for sometimes we cannot get the appropriate error message.

### RESOURCES
1. Andrew Machine GPU and GCP 
2. Pytorch source code (may be tricky, we should conduct experiments and play around it) 

### GOALS AND DELIVERABLES
75%: Implement a runnable CNN framework, which performs 50% as efficient as PyTorch on average(we’ll build reasonable and explainable test cases). 

100%: Achieves 75% efficiency of Pytorch on average.

125%: Outperforms Pytorch in some cases, while maintaining 75% PyTorch efficiency on average. 

### PLATFORM CHOICE
We are going to implement tensors in C++ on CPU side and the computation related to tensors in CUDA on GPU side.

### SCHEDULE
Nov Week1: PyTorch source code study 

Nov Week2: Implement CPU version of 2D Convolutional Layer; Midterm report 

Nov Week3: Implement GPU parallel version of 2D Convolutional Layer 

Nov Week4: Optimize efficiency

Dec Week1: Optimize efficiency; Final report



