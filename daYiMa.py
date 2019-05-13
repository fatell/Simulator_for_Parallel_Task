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
    x = [1, 2, 3, 4, 5 ,6 ,7, 8, 9, 10, 11, 12, 13, 14]
    x_label = [1904, 1903, 1902, 1901, 1812, 1811, 1810, 1809, 1808, 1807, 1806, 1805, 1804, 1803]
    y = [16, 13, 9, 11, 11, 0, 24, 23, 25, 25, 14, 13, 15, 9]
    x_label.reverse()
    y.reverse()

    plt.figure()
    plt.plot(x, y, marker='*', ms=10)
    plt.xticks(x, x_label, rotation=45)
    plt.xlabel('Month')
    plt.ylabel("Date")
    plt.title("Menstrual date trend")
    plt.grid(True)
    plt.savefig("/Users/weichenchen/Desktop/实时系统/实验结果/老婆大姨妈趋势图.png", format="PNG")
    plt.show()



