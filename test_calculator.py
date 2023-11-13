from calculator import square
import pytest
# docs.pytest.org
# pip install pytest
# pytest test_calculator.py

# 6:47:15 Harvard CS50’s Introduction to Programming with Python – Full University Course

def test_positive():
    assert square(2) == 4
    assert square(3) == 9

def test_negative():
    assert square(-2) == 4
    assert square(-3) == 9

def test_zero():
    assert square(0) == 0

# Allow the execption to be raised
def test_str():
    with pytest.raises(TypeError):
        square("cat")
    