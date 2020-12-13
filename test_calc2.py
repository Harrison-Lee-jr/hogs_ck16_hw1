import pytest
import yaml

def getdata():
    with open("./data.yml") as f:
        yml_data=yaml.safe_load(f)
        add_data=yml_data["data_add"]
        sub_data=yml_data["data_sub"]
        mul_data=yml_data["data_mul"]
        div_data=yml_data["data_div"]
        ids=yml_data["myid"]
        return [ids,add_data,sub_data,mul_data,div_data]

class TestCalc2:
    @pytest.mark.run(order=4)
    @pytest.mark.parametrize('a,b,expect',getdata()[1],ids=getdata()[0])
    def test_add2(self,a,b,expect,cal2):
        assert expect==cal2.add(a,b)

    @pytest.mark.run(order=3)
    @pytest.mark.parametrize('a,b,expect',getdata()[2],ids=getdata()[0])
    def test_sub2(self,a,b,expect,cal2):
        assert expect==cal2.sub(a,b)

    @pytest.mark.run(order=2)
    @pytest.mark.parametrize('a,b,expect',getdata()[3],ids=getdata()[0])
    def test_mul2(self,a,b,expect,cal2):
        assert expect==cal2.mul(a,b)

    @pytest.mark.run(order=1)
    @pytest.mark.parametrize('a,b,expect',getdata()[4],ids=getdata()[0])
    def test_div2(self,a,b,expect,cal2):
        assert expect==cal2.div(a,b)
