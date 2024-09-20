first = ['Strings', 'Student', 'Computers']
second = ['Строка', 'Урбан', 'Компьютер']

first_result = (len(z[0]) - len(z[1]) for z in zip(first, second) if len(z[0]) != len(z[1]))
second_result = (len(first[i]) == len(second[i]) for i in range(0, len(first)))

print(list(first_result))
print(list(second_result))
