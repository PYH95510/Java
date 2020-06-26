from .rectangle import Rectangle
from .quadrilateral import Quadrilateral
from .two_d_point import TwoDPoint


class Square(Rectangle):

    def __init__(self, *floats) -> None:
        super().__init__(*floats)
        if not self.__is_member():
            raise TypeError("A square cannot be formed by the given coordinates.")

    def __repr__(self) -> str:
        return ' It is square and vertices:' + str(self.vertices)

    def __str__(self) -> str:
        return 'Square is '

    def __eq__(self, other) -> bool:
        if isinstance(other, Square) and self.vertices[0].x == other.vertices[0].x and self.vertices[0].y == \
                other.vertices[0].y and self.vertices[1].x == other.vertices[1].x and self.vertices[1].y == \
                other.vertices[1].y and self.vertices[2].x == other.vertices[2].x and self.vertices[2].y == \
                other.vertices[2].y and self.vertices[3].x == other.vertices[3].x and self.vertices[3].y == \
                other.vertices[3].y:
            return True
        else:
            return False

    def __add__(self, other: object) -> object:
        return Square(self.vertices[0].x + other.vertices[0].x, self.vertices[0].y + other.vertices[0].y,
                      self.vertices[1].x + other.vertices[1].x, self.vertices[1].y + other.vertices[1].y,
                      self.vertices[2].x + other.vertices[2].x, self.vertices[2].y + other.vertices[2].y,
                      self.vertices[3].x + other.vertices[3].x, self.vertices[3].y + other.vertices[3].y)

    def __sub__(self, other: object) -> object:
        return Square(self.vertices[0].x - other.vertices[0].x, self.vertices[0].y - other.vertices[0].y,
                      self.vertices[1].x - other.vertices[1].x, self.vertices[1].y - other.vertices[1].y,
                      self.vertices[2].x - other.vertices[2].x, self.vertices[2].y - other.vertices[2].y,
                      self.vertices[3].x - other.vertices[3].x, self.vertices[3].y - other.vertices[3].y)

    def __is_member(self) -> bool:
        if self.vertices.__len__() == 4:
            x1 = abs(self.vertices[0].x - self.vertices[1].x)
            x2 = abs(self.vertices[2].x - self.vertices[3].x)
            y1 = abs(self.vertices[0].y - self.vertices[1].y)
            y2 = abs(self.vertices[2].y - self.vertices[3].y)

            if x1 == y1 and x2 == y2 and x1 == x2 and y1 == y2:
                return True
            else:
                return False

    def snap(self) -> object:
        """Snaps the sides of the square such that each corner (x,y) is modified to be a corner (x',y') where x' is the
        integer value closest to x and y' is the integer value closest to y. This, of course, may change the shape to a
        general quadrilateral, hence the return type. The only exception is when the square is positioned in a way where
        this approximation will lead it to vanish into a single point. In that case, a call to snap() will not modify
        this square in any way."""
        rx1 = round(self.vertices()[0].x)
        rx2 = round(self.vertices()[1].x)
        rx3 = round(self.vertices()[2].x)
        rx4 = round(self.vertices()[3].x)

        ry1 = round(self.vertices()[0].y)
        ry2 = round(self.vertices()[1].y)
        ry3 = round(self.vertices()[2].y)
        ry4 = round(self.vertices()[3].y)
        if rx1 == rx2 == rx3 == rx4 and ry1 == ry2 == ry3 == ry4:
            return self
        else:
            self.vertices()[0].x = rx1
            self.vertices()[1].x = rx2
            self.vertices()[2].x = rx3
            self.vertices()[3].x = rx4
            self.vertices()[0].y = ry1
            self.vertices()[1].y = ry2
            self.vertices()[2].y = ry3
            self.vertices()[3].y = ry4
            return self

