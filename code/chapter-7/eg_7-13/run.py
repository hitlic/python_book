import unittest
from test_case import TestMathMethods

suite = unittest.TestSuite()     # 测试套件
loader = unittest.TestLoader()   # 测试加载器
suite.addTest(loader.loadTestsFromTestCase(TestMathMethods))

file = open('test_result.txt', 'w+')
# verbosity用于控制测试报告的详细程度
runner = unittest.TextTestRunner(stream=file, verbosity=2)
runner.run(suite)
