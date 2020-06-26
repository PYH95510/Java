import unittest
from unittest import TestCase

from .quadrilateral import Quadrilateral
from .rectangle import Rectangle
from .sorter import ShapeSorter
from .square import Square
from .two_d_point import TwoDPoint


class TestQuadrilateral(TestCase):

    def test_side_lengths(self):
        tq = Quadrilateral(5, 5, 10, 5, 9, 2, 5, 2)
        tr = Rectangle(1, 10, 10, 10, 10, 0, 1, 0)
        ts = Square(2, 2, 4, 2, 4, 0, 2, 0)

        self.assertEqual(tq.side_lengths(), (5, 3.162277660168379, 4, 3))
        self.assertEqual(tr.side_lengths()[1], 10.0)
        self.assertEqual(ts.side_lengths()[2], 2.0)  # TODO

    def test_smallest_x(self):
        tq = Quadrilateral(5, 5, 10, 5, 9, 2, 5, 2)
        tr = Rectangle(1, 10, 10, 10, 10, 0, 1, 0)
        ts = Square(2, 2, 4, 2, 4, 0, 2, 0)

        self.assertEqual(tq.smallest_x(), 5)
        self.assertEqual(tr.smallest_x(), 1)
        self.assertEqual(ts.smallest_x(), 0)  # TODO

    def test_sort(self):
        tq1 = Quadrilateral(5, 5, 10, 5, 9, 2, 5, 2)
        tr1 = Rectangle(1, 10, 10, 10, 10, 0, 1, 0)
        ts1 = Square(2, 2, 4, 2, 4, 0, 2, 0)

        tq2 = Quadrilateral(2, 4, 7, 10, 10, 7, 5, 1)
        tr2 = Rectangle(4, 6, 20, 6, 20, 1, 4, 1)
        ts2 = Square(1, 1, 2, 1, 2, 0, 1, 0)

        tq3 = Quadrilateral(-6, 8, 3, 7, 6, -4, -5, 1)
        tr3 = Rectangle(9, 11, 10, 11, 10, 9, 9, 9)
        ts3 = Square(11, 20, 31, 20, 31, 0, 11, 0)

        self.assertEqual(ShapeSorter.sort(tq1, tr1, ts1), [tr1, tq1, ts1])
        self.assertEqual(ShapeSorter.sort(tq2, tr2, ts2), [tr2, tq2, ts2])
        self.assertEqual(ShapeSorter.sort(tq3, tr3, ts3), [ts3, tq3, tr3])
        self.assertEqual(ShapeSorter.sort(tq1, tq2, tq3, ts1, ts2, ts3), [ts3, tq3, tq2, tq1, ts2, ts1])

    def test_member(self):
        tq1 = Quadrilateral(5, 5, 10, 5, 9, 2, 5, 2)
        tr1 = Rectangle(1, 10, 10, 10, 10, 0, 1, 0)
        ts1 = Square(2, 2, 4, 2, 4, 0, 2, 0)
        tq2 = Quadrilateral(5, 5, 10, 5, 9, 2, 5, 2)
        tr2 = Quadrilateral(1, 10, 10, 10, 10, 0, 1, 0)
        ts2 = Quadrilateral(2, 2, 4, 2, 4, 0, 2, 0)

        self.assertEqual(tq1.__eq__(tq2), True)
        self.assertEqual(tr1.__eq__(tr2), False)
        self.assertEqual(tr2.__eq__(tr1), True)
        self.assertEqual(ts1.__eq__(ts2), False)
        self.assertEqual(ts2.__eq__(ts1), True)

    def test_snap(self):
        ts1 = Square(2, 2, 4, 2, 4, 0, 2, 0)
        ts2 = Square(2.1, 2.1, 4.1, 2.1, 4.1, 0.1, 2.1, 0.1)

        ts3 = Square(11, 20, 31, 20, 31, 0, 11, 0)
        ts4 = Square(11.4, 20.4, 31.4, 20.4, 31.4, 0.4, 11.4, 0.4)

        self.assertEqual(ts1.snap(), ts2)
        self.assertEqual(ts3.snap(), ts4)

    def test_area(self):
        tr = Rectangle(1, 10, 10, 10, 10, 0, 1, 0)
        ts = Square(2, 2, 4, 2, 4, 0, 2, 0)

        self.assertEqual(tr.area(), 90.0)
        self.assertEqual(ts.area(), 4.0)

    def test_center(self):
        tr = Rectangle(1, 10, 10, 10, 10, 0, 1, 0)
        ts = Square(2, 2, 4, 2, 4, 0, 2, 0)

        self.assertEqual(tr.center(), TwoDPoint(5.5, 5))
        self.assertEqual(ts.center(), TwoDPoint(3.0, 1.0))


if __name__ == "__main__":
    unittest.main()

