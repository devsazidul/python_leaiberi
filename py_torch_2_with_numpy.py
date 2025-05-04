import torch
import numpy as np

# Create a random tensor and convart it to a numpy array
# tensor to numpy
a=torch.ones(5)
print("a tensor:",a)
b=a.numpy()
print("b numpy array:",b)


# Create a numpy array and convart it to a tensor
# numpy to tensor
c=np.ones(5)
print("C numpy array:",c)
d=torch.from_numpy(c)
print("d tensor:",d)

# Create a random tensor and convart it to a numpy array
x=torch.ones(5,requires_grad=True)
print("X tensor:",x)