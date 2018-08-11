import numpy as np
from sklearn.metrics import mean_squared_error

dat = np.load("msd_train.npy")
x_train = dat[:,1:]
x_train = np.c_[x_train,np.ones(x.shape[0])]
y_test = dat[:,0:1]

lamda = 0.00000000001
print(y.shape)


# shpae ofresultant matrix
print(left.shape)
print(right.shape)
# calculate w
def w(x,y,lamda):
	# terms for calculating w
	left = (np.matmul(x.transpose(),x) * 1/x.shape[0]) + lamda*np.identity(x.shape[1])
	right = np.matmul(x.transpose()*1/x.shape[0],y)


# 10 - fold cross validation
def cross(inp,out,lam,num):
	size = inp.shape[0]/10;
	# inp1 = inp[size*num,size*(num+10)];
	inp1 = np.r_[inp[0:size*(num-1)],inp[size*num:]]


# weight matrix
w = np.matmul(np.linalg.inv(left),right)

test = np.load("msd_test.npy")
x_test = test[:,1:]
x_test = np.c_[x_test,np.ones(x_test.shape[0])]
y_test = test[:,0:1]


def MSE(Yt,Y):
    minval = np.amin(Y)
    err = np.sum(np.square(Yt - Y))
    denom = np.sum(np.square(Y-minval))
    return (err/denom)

print(MSE(np.matmul(x_test,w),y_test))
nms = mean_squared_error(y_test,np.matmul(x_test,w))
print(nms)