#Codemy Pytorch 3

import torch

my_torch2 = torch.arange(10)
#Reshape and view
my_torch2 = my_torch2.reshape(2, 5)
#Reshape if we don't know the number of items using -1
my_torch2 = torch.arange(15).reshape(3, -1)

my_torch2 = my_torch2.reshape(3, -1)
my_torch3 = torch.arange(10)
my_torch3
my_torch4 = my_torch3.view(2, 5)
my_torch5 = torch.arange(15)
print(my_torch5[7])
