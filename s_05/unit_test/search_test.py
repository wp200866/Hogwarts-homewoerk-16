# 被测方法
import unittest

class Search:
    def search_fun(self):
        print("search")
        return True

class TestSearch(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        print("setup class")
        cls.search = Search()

    @classmethod
    def tearDownClass(cls) -> None:
        print("teardown class")

    def test_search1(self):
        print("testsearch1")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search2(self):
        print("testsearch2")
        # search = Search()
        assert True == self.search.search_fun()

    def test_search3(self):
        print("testsearch3")
        # search = Search()
        assert True == self.search.search_fun()

    def test_equal(self):
        print("断言相等")
        self.assertEqual(1,1,"判断 1==1")

    def test_notequal(self):
        print("断言不相等")
        self.assertNotEqual(1,2,"判断 1 != 2")
        self.assertTrue(1==1, "verify")

if __name__ == '__main__':
    # # 方法一，执行当前文件所有的unittest测试
    # unittest.main()

    # # 方法二：执行指定的测试用例，将要执行的测试用例添加到测试套件立面，批量执行
    # 执行指定的测试用例
    # 创建一个测试套件，testsute
    # suite = unittest.TestSuite()
    # suite.addTest(TestSearch("test_search1"))
    # suite.addTest(TestSearch("test_search3"))
    # unittest.TextTestRunner().run(suite)

    # 方法三：执行某个测试类
    suite1 = unittest.TestLoader().loadTestsFromTestCase(TestSearch)
    suite = unittest.TestSuite([suite1])
    unittest.TextTestRunner(verbosity=2).run(suite)