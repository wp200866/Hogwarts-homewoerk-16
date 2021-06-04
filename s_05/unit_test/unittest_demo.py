import unittest

class TestStringMethods(unittest.TestCase):

    # setUp 和 tearDown 方法是在每条测试用例前后分别调用的方法
    def setUp(self) -> None:
        print("setup")

    def tearDown(self) -> None:
        print("teardown")

    # setUpClass 和 tearDownClass 是在整个类的前后分别调用的方法
    @classmethod
    def setUpClass(cls) -> None:
        print("set up class")

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def test_abc(self):
        print('test abc')

    def test_upper(self):
        print("tess upper 111")
        self.assertEqual('foo'.upper(), 'FOO')  # 断言操作

    def test_isupper(self):
        print("test isupper 222")
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        print("test_split 333")
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()