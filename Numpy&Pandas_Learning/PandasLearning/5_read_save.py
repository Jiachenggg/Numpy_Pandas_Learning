import pandas as pd

# read from
data = pd.read_csv('student.csv')
print(data)

# save to
data.to_pickle('student.pickle')
