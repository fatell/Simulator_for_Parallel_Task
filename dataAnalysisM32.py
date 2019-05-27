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
    a = np.loadtxt('./data/5-26/Gm32alpha4.txt')
    j = np.loadtxt('./data/5-26/GMm32alpha4.txt')
    e = np.loadtxt('./data/5-26/FSm32alpha4.txt')
    b = np.loadtxt('./data/5-26/Gm32alpha3.txt')
    k = np.loadtxt('./data/5-26/GMm32alpha3.txt')
    d = np.loadtxt('./data/5-26/FSm32alpha3.txt')
    c = np.loadtxt('./data/5-26/Gm32alpha2.txt')
    l = np.loadtxt('./data/5-26/GMm32alpha2.txt')
    f = np.loadtxt('./data/5-26/FSm32alpha2.txt')
    g = np.loadtxt('./data/5-26/Gm32alpha1-5.txt')
    m = np.loadtxt('./data/5-26/GMm32alpha1-5.txt')
    h = np.loadtxt('./data/5-26/FSm32alpha1-5.txt')
    length1 = len(a)
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
    gx1, gy1, gy2, gy3, gy4 = [], [], [], [], []
    hx1, hy1, hy2, hy3, hy4 = [], [], [], [], []
    jx1, jy1, jy2, jy3, jy4 = [], [], [], [], []
    kx1, ky1, ky2, ky3, ky4 = [], [], [], [], []
    lx1, ly1, ly2, ly3, ly4 = [], [], [], [], []
    mx1, my1, my2, my3, my4 = [], [], [], [], []
    for i in range(length1):
        ax1.append(a[i][0])
        bx1.append(b[i][0])
        cx1.append(c[i][0])
        dx1.append(d[i][0])
        ex1.append(e[i][0])
        fx1.append(f[i][0])
        gx1.append(g[i][0])
        hx1.append(h[i][0])
        jx1.append(j[i][0])
        kx1.append(k[i][0])
        lx1.append(l[i][0])
        mx1.append(m[i][0])

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
        dy1.append(d[i][1])
        dy2.append(d[i][2])
        dy3.append(d[i][3])
        dy4.append(d[i][4])
        ey1.append(e[i][1])
        ey2.append(e[i][2])
        ey3.append(e[i][3])
        ey4.append(e[i][4])
        fy1.append(f[i][1])
        fy2.append(f[i][2])
        fy3.append(f[i][3])
        fy4.append(f[i][4])
        gy1.append(g[i][1])
        gy2.append(g[i][2])
        gy3.append(g[i][3])
        gy4.append(g[i][4])
        hy1.append(h[i][1])
        hy2.append(h[i][2])
        hy3.append(h[i][3])
        hy4.append(h[i][4])
        jy1.append(j[i][1])
        jy2.append(j[i][2])
        jy3.append(j[i][3])
        jy4.append(j[i][4])
        ky1.append(k[i][1])
        ky2.append(k[i][2])
        ky3.append(k[i][3])
        ky4.append(k[i][4])
        ly1.append(l[i][1])
        ly2.append(l[i][2])
        ly3.append(l[i][3])
        ly4.append(l[i][4])
        my1.append(m[i][1])
        my2.append(m[i][2])
        my3.append(m[i][3])
        my4.append(m[i][4])


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
    plt.plot(ax1, ay1, marker='*', ms=10, label='GEDF')
    plt.plot(jx1, jy1, marker='>', ms=10, label='GEDF_modify')
    plt.plot(ex1, ey1, marker='<', ms=10, label='FS')
    # plt.plot(bx1, by1, marker='o', ms=10, label='alpha=3')
    # plt.plot(cx1, cy1, marker='>', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Tardiness")
    plt.title("Normalized Tardiness")
    plt.grid(True)
    plt.legend()
    plt.subplot(222)
    plt.plot(ax1, ay2, marker='*', ms=10, label='GEDF')
    plt.plot(jx1, jy2, marker='>', ms=10, label='GEDF_modify')
    plt.plot(ex1, ey2, marker='<', ms=10, label='FS')
    # plt.plot(bx1, by2, marker='o', ms=10, label='alpha=3')
    # plt.plot(cx1, cy2, marker='<', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Tardiness")
    plt.title("Normalized Tardiness")
    plt.grid(True)
    plt.legend()
    plt.subplot(223)
    plt.plot(ax1, ay3, marker='*', ms=10, label='GEDF')
    plt.plot(jx1, jy3, marker='>', ms=10, label='GEDF_modify')
    plt.plot(ex1, ey3, marker='<', ms=10, label='FS')
    # plt.plot(bx1, by3, marker='o', ms=10, label='alpha=3')
    # plt.plot(cx1, cy3, marker='^', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Response Time")
    plt.title("Normalized Response Time")
    plt.grid(True)
    plt.legend()
    plt.subplot(224)
    plt.plot(ax1, ay4, marker='*', ms=10, label='GEDF')
    plt.plot(jx1, jy4, marker='>', ms=10, label='GEDF_modify')
    plt.plot(ex1, ey4, marker='<', ms=10, label='FS')
    # plt.plot(bx1, by4, marker='o', ms=10, label='alpha=3')
    # plt.plot(cx1, cy4, marker='v', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Response Time")
    plt.title("Normalized Response Time")
    plt.grid(True)
    plt.legend()
    plt.suptitle("task sets scheduling analysis (implicit-deadline, 32 processors, alpha=4)", fontsize=22)
    # plt.show()
    plt.savefig("/Users/weichenchen/Desktop/实时系统/实验结果/NEWm32alpha4.png", format="PNG")
    plt.show()

    plt.figure(figsize=(16, 12))
    plt.subplot(221)
    # plt.plot(ax1, ay1, marker='*', ms=10, label='alpha=4')
    plt.plot(bx1, by1, marker='o', ms=10, label='GEDF')
    plt.plot(kx1, ky1, marker='>', ms=10, label='GEDF_modify')
    plt.plot(dx1, dy1, marker='*', ms=10, label='FS')
    # plt.plot(cx1, cy1, marker='>', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Tardiness")
    plt.title("Normalized Tardiness")
    plt.grid(True)
    plt.legend()
    plt.subplot(222)
    # plt.plot(ax1, ay2, marker='*', ms=10, label='alpha=4')
    plt.plot(bx1, by2, marker='o', ms=10, label='GEDF')
    plt.plot(kx1, ky2, marker='>', ms=10, label='GEDF_modify')
    plt.plot(dx1, dy2, marker='*', ms=10, label='FS')
    # plt.plot(cx1, cy2, marker='<', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Tardiness")
    plt.title("Normalized Tardiness")
    plt.grid(True)
    plt.legend()
    plt.subplot(223)
    # plt.plot(ax1, ay3, marker='*', ms=10, label='alpha=4')
    plt.plot(bx1, by3, marker='o', ms=10, label='GEDF')
    plt.plot(kx1, ky3, marker='>', ms=10, label='GEDF_modify')
    plt.plot(dx1, dy3, marker='*', ms=10, label='FS')
    # plt.plot(cx1, cy3, marker='^', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Response Time")
    plt.title("Normalized Response Time")
    plt.grid(True)
    plt.legend()
    plt.subplot(224)
    # plt.plot(ax1, ay4, marker='*', ms=10, label='alpha=4')
    plt.plot(bx1, by4, marker='o', ms=10, label='GEDF')
    plt.plot(kx1, ky4, marker='>', ms=10, label='GEDF_modify')
    plt.plot(dx1, dy4, marker='*', ms=10, label='FS')
    # plt.plot(cx1, cy4, marker='v', ms=10, label='alpha=2')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Response Time")
    plt.title("Normalized Response Time")
    plt.grid(True)
    plt.legend()
    plt.suptitle("task sets scheduling analysis (implicit-deadline, 32 processors, alpha=3)", fontsize=22)
    # plt.show()
    plt.savefig("/Users/weichenchen/Desktop/实时系统/实验结果/NEWm32alpha3.png", format="PNG")
    plt.show()

    plt.figure(figsize=(16, 12))
    plt.subplot(221)
    # plt.plot(ax1, ay1, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by1, marker='o', ms=10, label='alpha=3')
    plt.plot(ax1, ay1, marker='*', ms=10, label='GEDF')
    plt.plot(lx1, ly1, marker='>', ms=10, label='GEDF_modify')
    plt.plot(fx1, fy1, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Tardiness")
    plt.title("Normalized Tardiness ")
    plt.grid(True)
    plt.legend()
    plt.subplot(222)
    # plt.plot(ax1, ay2, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by2, marker='o', ms=10, label='alpha=3')
    plt.plot(cx1, cy2, marker='<', ms=10, label='GEDF')
    plt.plot(lx1, ly2, marker='>', ms=10, label='GEDF_modify')
    plt.plot(fx1, fy2, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Tardiness")
    plt.title("Normalized Tardiness ")
    plt.grid(True)
    plt.legend()
    plt.subplot(223)
    # plt.plot(ax1, ay3, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by3, marker='o', ms=10, label='alpha=3')
    plt.plot(cx1, cy3, marker='^', ms=10, label='GEDF')
    plt.plot(lx1, ly3, marker='>', ms=10, label='GEDF_modify')
    plt.plot(fx1, fy3, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Response Time")
    plt.title("Normalized Response Time ")
    plt.grid(True)
    plt.legend()
    plt.subplot(224)
    # plt.plot(ax1, ay4, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by4, marker='o', ms=10, label='alpha=3')
    plt.plot(cx1, cy4, marker='v', ms=10, label='GEDF')
    plt.plot(lx1, ly4, marker='>', ms=10, label='GEDF_modify')
    plt.plot(fx1, fy4, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Response Time")
    plt.title("Normalized Response Time ")
    plt.grid(True)
    plt.legend()
    plt.suptitle("task sets scheduling analysis (implicit-deadline, 32 processors, alpha=2)", fontsize=22)
    # plt.show()
    plt.savefig("/Users/weichenchen/Desktop/实时系统/实验结果/NEWm32alpha2.png", format="PNG")
    plt.show()

    plt.figure(figsize=(16, 12))
    plt.subplot(221)
    # plt.plot(ax1, ay1, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by1, marker='o', ms=10, label='alpha=3')
    plt.plot(gx1, gy1, marker='*', ms=10, label='GEDF')
    plt.plot(mx1, my1, marker='>', ms=10, label='GEDF_modify')
    plt.plot(hx1, hy1, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Tardiness")
    plt.title("Normalized Tardiness ")
    plt.grid(True)
    plt.legend()
    plt.subplot(222)
    # plt.plot(ax1, ay2, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by2, marker='o', ms=10, label='alpha=3')
    plt.plot(gx1, gy2, marker='<', ms=10, label='GEDF')
    plt.plot(mx1, my2, marker='>', ms=10, label='GEDF_modify')
    plt.plot(hx1, hy2, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Tardiness")
    plt.title("Normalized Tardiness ")
    plt.grid(True)
    plt.legend()
    plt.subplot(223)
    # plt.plot(ax1, ay3, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by3, marker='o', ms=10, label='alpha=3')
    plt.plot(gx1, gy3, marker='^', ms=10, label='GEDF')
    plt.plot(mx1, my3, marker='>', ms=10, label='GEDF_modify')
    plt.plot(hx1, hy3, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Max Response Time")
    plt.title("Normalized Response Time ")
    plt.grid(True)
    plt.legend()
    plt.subplot(224)
    # plt.plot(ax1, ay4, marker='*', ms=10, label='alpha=4')
    # plt.plot(bx1, by4, marker='o', ms=10, label='alpha=3')
    plt.plot(gx1, gy4, marker='v', ms=10, label='GEDF')
    plt.plot(mx1, my4, marker='>', ms=10, label='GEDF_modify')
    plt.plot(hx1, hy4, marker='<', ms=10, label='FS')
    plt.xlabel("Total Utilization (Base)")
    plt.ylabel("Avg. of Normalized Average Response Time")
    plt.title("Normalized Response Time ")
    plt.grid(True)
    plt.legend()
    plt.suptitle("task sets scheduling analysis (implicit-deadline, 32 processors, alpha=1.5)", fontsize=22)
    # plt.show()
    plt.savefig("/Users/weichenchen/Desktop/实时系统/实验结果/NEWm32alpha1-5.png", format="PNG")
    plt.show()


