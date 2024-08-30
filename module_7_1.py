import os.path


class Product:

    def __init__(self, name, weight, category):
        self.name = name
        self.weight = weight
        self.category = category

    def __str__(self):
        return (f'{self.name}, {self.weight}, {self.category}')


class Shop:
    __file_name = 'products.txt'

    def get_products(self):
        if os.path.isfile(self.__file_name):
            _file = open(self.__file_name, 'r')
            products = _file.read()
        else:
            _file = open(self.__file_name, 'w')
            products = ""
        _file.close()
        return products

    def add(self, *products):
        for product in products:
            products_from_file = self.get_products()
            _file = open(self.__file_name, 'a')
            if products_from_file.find(str(product)) == -1:
                _file.write(f'{str(product)}\n')
            else:
                print(f'Продукт {str(product)} уже есть в магазине')
            _file.close()


s1 = Shop()
p1 = Product('Potato', 50.5, 'Vegetables')
p2 = Product('Spaghetti', 3.4, 'Groceries')
p3 = Product('Potato', 5.5, 'Vegetables')

print(p2)  # __str__

s1.add(p1, p2, p3)

print(s1.get_products())
