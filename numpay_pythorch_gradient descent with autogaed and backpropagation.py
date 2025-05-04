import numpy as np

x=np.array([1,2,3,4],dtype=np.float32)
y=np.array([2,4,6,8],dtype=np.float32)

w =0.0

# Model prediction
def forward(x):
    return w*x

# loss = MSE
def loss(y,y_pred):
    return ((y_pred == y_pred-y)**2).mean()

# Gradient
# MSE =1/N *(w*x-y)**2
# DJ/DW=1/N * 2x (w*x-y)
def gradient(x,y,y_pred):
    return np.dot(x,y_pred-y)

print(f'Prediction before training: f(5)= {forward(5):.3f}')

learning_rate=0.1
n_iters=10

for epoch in range(n_iters):
    # prediction forward pass
    y_pred=forward(x)
    # loss
    l=loss(y,y_pred)
    # gradient
    dw=gradient(x,y,y_pred)
    # update weights
    w-=learning_rate *dw

    if epoch % 1 ==0:
        print(f'Epoch {epoch+1}: w={w:.3f}, loss={l:.3f}')

    print(f'Predictioin after training: f(5)= {forward(5):.3f}')
