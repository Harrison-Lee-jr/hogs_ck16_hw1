import pytest
from pythoncode.calculator import Calculator

class TestCalc:
    def setup_class(self):
        self.calc=Calculator()
        print('【开始计算】')
    def teardown_class(self):
        print('【计算结束】')

    @pytest.mark.parametrize('a,b,expect',[
        (3,5,8),(-1,-2,-3),(100,300,400)
    ],ids=['int','minus','bigint'])
    def test_add(self,a,b,expect):
        # cal=Calculator()
        assert expect==self.calc.add(a,b)

    @pytest.mark.parametrize('a,b,expect',[
        (5,4,1),(200,100,100),(10,6,4)
    ])
    def test_sub(self,a,b,expect):
        # cal=Calculator() #与上方add都用了调用计算函数，抽取出来放至setup
        assert expect==self.calc.sub(a,b)

    @pytest.mark.parametrize('a,b,expect',[
        (5,4,20),(20,10,200),(10,6,60)
    ])
    def test_mul(self,a,b,expect):
        assert expect==self.calc.mul(a,b)

    @pytest.mark.parametrize('a,b,expect',[
        (8,4,2),(200,100,2),(10,2,5)
    ])
    def test_div(self,a,b,expect):
        assert expect==self.calc.div(a,b)
