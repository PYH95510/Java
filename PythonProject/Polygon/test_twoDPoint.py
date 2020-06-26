from unittest import TestCase

from HW5.two_d_point import TwoDPoint


class TestTwoDPoint(TestCase):

    def test_from_coordinates(self):
        t1 = TwoDPoint.from_coordinates([2, 3, 4, 5, 6, 7, 8, 9])
        t2 = TwoDPoint.from_coordinates([10, 11, 12, 13, 14, 15, 16, 17])
        self.assertEqual(t1[0].x, 2)
        self.assertEqual(t2[1].y, 13)
        self.assertEqual(t1, [TwoDPoint(2, 3), TwoDPoint(4, 5), TwoDPoint(6, 7), TwoDPoint(8, 9)])
        self.assertEqual(t2, [TwoDPoint(10, 11), TwoDPoint(12, 13), TwoDPoint(14, 15), TwoDPoint(16, 17)])  # TODO