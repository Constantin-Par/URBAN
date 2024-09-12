def add_everything_up(a, b):
    try:
        с = a + b
    except TypeError:
        if type(a) is int or type(a) is float:
            a = str(a)
        if type(b) is int or type(b) is float:
            b = str(b)
        return a + b
    else:
        return a + b


print(add_everything_up(123.456, 'строка'))
print(add_everything_up('яблоко', 4215))
print(add_everything_up(123.456, 7))
