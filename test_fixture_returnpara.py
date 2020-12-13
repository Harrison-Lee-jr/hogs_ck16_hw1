import pytest
@pytest.fixture(params=['para1','para2'])
def myfixture2(request):
    return request.param
def test_print_param(myfixture2):
    print('excute test_case')
    print(myfixture2)
    assert 1==1