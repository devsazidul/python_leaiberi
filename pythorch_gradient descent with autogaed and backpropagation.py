import torch

# Data
x = torch.tensor([1, 2, 3, 4], dtype=torch.float32)
y = torch.tensor([2, 4, 6, 8], dtype=torch.float32)

# Initialize weight
w = torch.tensor(0.0, dtype=torch.float32, requires_grad=True)

# Model prediction
def forward(x):
    return w * x

# MSE loss function
def loss(y, y_pred):
    return ((y_pred - y) ** 2).mean()

# Gradient
# MSE = 1/N * (w*x - y)^2
# dL/dw = 1/N * 2x (w*x - y)
def gradient(x, y, y_pred):
    return torch.dot(x, y_pred - y)

print(f'Prediction before training: f(5)= {forward(torch.tensor(5.0)): .3f}')

learning_rate = 0.1
n_iters = 10

for epoch in range(n_iters):
    # prediction forward pass
    y_pred = forward(x)
    
    # loss calculation
    l = loss(y, y_pred)
    
    # gradient calculation
    l.backward()
    
    # update weight
    with torch.no_grad():
        w -= learning_rate * w.grad
    
    # zero the gradients after updating weights
    w.grad.zero_()

    if epoch % 1 == 0:
        print(f'Epoch {epoch + 1}: w={w.item():.3f}, loss={l.item():.3f}')

print(f'Prediction after training: f(5)= {forward(torch.tensor(5.0)): .3f}')
