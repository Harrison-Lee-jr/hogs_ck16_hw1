import pytest
import yaml

def get_datas():
    with open("./data.yml") as f:
        datas=yaml.safe_load(f)
        print(datas)
        add_datas=datas['datas']
        add_ids=datas['myid']
        return [add_datas,add_ids]

def add_function(a,b):
    return a+b

@pytest.mark.parametrize("a,b,expected",
get_datas()[0],ids=get_datas()[1])
def test_add(a,b,expected):
    assert add_function(a,b)==expected

# @pytest.mark.parametrize("a,b",[
#     (3,5),(-1,-2),(1000,1000)
# ],ids=["int","minus","bigint"])
# def test_add(a,b):
#     assert add_function(a,b)==a+b
#
# @pytest.mark.parametrize("a",[0,1,5])
# @pytest.mark.parametrize("b",[2,3,8])
# def test_add(a,b):
#     print('测试数据组合：a->%s,b->%s'%(a,b))