print("Распаковка позиционных параметров")


def print_params(a=1, b='строка', c=True):
    print(a, b, c)


print_params(b=25)
print_params(c=[1, 2, 3])

values_list = [1, True, 'Строка']
values_dict = {'a': 1, 'b': True, 'c': 'Строка'}

print_params(*values_list)
print_params(**values_dict)

values_list_2 = [54.32, 'Строка']
print_params(*values_list_2, 42)
