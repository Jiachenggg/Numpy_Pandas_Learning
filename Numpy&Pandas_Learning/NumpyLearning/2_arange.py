import numpy as np

a = np.array([[1,2,3],
                     [4,5,6]], dtype=int)
print(a.dtype)

a = np.zeros((3,4), dtype=int)
print(a)

a = np.ones((3,4), dtype=int)
print(a)

a = np.empty((3,4), dtype=int)
print(a)

a = np.arange(10, 20, 2)
print(a)

a = np.arange(12).reshape(3,4)
print(a)

a = np.linspace(1, 10, 6).reshape(2, 3)
print(a)
