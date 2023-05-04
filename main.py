from typing import List


class Point:
    def __init__(self, x: float, y: float) -> None:
        self._x = x
        self._y = y
        # self._z = z

    def get_coordinates(self) -> List[float]:
        return [self._x, self._y, self.z]

    @property
    def z(self):
        return 2 * self._x

    @z.setter
    def z(self, value):
        self._x = value

    @z.deleter
    def z(self):
        del self._x


my_point = Point(2.5, 6.3)
print(my_point.get_coordinates())
# print(my_point.x)
