# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/2 17:04
# @Author  : weichenchen
# @Site    : 
# @File    : dataAnalysis.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
'''
用来数据分析画图
'''
if __name__ == '__main__':
    a = np.loadtxt('m8alpha4.txt')
    b = np.loadtxt('m8alpha2.txt')
    length1 = len(a)
    length2 = len(b)
    x1 = []
    y1 = []
    for i in range(length1):
        x1.append(a[i][0])
        y1.append(a[i][1])
    print x1
    print y1

    x2 = []
    y2 = []
    for i in range(length2):
        x2.append(b[i][0])
        y2.append(b[i][1])
    print x2
    print y2

    plt.figure()
    plt.plot(x1, y1, marker='.', mec='r', mfc='w',label='alpha=4')
    plt.plot(x2, y2, marker='*', ms=10,label='alpha=2')
    plt.legend()
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Tardiness")
    plt.title("Normalized Tardiness by Total Util(m=8)")
    # plt.show()
    plt.savefig("/Users/weichenchen/Desktop/实时系统/实验结果/m8.png", format="PNG")
    plt.show()


