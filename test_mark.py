import pytest
class Test_demo():
    # 打标签，配合-m "demo" 运行
    @pytest.mark.demo
    def test_demo(self):
        print('my first testcase')
    @pytest.mark.smoke
    def test_two(self):
        print('my second testcase')