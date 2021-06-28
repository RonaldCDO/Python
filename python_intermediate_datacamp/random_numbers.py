import numpy as np

np.random.seed(123)
outcomes = []

for x in range(10):
    coin = np.random.randint(0, 2)
    if coin == 0:
        outcomes.append('heads')
    else:
        outcomes.append('tails')
print(outcomes)

tails = [0]

for y in range(10):
    gp = np.random.randint(0, 2)
    tails.append(tails[y] + gp)
print(tails)

teste = tails[-1]
print(teste)