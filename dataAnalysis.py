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
    a = np.loadtxt('result.txt')
    length = len(a)
    x = []
    y = []
    for i in range(length):
        x.append(a[i][0])
        y.append(a[i][1])
    print x
    print y
    plt.figure()
    plt.plot(x, y, marker='.', mec='r', mfc='w')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Max Tardiness")
    plt.title("Normalized Tardiness by Total Util(m=8,alpha=4)")
    plt.show()
