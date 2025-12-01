from ..app import add, is_even

def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(0, 0) == 0
    assert add(-1, 1) == 0

def test_add_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-10, 5) == -5

def test_is_even():
    assert is_even(0) is True
    assert is_even(2) is True
    assert is_even(-4) is True
    assert is_even(1) is False
    assert is_even(-3) is False
