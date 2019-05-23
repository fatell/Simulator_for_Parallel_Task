# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/5/23 19:49
# @Author  : weichenchen
# @Site    : 
# @File    : heavyLightRateDataAnalysis16.py
# @Software: PyCharm
import numpy as np
import matplotlib.pyplot as plt
'''
任务轻重比实验结果分析16核心
'''
if __name__ == '__main__':
    a = np.loadtxt('./data/m16HLR4.txt')
    e = np.loadtxt('./data/FSm16HLR4.txt')

    c = np.loadtxt('./data/m16HLR2.txt')
    f = np.loadtxt('./data/FSm16HLR2.txt')
    length1 = len(a)
    ax1 = []
    ay1 = []
    ay2 = []
    ay3 = []
    ay4 = []

    cx1 = []
    cy1 = []
    cy2 = []
    cy3 = []
    cy4 = []

    ex1 = []
    ey1 = []
    ey2 = []
    ey3 = []
    ey4 = []
    fx1 = []
    fy1 = []
    fy2 = []
    fy3 = []
    fy4 = []
    for i in range(length1):
        ax1.append(a[i][0])

        cx1.append(c[i][0])

        ex1.append(e[i][0])
        fx1.append(f[i][0])
        ay1.append(a[i][1])
        ay2.append(a[i][2])
        ay3.append(a[i][3])
        ay4.append(a[i][4])

        cy1.append(c[i][1])
        cy2.append(c[i][2])
        cy3.append(c[i][3])
        cy4.append(c[i][4])

        ey1.append(e[i][1])
        ey2.append(e[i][2])
        ey3.append(e[i][3])
        ey4.append(e[i][4])
        fy1.append(f[i][1])
        fy2.append(f[i][2])
        fy3.append(f[i][3])
        fy4.append(f[i][4])


    plt.figure(figsize=(16, 12))
    plt.subplot(221)
    plt.plot(ax1, ay1, marker='*', ms=10, label='GEDF')
    plt.plot(ex1, ey1, marker='<', ms=10, label='FS')
    # plt.plot(bx1, by1, marker='o', ms=10, label='alpha=3')
    # plt.plot(cx1, cy1, marker='>', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Tardiness")
    plt.title("Normalized Tardiness by Total Util(m=16,heavy_rate=0.25)")
    plt.grid(True)
    plt.legend()
    plt.subplot(222)
    plt.plot(ax1, ay2, marker='*', ms=10, label='GEDF')
    plt.plot(ex1, ey2, marker='<', ms=10, label='FS')
    # plt.plot(bx1, by2, marker='o', ms=10, label='alpha=3')
    # plt.plot(cx1, cy2, marker='<', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Tardiness")
    plt.title("Normalized Tardiness by Total Util(m=16,heavy_rate=0.25)")
    plt.grid(True)
    plt.legend()
    plt.subplot(223)
    plt.plot(ax1, ay3, marker='*', ms=10, label='GEDF')
    plt.plot(ex1, ey3, marker='<', ms=10, label='FS')
    # plt.plot(bx1, by3, marker='o', ms=10, label='alpha=3')
    # plt.plot(cx1, cy3, marker='^', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Response Time")
    plt.title("Normalized Response Time by Total Util(m=16,heavy_rate=0.25)")
    plt.grid(True)
    plt.legend()
    plt.subplot(224)
    plt.plot(ax1, ay4, marker='*', ms=10, label='GEDF')
    plt.plot(ex1, ey4, marker='<', ms=10, label='FS')
    # plt.plot(bx1, by4, marker='o', ms=10, label='alpha=3')
    # plt.plot(cx1, cy4, marker='v', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Response Time")
    plt.title("Normalized Response Time by Total Util(m=16,heavy_rate=0.25)")
    plt.grid(True)
    plt.legend()

    # plt.show()
    plt.savefig("/Users/weichenchen/Desktop/实时系统/实验结果/m16heavy4.png", format="PNG")
    plt.show()


    plt.figure(figsize=(16, 12))
    plt.subplot(221)
    # plt.plot(ax1, ay1, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by1, marker='o', ms=10, label='alpha=3')
    plt.plot(ax1, ay1, marker='*', ms=10, label='GEDF')
    plt.plot(fx1, fy1, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Tardiness")
    plt.title("Normalized Tardiness by Total Util(m=16,heavy_rate=0.5)")
    plt.grid(True)
    plt.legend()
    plt.subplot(222)
    # plt.plot(ax1, ay2, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by2, marker='o', ms=10, label='alpha=3')
    plt.plot(cx1, cy2, marker='<', ms=10, label='GEDF')
    plt.plot(fx1, fy2, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Tardiness")
    plt.title("Normalized Tardiness by Total Util(m=16,heavy_rate=0.5)")
    plt.grid(True)
    plt.legend()
    plt.subplot(223)
    # plt.plot(ax1, ay3, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by3, marker='o', ms=10, label='alpha=3')
    plt.plot(cx1, cy3, marker='^', ms=10, label='GEDF')
    plt.plot(fx1, fy3, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Response Time")
    plt.title("Normalized Response Time by Total Util(m=16,heavy_rate=0.5)")
    plt.grid(True)
    plt.legend()
    plt.subplot(224)
    # plt.plot(ax1, ay4, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by4, marker='o', ms=10, label='alpha=3')
    plt.plot(cx1, cy4, marker='v', ms=10, label='GEDF')
    plt.plot(fx1, fy4, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Response Time")
    plt.title("Normalized Response Time by Total Util(m=16,heavy_rate=0.5)")
    plt.grid(True)
    plt.legend()

    # plt.show()
    plt.savefig("/Users/weichenchen/Desktop/实时系统/实验结果/m16heavy2.png", format="PNG")
    plt.show()


