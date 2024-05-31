from Figure import Figure
from math import pi


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self.__radius = self._set_radius(*sides)

    def get_square(self):
        """ Return the square"""
        return round(pi * self.__radius ** 2, 2)

    @staticmethod
    def _set_radius(*sides):
        """ Return the radius of the circle"""
        return round(sides[0] / (2 * pi), 2)

    def set_sides(self, *sides):
        """ Set the radius of the circle"""
        self.__radius = self._set_radius(*sides)

    def get_radius(self):
        return self.__radius

    def __len__(self):
        return int(2 * pi * self.__radius)


if __name__ == '__main__':
    circle = Circle([255, 255, 255], 100)
    print(circle.get_color())
    print(circle.get_sides())
    print(circle.get_radius())
    circle.set_color([251, 121, 132])
    print(circle.get_color())
    circle.set_sides(20)
    print(circle.get_sides())
    print(circle.get_radius())
    print(circle.get_square())
    print(len(circle))
