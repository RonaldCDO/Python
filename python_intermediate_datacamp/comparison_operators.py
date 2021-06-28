import numpy as np
import pandas as pd

a = 'Ronald'
b = 'Naná'

print(a > b)

x1 = 'b'
x2 = 'c'

print(x1 >= x2)

bmi = np.array([21.8, 20.975, 21.75, 25.747, 21.441])
print(bmi > 23, '\n')

brics = pd.read_csv('brics.csv', index_col=0)
print(brics)

print(brics['area'])
is_huge = brics['area'] > 8
print(brics[is_huge], '\n')

print(brics[brics['area'] > 8], '\n')

print(np.logical_and(brics['area'] > 8, brics['area'] < 10), '\n')
print(brics[np.logical_and(brics['area'] > 8, brics['area'] < 10)], '\n')

