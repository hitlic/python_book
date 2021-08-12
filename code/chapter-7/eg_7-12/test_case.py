# 文件 test_case.py
import unittest
from math_methods import MathMethods

class TestMathMethods(unittest.TestCase):
    def test_add_two_zero(self):
        res = MathMethods().add(0, 0)
        print('两个0相加', res)
        self.assertEqual(0, res)

    def test_add_two_positive(self):
        res = MathMethods().add(1, 8)
        print('两个正数相加', res)
        self.assertEqual(9, res)

    def test_add_two_negative(self):
        res = MathMethods().add(-1, -4)
        print('两个负数相加', res)
        self.assertEqual(-5, res)