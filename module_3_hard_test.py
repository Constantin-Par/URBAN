def Convert_to_list(*param):
    list_ = []

 #   print('Вызов:', type(param), param)

    # if param == None:
    #     return list_

    for i in param:
#        print('В цикле:', type(i), i)
        if type(i) in [list, tuple, set]:
#            print('Добавляем значение (LTS):', i)
            list_.extend(Convert_to_list(*i))
        elif isinstance(i, dict):
#            print('Добавляем значение (D):', i)
            list_.extend(Convert_to_list(*i.items()))

        else:
#            print('Добавляем значение:', i)
            list_.append(i)

    # print('Возвращаем:', list_)
    # print('')
    return list_

def calculate_structure_sum(data_structure):
    sum = 0
    list_ = Convert_to_list(*data_structure)
    for i in list_:
        if isinstance(i, int):
            sum += i
        if isinstance(i, str):
            sum += len(i)
    return sum

def calculate_structure_sum_ok(data_structure):
    sum = 0
    if data_structure == None:
        return sum
    if type(data_structure) in [list, tuple, set]:
        for el_str in data_structure:
            sum += calculate_structure_sum(el_str)
    elif type(data_structure) == dict:
        for el_str in data_structure:
            sum += calculate_structure_sum(el_str)
            sum += calculate_structure_sum(data_structure[el_str])
    elif type(data_structure) == str:
        sum += len(data_structure)
    elif type(data_structure) in [int, float, complex]:
        sum += data_structure
    return sum


# result = calculate_structure_sum(data_structure)
# print(result)

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

print('Результат calculate_structure_sum:', calculate_structure_sum(data_structure))
