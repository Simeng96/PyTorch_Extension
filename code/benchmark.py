import argparse
import math
import time

import torch

TIME_SCALES = {'s': 1, 'ms': 1000, 'us': 1000000}

parser = argparse.ArgumentParser()
parser.add_argument('language', choices=['py', 'cpp', 'cuda'])
parser.add_argument('device', choices=['cpu', 'gpu'])

options = parser.parse_args()

if options.language == 'py':
    from python.horder import HighOrder
elif options.language == 'cpp':
    from cpp.horder import HighOrder
else:
    from cuda.horder import HighOrder
    options.cuda = True

if options.device == 'cpu':
    device = torch.device("cpu")
else:
    device = torch.device("cuda")

dtype = torch.float32

kwargs = {'dtype': torch.float32,
          'device': device,
          'requires_grad': True}

# path for real data
path = "../data/img_dict.npy"
batch_size = 8
num_workers = 8
H = 224
W = 224
runs = 5
scale_name = 'ms'

# fake(random initialized data)
X = torch.randn((batch_size, 3, H, W), device=device, requires_grad=True)
model = HighOrder().to(device, dtype)

# force initialization
output = model(X)
output.sum().backward()

forward_min = math.inf
forward_time = 0
backward_min = math.inf
backward_time = 0

for _ in range(runs):
    model.zero_grad()

    start = time.time()
    output = model(X)
    elapsed = time.time() - start
    forward_min = min(forward_min, elapsed)
    forward_time += elapsed

    start = time.time()
    output.sum().backward()
    elapsed = time.time() - start
    backward_min = min(backward_min, elapsed)
    backward_time += elapsed

scale = TIME_SCALES[scale_name]
forward_min *= scale
backward_min *= scale
forward_average = forward_time / runs * scale
backward_average = backward_time / runs * scale

print('Forward: {0:.2f}/{1:.2f} {4} | Backward {2:.2f}/{3:.2f} {4}'.format(
    forward_min, forward_average, backward_min, backward_average,
    scale_name))
