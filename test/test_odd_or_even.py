from src.odd_or_even import odd_or_even
import pytest

@pytest.mark.par_o_impar
def test_odd_or_even():
    assert odd_or_even([0, 1, 2]) == "odd"
    assert odd_or_even([0, 1, 3]) == "even"
    assert odd_or_even([1023, 1, 2]) == "even"