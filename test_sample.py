import pytest
# content of test_sample.py
class TestDemo():
    def func(self,x):
        self.x = x
        return x + 1


    def test_answer(self):
        # assert self.func(3) == 4
        # 即使断言报错了，还会继续执行
        pytest.assume(self.func(3) == 4)
        print("____________")

    def test_b(self):
        # assert self.func(3) == 4
        pytest.assume(self.func(3) == 4)
        print("____________")

    def test_c(self):
        x = 'hello'
        assert 'h' in x

class TestDemo1():
    def func(self,x):
        self.x = x
        return x + 2

    def test_a(self):
        assert self.func(3) == 5
        print("______llll______")

    def test_b(self):
        # assert self.func(3) == 15
        pytest.assume(self.func(3) == 5)
        print("______hhhh______")

if __name__ == '__main__':
    # pytest.main("-v -x TestDemo")
    # pytest.main(['-v','-s','TestDemo'])
    pytest.main()