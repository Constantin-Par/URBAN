def custom_write(file_name, strings):
    file = open(file_name, 'w', encoding='utf-8')
    strings_positions = {}
    _line = 0
    for string in strings:
        _line += 1
        strings_positions[(_line, file.tell())] = string
        file.write(f'{string}\n')
    file.close()
    return strings_positions


#print(custom_write("module_7_2.txt", ['строка 1', 'строка 2', 'строка 3', 'строка 4', 'строка 5', 'строка 6']))

info = [
    'Text for tell.',
    'Используйте кодировку utf-8.',
    'Because there are 2 languages!',
    'Спасибо!'
    ]

result = custom_write('module_7_2.txt', info)
for elem in result.items():
  print(elem)