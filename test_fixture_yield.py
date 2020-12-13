import pytest
@pytest.fixture(params=['par1','par2'])
def connect_db(request):
    print('begin to connect mysql')
    yield request.param
    print('teardown to close sqlconnect')

def test_print_param(connect_db):
    print('excute case')
    print(connect_db)
    assert 1==1