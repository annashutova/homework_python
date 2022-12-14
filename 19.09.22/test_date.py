import date_validator
import pytest


tests = [('12.03.2021', True), ('29.02.2005', False), ('31.10.22', True)]


@pytest.mark.parametrize('inp, answer', tests)
def test_date(inp, answer):
    """Tests valid_date function."""
    assert date_validator.valid_date(inp) == answer
