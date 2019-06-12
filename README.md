# GEDF_for_Parallel
## 任务模型和仿真器实现
- 采用DAG并行任务模型，实现了一个DAG并行任务调度算法仿真器
- 目前实现了GEDF，GEDF_modify，FS调度算法
- 调度模块可扩展，只需在scheduler.py模块里添加新的调度算法实现即可
## 主要模块说明
- 主要模块类:
  -- parallerTask.py:并行任务类
  
