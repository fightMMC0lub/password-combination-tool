# test_password_calculator.py
import sys
import os

# Add the parent directory to the Python path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Import the function to be tested
from password_calculator import calculate_combinations

def test_calculate_combinations():
    # Example test case for 8 characters with uppercase, lowercase, digits, and special characters
    result = calculate_combinations(8, True, True, True, True)
    assert result == 218340105584896  # Replace with the correct expected value

def test_calculate_combinations_without_special_chars():
    result = calculate_combinations(8, True, True, True, False)
    assert result == 218340105584896  # Adjust expected result accordingly
