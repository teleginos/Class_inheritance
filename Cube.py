from Figure import Figure


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, *sides):
        super().__init__(color, *sides)
        self._Figure__sides = [sides[0]] * self.sides_count if self._is_valid_sides(*sides) else [1] * self.sides_count

    def _is_valid_sides(self, *sides):
        return all(side > 0 for side in sides) and len(sides) == 1

    def set_sides(self, *sides):
        self._Figure__sides = [sides[0]] * self.sides_count if self._is_valid_sides(*sides) else self._Figure__sides

    def get_volume(self):
        return pow(*set(self.get_sides()), 3)

    def __len__(self):
        return self.sides_count * self.get_sides()[0]


if __name__ == '__main__':
    cube = Cube([255, 255, 255], 12)
    print(cube.get_color())
    print(cube.get_sides())
    print(len(cube))
    cube.set_sides(10)
    print(cube.get_sides())
    print(len(cube))
