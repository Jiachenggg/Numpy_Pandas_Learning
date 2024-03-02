import numpy as np

A = np.array([1,1,1])
B = np.array([2,2,2])

print(np.vstack((A, B)))  # vertical stack
print(np.hstack((A, B)))  # horizontal stack

A = np.array([1,1,1])[:, np.newaxis]
B = np.array([2,2,2])[:, np.newaxis]
print(A)
print(B)

print('-----')

print(np.concatenate((A,B,B,A), axis=0))
print(np.concatenate((A,B,B,A), axis=1))

A = np.arange(12).reshape(3, 4)
print(A)
print(np.split(A, 2, axis=1))
print(np.split(A, 3, axis=0))
print(np.array_split(A, 3, axis=1))

print(np.vsplit(A, 3))  # vertical split
print(np.hsplit(A, 2))  # horizontal split
