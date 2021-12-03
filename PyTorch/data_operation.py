import torch

x = torch.arange(12)
x.shape
x.numel()

X = x.reshape(3, 4)

torch.zeros((2, 3, 4))
torch.ones((2, 3, 4))

torch.tensor([[1, 2, 3], [4, 5, 6], [7, 8, 9]])

Y = torch.tensor([[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]])

# 第0维合并
torch.cat((X, Y), dim=0)
torch.cat((X, Y), dim=1)

# 对张量中所有元素求和
X.sum()

# 广播机制
a = torch.arange(3).reshape((3, 1))
b = torch.arange(2).reshape((1, 2))

a + b

# 与numpy之间的转换
A = X.numpy()
B = torch.tensor(A)

# 矩阵转置
X.T

# 指定纬度求和
X_sum_axis0 = X.sum(axis=0)
X.sum(axis=[0, 1])

# 指定纬度求均值
X.mean(axis=0)

# 保持维度不变
X.sum(axis=0, keepdims=True)

# 累加求和
X.cumsum(axis=0)

# 点积
torch.dot(X, B)
torch.mv(x, X)

# L2范数
u = torch.tensor([3.0, -4.0])
torch.norm(u)

# L1范数
torch.abs(u).sum()