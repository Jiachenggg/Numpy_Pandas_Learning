import numpy as np

a = np.arange(4)
print(a)

b = a
c = a
d = b

a[0] = 11
print(a,b,c,d)
print(b is a)
d[1:3] = [22,33]
print(a,b,c,d)

b = a.copy()  # deep copy
a[3] = 44
print(a,b)
