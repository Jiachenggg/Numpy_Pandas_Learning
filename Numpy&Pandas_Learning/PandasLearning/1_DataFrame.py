import numpy as np
import pandas as pd

s = pd.Series([1, 2, 3, np.nan, 55, 66])
print(s)

dates = pd.date_range('20231212', periods=7)
print(dates)

#  np.random.randn(7, 4)返回了一个满足标准正态分布的随机数数组，其中的每个元素都是从均值为 0、标准差为 1 的正态分布中随机采样得到的
df = pd.DataFrame(np.random.randn(7, 4), index=dates, columns=['a', 'b', 'c', 'd'])
print(df)

df1 = pd.DataFrame(np.arange(12).reshape((3, 4)))
print(df1)

df2 = pd.DataFrame({'A': 1.,
                    'B': pd.Timestamp('20231212'),
                    'C': pd.Series(1, index=list(range(4)), dtype='float32'),
                    'D': np.array([3] * 4, dtype='int32'),
                    'E': pd.Categorical(["test", "train", "test", "train"]),
                    'F': 'foo'})
print(df2)
print(df2.dtypes)
print(df2.columns)
print(df2.values)

print(df2.describe())

print(df2.T)

print(df2.sort_index(axis=1, ascending=False))
print(df2.sort_index(axis=0, ascending=False))

print(df2.sort_values(by='E'))
