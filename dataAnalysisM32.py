# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/9 16:58
# @Author  : weichenchen
# @Site    : 
# @File    : dataAnalysisM32.py
# @Software: PyCharm

import numpy as np
import matplotlib.pyplot as plt
'''
用来数据分析画图
'''
if __name__ == '__main__':
    a = np.loadtxt('./data/m32alpha4.txt')
    b = np.loadtxt('./data/m32alpha3.txt')
    c = np.loadtxt('./data/m32alpha2.txt')
    length1 = len(a)
    length2 = len(b)
    length3 = len(c)
    ax1 = []
    ay1 = []
    ay2 = []
    ay3 = []
    ay4 = []
    bx1 = []
    by1 = []
    by2 = []
    by3 = []
    by4 = []
    cx1 = []
    cy1 = []
    cy2 = []
    cy3 = []
    cy4 = []
    for i in range(length1):
        ax1.append(a[i][0])
        bx1.append(b[i][0])
        cx1.append(c[i][0])
        ay1.append(a[i][1])
        ay2.append(a[i][2])
        ay3.append(a[i][3])
        ay4.append(a[i][4])
        by1.append(b[i][1])
        by2.append(b[i][2])
        by3.append(b[i][3])
        by4.append(b[i][4])
        cy1.append(c[i][1])
        cy2.append(c[i][2])
        cy3.append(c[i][3])
        cy4.append(c[i][4])

    # print x1
    # print y1

    # x2 = []
    # y2 = []
    # for i in range(length2):
    #     x2.append(b[i][0])
    #     y2.append(b[i][1])
    # print x2
    # print y2

    plt.figure(figsize=(16, 12))
    plt.subplot(221)
    plt.plot(ax1, ay1, marker='*', ms=10, label='alpha=4')
    plt.plot(bx1, by1, marker='o', ms=10, label='alpha=3')
    plt.plot(cx1, cy1, marker='>', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Tardiness")
    plt.title("Normalized Tardiness by Total Util(m=32,alpha=4)")
    plt.grid(True)
    plt.legend()
    plt.subplot(222)
    plt.plot(ax1, ay2, marker='*', ms=10, label='alpha=4')
    plt.plot(bx1, by2, marker='o', ms=10, label='alpha=3')
    plt.plot(cx1, cy2, marker='<', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Tardiness")
    plt.title("Normalized Tardiness by Total Util(m=32,alpha=4)")
    plt.grid(True)
    plt.legend()
    plt.subplot(223)
    plt.plot(ax1, ay3, marker='*', ms=10, label='alpha=4')
    plt.plot(bx1, by3, marker='o', ms=10, label='alpha=3')
    plt.plot(cx1, cy3, marker='^', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Response Time")
    plt.title("Normalized Response Time by Total Util(m=32,alpha=4)")
    plt.grid(True)
    plt.legend()
    plt.subplot(224)
    plt.plot(ax1, ay4, marker='*', ms=10, label='alpha=4')
    plt.plot(bx1, by4, marker='o', ms=10, label='alpha=3')
    plt.plot(cx1, cy4, marker='v', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Response Time")
    plt.title("Normalized Response Time by Total Util(m=32,alpha=4)")
    plt.grid(True)
    plt.legend()

    # plt.show()
    plt.savefig("/Users/weichenchen/Desktop/实时系统/实验结果/m32.png", format="PNG")
    plt.show()


