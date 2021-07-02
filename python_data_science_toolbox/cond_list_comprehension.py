print([num for num in range(0, 26) if num % 2 == 1])

age = [num for num in range(0, 100) if num >= 18
       and num % 2 == 0 and num % 3 == 0 and num % 4 == 0]

print(age)

pos_and_neg = {num: -num for num in range(6)}
print(pos_and_neg)
print(type(pos_and_neg))

a_list = ['Alfredo', 'Alberto', 'Josiane', 'Bob']

dict_string_lenght = {member: len(member) for member in a_list}

print(dict_string_lenght)