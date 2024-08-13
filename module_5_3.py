class House:
    def __init__(self, name, number_of_floors):
        self.name = name
        self.number_of_floors = number_of_floors

    def go_to(self, new_floor):
        if new_floor > self.number_of_floors or new_floor < 1:
            print(f"{self.name}: этажа {new_floor} не существует")
            return
        for i in range(1, new_floor + 1):
            print(f'{self.name}: этаж {i}')

    def __len__(self):
        return self.number_of_floors

    def __str__(self):
        return f'Название: {self.name}, количество этажей: {self.number_of_floors}'

    def __eq__(self, other):
        if not isinstance(other, House):
            return f'ОШИБКА __eq__: "{other}" не принадлежит классу House'
        return self.number_of_floors == other.number_of_floors

    def __lt__(self, other):
        if not isinstance(other, House):
            return f'ОШИБКА __lt__: "{other}" не принадлежит классу House'
        if not isinstance(other.number_of_floors, int):
            return f'ОШИБКА __lt__: Количество этажей "{other.number_of_floors}" не является целым числом'
        return self.number_of_floors < other.number_of_floors

    def __le__(self, other):
        return self.number_of_floors <= other.number_of_floors

    def __gt__(self, other):
        return self.number_of_floors > other.number_of_floors

    def __ge__(self, other):
        return self.number_of_floors >= other.number_of_floors

    def __ne__(self, other):
        return self.number_of_floors != other.number_of_floors

    def __add__(self, value):
        if not isinstance(value, int):
            return f'ОШИБКА __add__: Количество этажей "{value}" не является целым числом'
        self.number_of_floors += value
        return self

    def __iadd__(self, value):
        self.__add__(value)
        return self

    def __radd__(self, value):
        self.__add__(value)
        return self


h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

h1 = House('ЖК Эльбрус', 10)
h2 = House('ЖК Акация', 20)

print(h1)
print(h2)

print('h1 == h2', h1 == h2)  # __eq__

h1 = h1 + 10  # __add__
print('+ 10', h1)
print('h1 == h2', h1 == h2)

h1 += 10  # __iadd__
print('+= 10', h1)

h2 = 10 + h2  # __radd__
print('10 +', h2)

print('h1 > h2', h1 > h2)  # __gt__
print('h1 >= h2', h1 >= h2)  # __ge__
print('h1 < h2', h1 < h2)  # __lt__
print('h1 <= h2', h1 <= h2)  # __le__
print('h1 != h2', h1 != h2)  # __ne__

print()
print('ОШИБКИ:')
#h1 = h1 + '111'  # __add__
print(h1 + '111')
print(h1 == 2)  # __eq__
print(h1 < 'этаж')  # __lt__
