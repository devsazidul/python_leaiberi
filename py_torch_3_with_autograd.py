import torch

x=torch.randn(3,requires_grad=True)
print("x:",x)

y=x+2
print("y:",y)

z=y*y*2
z=z.mean()
print("z:",z)

z.backward()
print("x.grad:",x.grad)