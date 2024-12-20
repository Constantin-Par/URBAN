def Convert_any_to_list(*param):
    list_ = []
    for i in param:
        if type(i) in [list, tuple, set]:
            list_.extend(Convert_any_to_list(*i))
        elif isinstance(i, dict):
            list_.extend(Convert_any_to_list(*i.items()))
        else:
            list_.append(i)
    return list_


def calculate_structure_sum(data_structure):
    sum = 0
    list_ = Convert_any_to_list(*data_structure)
    for i in list_:
        if isinstance(i, int):
            sum += i
        elif isinstance(i, str):
            sum += len(i)
    return sum


data_structure = [[1, 2, 3], {'a': 4, 'b': 5}, (6, {'cube': 7, 'drum': 8}), "Hello",
                  ((), [{(2, 'Urban', ('Urban2', 35))}])]

result = calculate_structure_sum(data_structure)
print(result)
