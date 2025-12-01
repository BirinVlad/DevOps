import pytest
from app import add, is_even

@pytest.fixture
def sample_numbers():
    return [2, 4, 6, 8, 10, 0, -2, -4]

def test_add():
    # Test basic addition
    assert add(2, 3) == 5
    # Test adding zeros
    assert add(0, 0) == 0
    # Test adding negative numbers
    assert add(-1, 1) == 0
    assert add(-5, -3) == -8
    # Test adding with zero
    assert add(10, 0) == 10

def test_all_even(sample_numbers):
    """Test that all numbers in the sample_numbers fixture are even"""
    for n in sample_numbers:
        assert is_even(n), f"Expected {n} to be even"

@pytest.mark.parametrize("value, expected", [
    (0, True),     # zero is even
    (2, True),     # positive even
    (42, True),    # another positive even
    (-4, True),    # negative even
    (1, False),    # positive odd
    (-3, False),   # negative odd
    (999, False),  # large odd
    (1000, True)   # large even
])
def test_is_even(value, expected):
    assert is_even(value) == expected
