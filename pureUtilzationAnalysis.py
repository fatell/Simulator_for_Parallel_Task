# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 15:27
# @Author  : weichenchen
# @Site    : 
# @File    : pureUtilzationAnalysis.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt

'''
用来数据分析画图
'''

if __name__ == '__main__':
    a = np.loadtxt('./data/m16alpha2.txt')
    b = np.loadtxt('./data/FSm16alpha2.txt')
    c = np.loadtxt('./data/m32alpha2.txt')
    d = np.loadtxt('./data/FSm32alpha2.txt')

    length1 = len(a)
    length2 = len(c)
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
    dx1 = []
    dy1 = []
    dy2 = []
    dy3 = []
    dy4 = []

    for i in range(length1):
        ax1.append(a[i][0])
        bx1.append(b[i][0])

        ay1.append(a[i][1])
        ay2.append(a[i][2])
        ay3.append(a[i][3])
        ay4.append(a[i][4])
        by1.append(b[i][1])
        by2.append(b[i][2])
        by3.append(b[i][3])
        by4.append(b[i][4])
    for j in range(length2):
        cx1.append(c[j][0])
        dx1.append(d[j][0])

        cy1.append(c[j][1])
        cy2.append(c[j][2])
        cy3.append(c[j][3])
        cy4.append(c[j][4])
        dy1.append(d[j][1])
        dy2.append(d[j][2])
        dy3.append(d[j][3])
        dy4.append(d[j][4])

    plt.figure(figsize=(16, 12))
    plt.rcParams['font.sans-serif'] = ['Arial Unicode MS']
    plt.subplot(221)
    plt.plot(ax1, ay1, marker='*', ms=10, label='GEDF')
    plt.plot(bx1, by1, marker='<', ms=10, label='FS')
    # plt.plot(bx1, by1, marker='o', ms=10, label='alpha=3')
    # plt.plot(cx1, cy1, marker='>', ms=10, label='alpha=2')
    plt.xlabel(u"系统总利用率", fontsize=22)
    plt.ylabel(u"平均归一化最大延迟度", fontsize=22)
    plt.title(u"归一化延迟度", fontsize=22)

    plt.grid(True)
    plt.legend()
    plt.subplot(222)
    plt.plot(ax1, ay2, marker='*', ms=10, label='GEDF')
    plt.plot(bx1, by2, marker='<', ms=10, label='FS')

    plt.xlabel(u"系统总利用率", fontsize=22)
    plt.ylabel(u"平均归一化平均延迟度", fontsize=22)
    plt.title(u"归一化延迟度", fontsize=22)

    plt.grid(True)
    plt.legend()
    plt.subplot(223)
    plt.plot(ax1, ay3, marker='*', ms=10, label='GEDF')
    plt.plot(bx1, by3, marker='<', ms=10, label='FS')

    plt.xlabel(u"系统总利用率", fontsize=22)
    plt.ylabel(u"平均归一化最大响应时间", fontsize=22)
    plt.title(u"归一化响应时间", fontsize=22)

    plt.grid(True)
    plt.legend()
    plt.subplot(224)
    plt.plot(ax1, ay4, marker='*', ms=10, label='GEDF')
    plt.plot(bx1, by4, marker='<', ms=10, label='FS')
    # plt.plot(bx1, by4, marker='o', ms=10, label='alpha=3')
    # plt.plot(cx1, cy4, marker='v', ms=10, label='alpha=2')
    plt.xlabel(u"系统总利用率", fontsize=22)
    plt.ylabel(u"平均归一化平均响应时间", fontsize=22)
    plt.title(u"归一化响应时间", fontsize=22)
    # plt.xlabel("Total Utilization (Base)")
    # plt.ylabel("Avg. of Normalized Average Response Time")
    # plt.title("Normalized Response Time")
    plt.grid(True)
    plt.legend()
    # plt.suptitle(u"任务集调度分析（隐式截止期限，16核心，alpha=4）", fontsize=22)
    # plt.suptitle("task sets scheduling analysis (implicit-deadline, 16 processors, alpha=4)", fontsize=22)
    # plt.show()
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    plt.savefig("/Users/weichenchen/Desktop/实时系统/实验结果/NEWm16.png", format="PNG")
    plt.show()

    plt.figure(figsize=(16, 12))
    plt.subplot(221)
    # plt.plot(ax1, ay1, marker='*', ms=10, label='alpha=4')
    plt.plot(cx1, cy1, marker='o', ms=10, label='GEDF')
    plt.plot(dx1, dy1, marker='*', ms=10, label='FS')
    # plt.plot(cx1, cy1, marker='>', ms=10, label='alpha=2')
    plt.xlabel(u"系统总利用率", fontsize=18)
    plt.ylabel(u"平均归一化最大延迟度", fontsize=18)
    plt.title(u"归一化延迟度", fontsize=18)
    # plt.xlabel("Total Utilization (Base)")
    # plt.ylabel("Avg. of Normalized Max Tardiness")
    # plt.title("Normalized Tardiness")
    plt.grid(True)
    plt.legend()
    plt.subplot(222)
    # plt.plot(ax1, ay2, marker='*', ms=10, label='alpha=4')
    plt.plot(cx1, cy2, marker='o', ms=10, label='GEDF')
    plt.plot(dx1, dy2, marker='*', ms=10, label='FS')
    # plt.plot(cx1, cy2, marker='<', ms=10, label='alpha=2')
    plt.xlabel(u"系统总利用率", fontsize=18)
    plt.ylabel(u"平均归一化平均延迟度", fontsize=18)
    plt.title(u"归一化延迟度", fontsize=18)
    # plt.xlabel("Total Utilization (Base)")
    # plt.ylabel("Avg. of Normalized Average Tardiness")
    # plt.title("Normalized Tardiness")
    plt.grid(True)
    plt.legend()
    plt.subplot(223)
    # plt.plot(ax1, ay3, marker='*', ms=10, label='alpha=4')
    plt.plot(cx1, cy3, marker='o', ms=10, label='GEDF')
    plt.plot(dx1, dy3, marker='*', ms=10, label='FS')
    # plt.plot(cx1, cy3, marker='^', ms=10, label='alpha=2')
    plt.xlabel(u"系统总利用率", fontsize=18)
    plt.ylabel(u"平均归一化最大响应时间", fontsize=18)
    plt.title(u"归一化响应时间", fontsize=18)
    # plt.xlabel("Total Utilization (Base)")
    # plt.ylabel("Avg. of Normalized Max Response Time")
    # plt.title("Normalized Response Time")
    plt.grid(True)
    plt.legend()
    plt.subplot(224)
    # plt.plot(ax1, ay4, marker='*', ms=10, label='alpha=4')
    plt.plot(cx1, cy4, marker='o', ms=10, label='GEDF')
    plt.plot(dx1, dy4, marker='*', ms=10, label='FS')
    # plt.plot(cx1, cy4, marker='v', ms=10, label='alpha=2')
    plt.xlabel(u"系统总利用率", fontsize=18)
    plt.ylabel(u"平均归一化平均响应时间", fontsize=18)
    plt.title(u"归一化响应时间", fontsize=18)
    # plt.xlabel("Total Utilization (Base)")
    # plt.ylabel("Avg. of Normalized Average Response Time")
    # plt.title("Normalized Response Time")
    plt.grid(True)
    plt.legend()
    # plt.suptitle(u"任务集调度分析（隐式截止期限，16核心，alpha=3）", fontsize=22)
    # plt.suptitle("task sets scheduling analysis (implicit-deadline, 16 processors, alpha=3)", fontsize=22)
    # plt.show()
    plt.subplots_adjust(wspace=0.3, hspace=0.3)
    plt.savefig("/Users/weichenchen/Desktop/实时系统/实验结果/NEWm32.png", format="PNG")
    plt.show()
