#基础
import numpy as np
# print("numpy版本",np.__version__)

# test_array = np.array([1,2,3])
# print(f"测试数组：{test_array}")

#一维数组
arr1 = np.array([1,2,3,4,5])
print("一维数组：",arr1)
print("类型",type(arr1))
print("维度",arr1.ndim)
print("形状:",arr1.shape)

#二维数组
arr2 = np.array([[1,2,3],[4,5,6]])
print("二维数组：",arr2)
print("维度：",arr2.ndim)
print("形状:",arr2.shape)

#指定数据类型
arr3 = np.array([1.1, 2.2, 3.3], dtype=np.float32)
print("\n指定类型的数组：", arr3)
print("数据类型：", arr3.dtype)  # float32

##快速创建：全0/全1数组
#1.np.zeros():创建0数组
zeros_1d = np.zeros(5)
print("\n一维全0数组：",zeros_1d)

zeros_2d = np.zeros((3,4),dtype=int)
print("二维全0数组：\n",zeros_2d)

#2. np_ones():创建全1数组