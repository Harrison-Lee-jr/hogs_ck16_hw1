import pytest
@pytest.mark.run(order=2)
def test_1():
    assert 1
@pytest.mark.run(order=1)
def test_2():
    assert 2