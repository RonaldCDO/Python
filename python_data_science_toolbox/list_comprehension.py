nums = [1, 2, 3, 4, 5]

result = [num + 1 for num in nums]
print('first way')
print(result)

result2 = []
# same as
for num in nums:
    result2.append(num + 1)
print('second way')
print(result2)

result_range = [num for num in range(10)]
print('first way')
print(result_range)

# same as
result_range2 = []
for num in range(10):
    result_range2.append(num)
print('second way')
print(result_range2)

# nested loops
pairs_1 = []
for num1 in range(0, 3):
    for num2 in range(0, 3):
        pairs_1.append((num1, num2))
print('first way')
print(pairs_1)

# same as
pairs_2 = [(num1, num2) for num1 in range(0, 3) for num2 in range(0, 3)]
print('second way')
print(pairs_2)

