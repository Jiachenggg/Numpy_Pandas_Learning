import numpy as np
import pandas as pd

dates = pd.date_range('20231212', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

print(df)
print(df['A'], df.A)
print(df[0:3], df['20231212':'20231214'])

# select by label: loc
print(df)
print(df.loc['20231214'])
print(df.loc[:, ['A', 'B']])
print(df.loc['20231214', ['A', 'B']])

# select by position: iloc
print(df)
print(df.iloc[3])
print(df.iloc[3, 1])
print(df.iloc[3:5, 1:3])
print(df.iloc[[1, 3, 5], 1:3])

# Boolean indexing
print(df)
print(df[df.A > 8])
