import numpy as np
import pandas as pd

dates = pd.date_range('20231212', periods=6)
df = pd.DataFrame(np.arange(24).reshape((6, 4)), index=dates, columns=['A', 'B', 'C', 'D'])

df.iloc[2, 2] = 1111
df.loc['20231212', 'B'] = 2222
# df[df.A>4] = 0
df.B[df.A > 4] = 0
df['E'] = np.nan
df['F'] = pd.Series([1, 2, 3, 4, 5, 6], index=pd.date_range('20231212', periods=6))
print(df)
