import os_test

os_test.makedirs(os_test.path.join('..', 'data'), exist_ok=True)
data_file = os_test.path.join('..', 'data', 'train_result.csv')
with open(data_file, 'w') as f:
    f.write('轮次,训练损失,校验损失，校验准确率\n')
    f.write('2,NA,106000\n')
    f.write('4,NA,178100\n')
    f.write('NA,NA,140000\n')

from torch.optim.optimizer import Optimizer