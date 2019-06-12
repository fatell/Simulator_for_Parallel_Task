# Simulator for DAG Parallel Task
## 任务模型和仿真器实现
- 采用DAG并行任务模型，实现了一个DAG并行任务调度算法仿真器
- 目前实现了GEDF，GEDF_modify，FS调度算法
- 调度模块可扩展，只需在scheduler.py模块里添加新的调度算法实现即可
## 主要模块说明
- parallerTask.py: 并行任务类
- job.py: 作业类
- nodeInJob.py: 作业中子节点类
- scheduler.py: 调度模块，具体的调度算法都在这个模块实现
- taskSetsGenerator.py: 任务集生成模块，不同的任务集生成方式都在这里实现
- testxxxx.py: 一些测试类
- taskSetsAnalysis.py: 任务集静态属性分析（小提琴图）
- xxxxAnalysis16/32.py: 各种实验结果分析（16核心和32核心）

## 分支说明
- master分支：主分支，生成的任务周期会调整成和谐周期，即2的幂次方
- Period_not_harmonious分支：该分支生成的任务周期不做调整  
