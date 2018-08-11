import numpy as np
from sklearn.metrics import mean_squared_error

dat = np.load("msd_train.npy")
x = dat[:,1:]
x = np.c_[np.ones(x.shape[0]),x]
y = dat[:,0:1]

print(y.shape)
# terms for calculating w
left = np.matmul(x.transpose(),x)
right = np.matmul(x.transpose(),y)
# shpae ofresultant matrix
print(left.shape)
print(right.shape)

# weight matrix
w = np.matmul(np.linalg.inv(left),right)


# testing
test = np.load("msd_test.npy")
x_test = test[:,1:]
x_test = np.c_[np.ones(x_test.shape[0]),x_test]
y_test = test[:,0:1]

#NMSE
def NMSE(Yt,Y):
    minval = np.amin(Y)
    err = np.sum(np.square(Yt - Y))
    denom = np.sum(np.square(Y-minval))
    return (err/denom)

print(NMSE(np.matmul(x_test,w),y_test))

#  MSE
# mse = mean_squared_error(y_test,np.matmul(x_test,sj))
# print(nms)
# print(sj)

