pop = [30.55, 2.77, 39.21]
countries = ['afghanistan', 'albania', 'algeria']
ind_alb = countries.index('albania')

world = {'afghnanistan': 30.55, 'albania': 2.77, 'algeria': 39.21}
print(world['albania'])

immutable = {0: 'hello', True: 'dear', 'two': 'world'}
print(immutable)

# test = {['just', 'to', 'test']:'value'}

world['sealand'] = 0.000027
print(world)

print('sealand' in world)

world['sealand'] = 0.000028
print(world)

del (world['sealand'])
print(world)

print('python'.title())
print(3 ** 2 - int(3.2))
print(True % 20 * 5)
print(True % 20)
print('teste0', int(6 / 10) - (bool('python') + 1))
print('teste', int(6 / 10))
print('teste2', bool('python') + 1)
print(int(bool('python')))
print(True * 2 % 10 - False ** 5)
print(int(False))

