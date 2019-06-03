# !/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/6/3 16:51
# @Author  : weichenchen
# @Site    : 
# @File    : timeOfTaskGenerationAnalysis.py
# @Software: PyCharm
import time
from taskSetsGenerator import *
U = 16
if __name__ == '__main__':
    start0 = time.time()
    tasksets0 = tasksets_generator(U)# 参数：总利用率
    end0 = time.time()
    print (end0 - start0),
    start1 = time.time()
    tasksets1 = tasksets_generator1(U, 16)  # 参数： 总利用率  核心数
    end1 = time.time()
    print (end1 - start1),
    start2 = time.time()
    tasksets2 = tasksets_generator2(U, 4)  # 参数：总利用率  alpha
    end2 = time.time()
    print (end2 - start2)


