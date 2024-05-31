class Figure:
    sides_count = 3

    def __init__(self, color, *sides, filed=False):
        self.__sides = list(sides) if self._is_valid_sides(*sides) else [1 for _ in range(self.sides_count)]
        self.__color = color if self._is_valid_color(color) else [0, 0, 0]
        self.filed = filed

    def get_color(self):
        """ Return the color"""
        return list(self.__color)

    def set_color(self, *color):
        """ Set the color"""
        self.__color = color if self._is_valid_color(color) else self.__color

    @staticmethod
    def _is_valid_color(color):
        """ Проверка на корректность цвета"""
        return all(isinstance(c, int) and 0 < c < 256 for c in color)

    def get_sides(self):
        """ Return the sides"""
        return list(self.__sides)

    def _is_valid_sides(self, *sides):
        """ Проверка на корректность сторон"""
        return len(sides) == self.sides_count

    def set_sides(self, *sides):
        """ Set the sides"""
        self.__sides = list(sides) if self._is_valid_sides(*sides) else self.__sides

    def __len__(self):
        """
        Возвращает периметр фигуры
        """
        pass


if __name__ == '__main__':
    figure = Figure([255, 255, 255], 10, 2, 3)
    print(figure.get_color())
    print(figure.get_sides())
    figure.set_color([255, 221, 132])
    print(figure.get_color())
    figure.set_sides(1, 2, 3)
    print(figure.get_sides())
