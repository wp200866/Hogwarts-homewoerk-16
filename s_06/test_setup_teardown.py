import pytest

def setup_module():
    print("setup:整个模块只执行一次,开始的时候执行")

def teardown_module():
    print("teardown:整个模块只执行一次,结束的时候执行")

def setup_function():
    print("\nsetup:不在类中的测试用例，开始的时候都会执行")

def teardown_function():
    print("teardown:不在类中的测试用例，结束的时候都会执行")

def test_tree():
    print("test-three")

def test_four():
    print("test-four")

class TestClass():
    def setup_class(self):
        print("setup_class:类里面所有用例开始执行")
    def teardown_class(self):
        print("teardown_class:类里面所有用例开始执行")

    def setup_method(self):
        print("setup:每个用例开始执行")
    def teardown_method(self):
        print("teardown:每个用例结束执行")
    def test_one(self):
        print("test-one")
    def test_two(self):
        print("test-two")
