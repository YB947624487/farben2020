import numpy as np
arr = [1,2,3,4,5,6]
\#求均值
arr_mean = np.mean(arr)
\#求方差
arr_var = np.var(arr)
\#求样本标准差
arr_std = np.std(arr,ddof=1)

求总体标准差

arr_std = np。std（arr，ddof=0）

print("平均值为：%f" % arr_mean)
print("方差为：%f" % arr_var)
print("标准差为:%f" % arr_std)