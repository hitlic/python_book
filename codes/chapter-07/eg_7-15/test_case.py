import unittest
from math_methods import MathMethods

class TestMathMethods(unittest.TestCase):
    def setUp(self):
        self.unit = MathMethods()

    def tearDown(self):
        del self.unit

    def test_add_two_zero(self):
        res = self.unit.add(0, 0)
        print('两个0相加', res)
        self.assertEqual(0, res)

    def test_add_two_positive(self):
        res = self.unit.add(1, 8)
        print('两个正数相加', res)
        self.assertEqual(9, res)

    def test_add_two_negative(self):
        res = self.unit.add(-1, -4)
        print('两个负数相加', res)
        self.assertEqual(-5, res)