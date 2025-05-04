# pytorch ===== tesonr basics learing.

import torch

print("Pytorch version: ",torch.__version__)
x=torch.empty(3,2,2,6)
print("empty tesonr: ",x)

y=torch.rand(3,2,2,4)
print("Random tensor:",y)

z=torch.zeros(2,3)
print("Zero tesonr:",z)

a=torch.ones(5,4)
print("Ones tesonr:",a)

b=torch.rand(4,4)
print(b)
c=b.view(- 1,8)
print("Reshape tensor:",c.size())