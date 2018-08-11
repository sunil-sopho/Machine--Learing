import numpy as np
from sklearn.metrics import mean_squared_error

dat = np.load("msd_train.npy")
x = dat[0:10,1:4]
x = np.c_[x,np.ones(x.shape[0])]
y = dat[0:2,0:1]

size = 2
num = 0
# print(x[0:size*num])
y = np.r_[x[0:size*(num-1)],x[size*num:]]
print(x)
print(y.shape)
print(y)