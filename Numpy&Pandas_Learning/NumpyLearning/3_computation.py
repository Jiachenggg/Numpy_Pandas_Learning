import numpy as np

a = np.array([10, 20, 30, 40])
b = np.arange(4)
print(a, b)

c = a + b
# c = a - b
print(c)

c = b ** 2
print(c)

c = 10 * np.sin(a)
# c = 10 * np.tan(a)
print(c)

print(b)
print(b < 3)
print(b == 3)

a = np.array([[1,1],
              [0,1]])
b = np.arange(4).reshape((2,2))

c = a * b
c_dot = np.dot(a,b)
c_dot_2 = a.dot(b)
print(c)
print(c_dot)
print(c_dot_2)

a = np.random.random((2, 4))
print(a)
print(np.sum(a, axis=1))
print(np.min(a, axis=1))
print(np.max(a, axis=0))

A = np.arange(2,14).reshape((3,4))
print(A)
print(np.argmin(A))
print(np.argmax(A))

print(np.mean(A))
print(A.mean())
print(np.average(A))

print(np.median(A))

print(A)
print(np.cumsum(A))
print(np.diff(A))

print(np.nonzero(A))

A = np.arange(14, 2, -1).reshape(3, 4)
print(A)
print(np.sort(A))

print(A)
print(np.transpose(A))
print(A.T)
print((A.T).dot(A))

print(A)
print(np.clip(A, 5, 9))

print(A)
print(np.mean(A, axis=1))
print(np.mean(A, axis=0))