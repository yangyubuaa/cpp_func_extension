import torch
from test import Test

if __name__=="__main__":
    x = torch.Tensor([1,2,3])
    y = torch.Tensor([4,5,6])
    x.requires_grad=True
    y.requires_grad=True
    test = Test()
    z = test(x, y)
    z.sum().backward()
    print('x: ', x)
    print('y: ', y)
    print('z: ', z)
    print('x.grad: ', x.grad)
    print('y.grad: ', y.grad)