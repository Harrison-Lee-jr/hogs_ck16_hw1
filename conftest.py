import pytest
from pythoncode.calculator import Calculator

#test_calc2.py用
@pytest.fixture(scope='module')
def cal2():
    set='【开始计算】'
    print(set)
    cal=Calculator()
    yield cal
    print('【计算结束】')

#设置后用例里不用加fixture，全部调用生效。不建议用
#@pytest.fixture(autouse='true')

#作用域：
#@pytest.fixture(scope='class')
#@pytest.fixture(scope='module')
#@pytest.fixture(scope='session')
#@pytest.fixture(scope='function')

#fixture参数化，有几个参数就会调用几次
# @pytest.fixture(params=["***参数1***","***参数2***"])
# def myfixture(request):
#     print('\n执行我的fixture，里面的参数是：%s\n'% request.param)
#     env=request.param
#     return env

# yield:
# @pytest.fixture(params=["***参数1***","***参数2***"])
# def myfixture(request):
#     print('\n执行我的fixture，里面的参数是：%s\n'% request.param)
#     yield request.param #类似return,但yield返回值后，它后面的代码仍可执行；而return后的代码不会被执行
#     print('激活fixture里面的teardown操作：如清理数据，关闭数据库连接，关闭浏览器，登出等')

# @pytest.fixture()
# def myfixture():
#     print('执行我的fixture')
# def connectdb():
#     print('执行我的fixture--connectdb')

def pytest_collection_modifyitems(session, config, items):
    print(type(items)) #items是一个列表list
    items.reverse()
    for item in items:
        item.name = item.name.encode('utf-8').decode('unicode-escape')
        item._nodeid = item.nodeid.encode('utf-8').decode('unicode-escape')
        print('item.name是%s' % item.name)
        print('item.nodeid是%s' % item._nodeid)
        # 加标签
        if "add" in item._nodeid:
            item.add_marker(pytest.mark.add)
        if "div" in item._nodeid:
            item.add_marker(pytest.mark.div)