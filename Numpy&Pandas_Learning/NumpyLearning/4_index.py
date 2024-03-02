import numpy as np

A = np.arange(3, 15)
print(A)
print(A[2])

A = np.arange(3, 15).reshape(3, 4)
print(A)
print(A[2])
print(A[1][1])
# print(A[1,1])
print(A[2,:])
print(A[:,1])
print(A[1,1:3])

print(A)
for row in A:
    print(row)
for column in A.T:  # np.transpose(A)
    print(column)

print(A)
print(A.flatten())
for item in A.flat:
    print(item)
