import numpy as np
import pandas as pd

# while loop
error = 50.0

while error > 1:
    error /= 4
    print(error, '\n')

fam = [1.73, 1.68, 1.71, 1.89]
print(fam[0])
print(fam[1])
print(fam[2])
print(fam[3], '\n')

# for loop
for index, height in enumerate(fam):
    print('index' + str(index) + ' : ' + str(height), '\n')

for c in 'family':
    print(c.capitalize())
print()

# Data Structures loop
a = {0: 'zero', 1: 'um', 3: 'tres', 2: 'dois', 1: 'um'}
for i in enumerate(a):
    print(i)
print()
for i in a:
    print(a[i])
print()
for i in a:
    print(a[i].upper())
print()

world = {'afghanistan': 30.55,
         'albania': 2.77,
         'algeria': 39.21}

for i in world:
    print(i, world[i])
print()

for key, value in world.items():
    print(key + ' -- ' + str(value), '\n')

np_height = np.array([1.73, 1.68, 1.71, 1.89, 1.79])
np_weight = np.array([65.4, 59.2, 63.6, 88.4, 68.7])
bmi = np_weight / np_height ** 2

for val in bmi:
    print('%.2f' % val)
    print('{:.2f}'.format(val))
print()

meas = np.array([np_height, np_weight])

for val in meas:
    print(val)
print()

for val in np.nditer(meas):
    print(val)
print()

# Loop Data Structures part 2

brics = pd.read_csv('brics.csv', index_col=0)

for i in brics:
    print(i)
print()
for lab, row in brics.iterrows():
    print(lab + ': ' + row['capital'])
print()

for lab, row in brics.iterrows():
    brics.loc[lab, 'name_lenght'] = len(row['country'])
print(brics)

brics['name_lenght'] = brics['country'].apply(len)
print(brics)



