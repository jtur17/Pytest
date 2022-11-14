from src.int_to_str import number_to_string
import pytest

@pytest.mark.string_1
def test_number_string():
    assert number_to_string(67) == '67'
    