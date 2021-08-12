import unittest
from unit_test import TestMathMethods

suite = unittest.TestSuite()
tests = [
    TestMathMethods('test_add_two_zero'),
    TestMathMethods('test_add_two_negative'),
    TestMathMethods('test_add_two_positive')
]

suite.addTests(tests)

runner = unittest.TextTestRunner(verbosity=2)
runner.run(suite)
