print('СЛОВАРИ')
my_dict = {'Igor': 1996, 'Mark': 2002, 'Gleb': 1984}
print('Исходный словарь:', my_dict)
print('Год рождения Igor:',my_dict['Igor'])
print('Год рождения Roman (нет в словаре):', my_dict.get('Roman'))
my_dict.update({'Semen': 2004, 'Petr': 1992})
print('Добавили Semen и Petr:', my_dict)
print('Забрали из словаря Semen, его год рождения::', my_dict.pop('Semen'))
print('Словарь без Semen:', my_dict)

print('')
print('МНОЖЕСТВА')
my_set = {1, 2, 3.14, 2, 'one', 'two', 'three', False, True, -60, (1, 2, 4), 4, 1, True, (1, 2, 4), (4,7,8,9,1)}
print('Исходное множество:', my_set)
my_set.add(2024)
my_set.add('Praga')
print('Множество (добавили 2024 и "Praga"):', my_set)
my_set.remove(-60)
print('Множество (удалили -60):', my_set)

# phone_book = {'Ab1': 89255065019, 'Ab2': 89165673212}
# print(phone_book)
# print(type(phone_book))
# print(phone_book['Ab1'])
# phone_book['Ab1'] = 657463544
# print(phone_book['Ab1'])
# phone_book['Ab_new'] = 3872395834
# print(phone_book)
# del phone_book['Ab2']
# print(phone_book)
# phone_book.update({'Ab1': 35453, 'Saha': 76858946754, 'Alex': 9403458349})
# print(phone_book.get('Ab_new'))
# print(phone_book.get('Ab_new1'))
# print(phone_book)
# print(phone_book.pop('Ab1'))
# print(phone_book)
# print(phone_book.keys())
# print(phone_book.values())
# print(phone_book.items())

# set_ = {8, 1,2,3,4,1,2,3,4,5,6}
# list_ = [8, 1,2,3,4,1,2,3,4,5,6]
# list_ = set(list_)
# print(list_)
# print(list_.discard(1))
# print(list_)
# print(list_.remove(2))
# print(list_)
# print(list_.add(52))
# print(list_)
# print(list_.pop())
# print(list_)