import math

from .two_d_point import TwoDPoint
from typing import Tuple


class Quadrilateral:

    def __init__(self, *floats) -> None:
        points = TwoDPoint.from_coordinates(list(floats))
        self.__vertices = tuple(points[0:4])

    @property
    def __str__(self) -> str:
        return 'Quadrilateral is'

    def __repr__(self) -> str:
        return 'It is quadrilateral and vertices:' + str(self.vertices)

    def __add__(self, other: object) -> object:
        return Quadrilateral(self.vertices[0].x + other.vertices[0].x, self.vertices[0].y + other.vertices[0].y,
                             self.vertices[1].x + other.vertices[1].x, self.vertices[1].y + other.vertices[1].y,
                             self.vertices[2].x + other.vertices[2].x, self.vertices[2].y + other.vertices[2].y,
                             self.vertices[3].x + other.vertices[3].x, self.vertices[3].y + other.vertices[3].y)

    def __eq__(self, other: object) -> bool:
        if isinstance(other, Quadrilateral) and self.vertices[0].x == other.vertices[0].x and self.vertices[0].y == \
                other.vertices[0].y and self.vertices[1].x == other.vertices[1].x and self.vertices[1].y == \
                other.vertices[1].y and self.vertices[2].x == other.vertices[2].x and self.vertices[2].y == \
                other.vertices[2].y and self.vertices[3].x == other.vertices[3].x and self.vertices[3].y == \
                other.vertices[3].y:
            return True
        else:
            return False

    def __ne__(self, other: object) -> bool:
        return not self.__eq__(other)

    def __sub__(self, other: object) -> object:
        return Quadrilateral(self.vertices[0].x - other.vertices[0].x, self.vertices[0].y - other.vertices[0].y,
                             self.vertices[1].x - other.vertices[1].x, self.vertices[1].y - other.vertices[1].y,
                             self.vertices[2].x - other.vertices[2].x, self.vertices[2].y - other.vertices[2].y,
                             self.vertices[3].x - other.vertices[3].x, self.vertices[3].y - other.vertices[3].y)

    def vertices(self) -> Tuple:
        return self.__vertices

    def side_lengths(self) -> tuple:
        """Returns a tuple of four floats, each denoting the length of a side of this quadrilateral. The value must be
        ordered clockwise, starting from the top left corner."""
        si1x = math.pow(self.vertices[0].x - self.vertices[1].x, 2)
        si1y = math.pow(int(self.vertices[0].y) - int(self.vertices[1].y), 2)
        si2x = math.pow(int(self.vertices[1].x) - int(self.vertices[2].x), 2)
        si2y = math.pow(int(self.vertices[1].y) - int(self.vertices[2].y), 2)
        si3x = math.pow(int(self.vertices[2].x) - int(self.vertices[3].x), 2)
        si3y = math.pow(int(self.vertices[2].y) - int(self.vertices[3].y), 2)
        si4x = math.pow(int(self.vertices[3].x) - int(self.vertices[0].x), 2)
        si4y = math.pow(int(self.vertices[3].y) - int(self.vertices[0].y), 2)

        side1 = math.sqrt(si1x + si1y)
        side2 = math.sqrt(si2x + si2y)
        side3 = math.sqrt(si3x + si3y)
        side4 = math.sqrt(si4x + si4y)

        sides = (side1, side2, side3, side4)

        return sides  # TODO

    def smallest_x(self) -> float:
        """Returns the x-coordinate of the vertex with the smallest x-value of the four vertices of this
        quadrilateral."""
        small1 = 0.0
        small2 = 0.0
        if self.vertices[0].x <= self.vertices[1].x:
            small1 = self.vertices[0].x
        else:
            small1 = self.vertices[1].x

        if self.vertices[2].x <= self.vertices[3].x:
            small2 = self.vertices[2].x
        else:
            small2 = self.vertices[3].x

        if small1 < small2:
            return small1
        else:
            return small2  # TODO


