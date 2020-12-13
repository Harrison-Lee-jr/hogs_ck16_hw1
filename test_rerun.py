import pytest
import random
# @pytest.mark.flaky(reruns=6, reruns_delay=2)
def test_example():
    print(3)
    assert random.choice([True, False])