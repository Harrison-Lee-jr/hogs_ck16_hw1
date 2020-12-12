import pytest
class Test_demo():

    def test_one(self):
        a=5
        b=1
        assert a!=b
        print('this is the first case')

    def test_two(self):
        a=-1
        b=1
        assert a!=b
        print('this is the second case')