from .quadrilateral import Quadrilateral
from .two_d_point import TwoDPoint


class Rectangle(Quadrilateral):

    def __init__(self, *floats) -> None:
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A rectangle cannot be formed by the given coordinates.")

    def __repr__(self) -> str:
        return 'It is rectangle and vertices' + str(self.vertices)

    def __str__(self) -> str:
        return 'Rectangle is'

    def __add__(self, other: object) -> object:
        return Rectangle(self.vertices[0].x + other.vertices[0].x, self.vertices[0].y + other.vertices[0].y,
                         self.vertices[1].x + other.vertices[1].x, self.vertices[1].y + other.vertices[1].y,
                         self.vertices[2].x + other.vertices[2].x, self.vertices[2].y + other.vertices[2].y,
                         self.vertices[3].x + other.vertices[3].x, self.vertices[3].y + other.vertices[3].y)

    def __sub__(self, other: object) -> object:
        return Rectangle(self.vertices[0].x - other.vertices[0].x, self.vertices[0].y - other.vertices[0].y,
                         self.vertices[1].x - other.vertices[1].x, self.vertices[1].y - other.vertices[1].y,
                         self.vertices[2].x - other.vertices[2].x, self.vertices[2].y - other.vertices[2].y,
                         self.vertices[3].x - other.vertices[3].x, self.vertices[3].y - other.vertices[3].y)

    def __is_member(self) -> bool:
        """Returns True if the given coordinates form a valid rectangle, and False otherwise."""
        xs1 = abs(self.vertices[0].x - self.vertices[1].x)
        xs2 = abs(self.vertices[2].x - self.vertices[3].x)
        ys1 = abs(self.vertices[0].y - self.vertices[1].y)
        ys2 = abs(self.vertices[2].y - self.verticies[3].y)

        if xs1 == xs2 and ys1 == ys2:
            return True
        else:  # TODO
            return False

    def center(self) -> object:
        """Returns the center of this rectangle, calculated to be the point of intersection of its diagonals."""
        x1 = self.vertices[0].x - self.vertices[1].x
        y1 = self.vertices[1].y - self.vertices[2].y

        return TwoDPoint(x1/2, y1/2)  # TODO

    def area(self) -> float:
        """Returns the area of this rectangle. The implementation invokes the side_lengths() method from the superclass,
        and computes the product of this rectangle's length and width."""
        wid = self.side_lengths()[0]
        lth = self.side_lengths()[1]
        return wid*lth  # TODO
