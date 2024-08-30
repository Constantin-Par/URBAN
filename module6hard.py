import math


class Figure:
    sides_count = 0  # а зачем это тут?

    def __init__(self, _sides, _color):
        if self.__is_valid_sides(_sides):
            self.__sides = _sides
        if self.__is_valid_color_list(_color):
            self.__color = _color
        self.filled = False

    def get_color(self):
        return self.__color

    def get_sides(self):
        return self.__sides

    def __is_valid_color(self, r, g, b):
        return self.__is_valid_color_rgb(r) and self.__is_valid_color_rgb(g) and self.__is_valid_color_rgb(b)

    def __is_valid_color_rgb(self, _color):
        return type(_color) is int and 0 <= _color <= 250

    def __is_valid_color_list(self, _color):
        return len(_color) == 3 and self.__is_valid_color(_color[0], _color[1], _color[2])

    def __is_valid_sides(self, _sides):
        for _side in _sides:
            if not type(_side) is int or _side < 1:
                return False
        return True

    def __len__(self):
        _len = 0
        for _side in self.__sides:
            _len += _side
        return _len

    def set_color(self, r, g, b):
        if self.__is_valid_color(r, g, b):
            self.__color = [r, g, b]

    def set_sides(self, *new_sides):
        if len(new_sides) == self.sides_count:
            if self.__is_valid_sides(new_sides):
                self.__sides = list(new_sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, _color, *_sides):
        if len(_sides) > self.sides_count:
            _sides = [1]
        if _sides[0] > 0:
            self.__radius = _sides[0] / 2 / math.pi
        super().__init__(_sides, _color)

    def get_square(self):
        return math.pi * self.__radius ^ 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, _color, *_sides):
        if len(_sides) > self.sides_count:
            _sides = [1, 1, 1]
        super().__init__(_sides, _color)

    def get_square(self):
        _a, _b, _c = super().get_sides()[0], super().get_sides()[1], super().get_sides()[2]
        _p = (_a + _b + _c) / 2
        return math.sqrt(_p * (_p - _a) * (_p - _b) * (_p - _c))


class Cube(Figure):
    sides_count = 12

    def __init__(self, _color, *_rib):
        if len(_rib) > 1:
            _rib = 1
        else:
            _rib = _rib[0]
        _sides = []
        for _i in range(0, 13):
            _sides.append(_rib)
        super().__init__(_sides, _color)

    def get_volume(self):
        return super().get_sides()[0] ** 3


circle1 = Circle((200, 200, 100), 10)  # (Цвет, стороны)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)  # Изменится
print(circle1.get_color())
cube1.set_color(300, 70, 15)  # Не изменится
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)  # Не изменится
print(cube1.get_sides())
circle1.set_sides(15)  # Изменится
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume())
