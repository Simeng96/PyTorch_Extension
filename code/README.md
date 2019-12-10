# Commands  

1. To run Python extension  
python benchmark.py py cpu  
python benchmark.py py gpu  

2. To compile and run C++ extension:  
cd cpp/  
python setup.py install  
cd ..  
python benchmark.py cpp cpu  
python benchmark.py cpp gpu  

3. To compile and run CUDA extension:  
cd cuda/  
python setup.py install  
cd ..  
python benchmark.py cuda cpu  
python benchmark.py cuda gpu  

4. To run all of the experiments  
./run.sh  

5. To check the correctness of C++ and CUDA extension, we use Python extension as ground truth (note that we implement Python extension using PyTorch's nn.module, which only requires the implementation of forward pass and the backprop is implemented automatically):  
python check.py  
