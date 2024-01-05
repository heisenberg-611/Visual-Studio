import torch
import numpy as np

a = torch.ones(5)
print(a)
b = a.numpy()
print(type(b))

a.add_(2)
print(a)
print(b)