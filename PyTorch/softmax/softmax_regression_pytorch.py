import torch
from torch import nn
from d2l import torch as d2l
import matplotlib.pyplot as plt
import os

os.environ["KMP_DUPLICATE_LIB_OK"] = "TRUE"

if __name__ == '__main__':
    batch_size = 256
    train_iter, test_iter = d2l.load_data_fashion_mnist(batch_size)

    # pytorch不会隐式地调整输入形状
    # 因此，我们定义展平层（flatten）在线性层前调整网络输入的形状
    net = nn.Sequential(nn.Flatten(), nn.Linear(784, 10))

    def init_weights(m):
        if type(m) == nn.Linear:
            nn.init.normal_(m.weight, std=0.01)

    net.apply(init_weights)

    # 在交叉熵损失函数中传递未归一化的预测，并同时计算softmax及其对数
    loss = nn.CrossEntropyLoss()

    # 使用学习率为0.1的SGD作为优化算法
    trainer = torch.optim.SGD(net.parameters(), lr=0.1)

    num_epochs = 10
    d2l.train_ch3(net, train_iter, test_iter, loss, num_epochs, trainer)