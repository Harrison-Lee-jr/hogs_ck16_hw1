import pytest
@pytest.fixture()
def myfixture1():
    print('执行myfixture')
#可提取到conftest.py 文件名固定写法。这样package内所有文件都可调用执行
class Test_firstFile():
    def test_one(self):
        print('执行test_one')
        assert 1+1==2
    def test_two(self,myfixture1): #加了后在执行用例2时就会先执行fixture
        print('执行test_two')
        assert 1+1==2
    def test_three(self):
        print('执行test_three')
        assert 1+1==2