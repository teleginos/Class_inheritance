from Figure import Figure
from math import sqrt


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        if not self._is_valid_triangle():
            raise ValueError('Не существует треугольника с такими сторонами')
        self.__height = self._set_height()

    def _set_height(self):
        a, b, c = self.get_sides()
        p = (1 / 2) * (a + b + c)
        h = 2 * sqrt(p * (p - a) * (p - b) * (p - c)) / a
        return h

    def get_height(self):
        return self.__height

    def _is_valid_triangle(self):
        a, b, c = self.get_sides()
        return a + b > c and a + c > b and b + c > a

    def get_square(self):
        return (1 / 2) * self.get_sides()[2] * self.get_height()

    def __len__(self):
        a, b, c = self.get_sides()
        return a + b + c


if __name__ == '__main__':
    triangle = Triangle([255, 255, 255], 5, 4, 2)
    print(triangle.get_color())
    print(triangle.get_sides())
    print(triangle.get_square())

