#f(x)=sign(wx+b)
#L(w,b)=-sum yi(w*xi+b)
#
# -*- coding: utf-8 -*-
from __future__ import division
import random
import numpy as np
import matplotlib.pyplot as plt


def sign(v):
    if v>=0:
        return 1
    else:
        return -1


def train(train_num,train_datas,lr):
    w=[0,0]
    b=0
    for i in range(train_num):
        #random choose data
        x=random.choice(train_datas)
        x1,x2,y=x
        if(y*sign(w[0]*x1+w[1]*x2 + b)<=0):
            w[0]+=lr*y*x1
            w[1]+=lr*y*x2
            b+=lr*y

    return w,b



def plot_points(train_datas,w,b):
    plt.figure()
    x1=np.linspace(0,10,50)
    x11=np.linspace(0,10)
    print x1
    #print x11
    x2=(-b-w[0]*x1)/w[1]
    print b
    print x2.shape
    print x1.shape
    plt.plot(x1,x2,color='r',label='y1 data')
    datas_len=len(train_datas)
    for i in range(datas_len):
        if (train_datas[i][-1]==1):
            plt.scatter(train_datas[i][0],train_datas[i][1],s=50)
        else:
            plt.scatter(train_datas[i][0],train_datas[i][1],marker='x',s=50)
    plt.show()



if __name__=='__main__':
    train_data1 = [[1, 3, 1], [2, 2, 1], [3, 8, 1], [2, 6, 1],[2, 8, 1]]  # +1
    train_data2 = [[2, 1, -1], [4, 1, -1], [6, 2, -1], [7, 3, -1]]  # -1
    #train_data1=[[3,3,1],[4,3,1]]
    #train_data2=[[1,1,-1]]
    train_datas=train_data1+train_data2
    w,b=train(train_num=50,train_datas=train_datas,lr=0.01)
    plot_points(train_datas,w,b)