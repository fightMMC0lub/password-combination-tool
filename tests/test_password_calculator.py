import pytest
from password_calculator import calculate_combinations

def test_calculate_combinations():
    result = calculate_combinations(8, True, True, True)
    assert result == 218340105584896
