import torch

x = torch.arange(4.0)

x.requires_grad_(True)  # 等价于 x = torch.arange(4.0, requires_grad = True)
x.grad

y = 2 * torch.dot(x, x)

y.backward()
x.grad

x.grad.zero_()  # 梯度清0
y = x.sum()
y.backward()
x.grad

x.grad.zero_()
y = x * x
u = y.detach()  # 把u定义为与y相同值的常数
z = u * x

z.sum().backward()
x.grad == u