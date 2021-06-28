import numpy as np

store = np.array([0, 9, 0, 1])
cost = np.array([82, 82, 73, 73])
np_cols = np.column_stack((store, cost))

print(np_cols)

np_array = np.array([1, 2, 3])
print(type(np_array))

p = 0
print([p, 3])

list_ = [1, 2, 3, -2, -6, -4, 5]

print(list_.index(-6))

np_heights = np.array([[1.60, 1.75], [1.56, 1.70], [1.49, 1.68]])
print(np.mean(np_heights[:, 0]))
print(np_heights[:])

test = [1,2,3,4,5,6,7,8,9,10]
print(np.average(test))

g = [1,2,3,55,66,77]
f = np.ma.masked_greater(g,5)

