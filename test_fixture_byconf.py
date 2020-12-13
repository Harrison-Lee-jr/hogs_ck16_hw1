import pytest
# @pytest.fixture()
# def myfixture():
#     print('执行我的fixture')
# 可提取到conftest.py 文件名固定写法。这样package内所有文件都可调用执行

class Test_demo():
    def test_one(self):
        print('执行test_one')
        assert 1+1==2
    def test_two(self,myfixture):
        print('执行test_two')
        # myenv=myfixture
        # print(myenv)
        assert 1+1==2
    def test_three(self):
        print('执行test_three')
        assert 1+1==2