import pytest
#多重校验：pytest-assume;一个失败，后面的断言将不再执行
def test_simple_assume_fortrue():
    pytest.assume(1 == 1)
    pytest.assume(True)
    pytest.assume(2==2)

def test_simple_assume_forfalse():
    pytest.assume(1 == 1)
    pytest.assume(2==3)
    pytest.assume(True)