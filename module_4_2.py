def test_function():
    def inner_function():
        print('Я в области видимости функции test_function')
        pass

    inner_function()
    pass

test_function()

# При вызове inner_function() вне функции test_function() выдается ошибка:
# Traceback (most recent call last):
#   File "D:\Python\PycharmProjects\datas\module_4_2.py", line 10, in <module>
#     inner_function()
#     ^^^^^^^^^^^^^^
# NameError: name 'inner_function' is not defined. Did you mean: 'test_function'?
