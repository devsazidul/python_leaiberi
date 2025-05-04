import torch

x=torch.tensor(1.0)
y=torch.tensor(2.0)

w=torch.tensor(1.0,requires_grad=True)

y_hat=w*x
less= (y_hat-y)**2
print(less)

less.backward()

print(w.grad)