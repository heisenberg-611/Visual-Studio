import torch
import numpy as np

tensor_4d = torch.rand(2, 3, 4, 5)
print(tensor_4d)

np = np.random.rand(2, 3, 4, 5)

##create tensor out of numpy array
my_tensor = torch.tensor(np)
print(my_tensor.shape)