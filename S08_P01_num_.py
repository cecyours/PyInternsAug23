import numpy as np

arr = np.array([[2, 4, 5],
                [3, 5, 6]], dtype=float)

print(arr)
print(id(arr))

print("----------------")

matrix = np.zeros((3))
print(matrix)


print("-------------")
x = np.linspace(1, 10, 3)
print(x < 2)
