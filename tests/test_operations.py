"""Tests for calculator operations."""

import pytest

from src.calculator.operations import add, divide, multiply, subtract   

def test_add():
    """Test the add function."""
    assert add(1, 2) == 3
    assert add(-1, 1) == 0
    assert add(0, 0) == 0


def test_subtract():
    """Test the subtract function."""
    assert subtract(3, 2) == 1
    assert subtract(2, 3) == -1
    assert subtract(0, 0) == 0


def test_multiply():
    """Test the multiply function."""
    assert multiply(2, 3) == 6
    assert multiply(-2, 3) == -6
    assert multiply(0, 5) == 0


def test_divide():
    """Test the divide function."""
    assert divide(6, 3) == 2
    assert divide(5, 2) == 2.5
    assert divide(-6, 2) == -3


def test_divide_by_zero():
    """Test that dividing by zero raises an exception."""
    with pytest.raises(ZeroDivisionError):
        divide(1, 0)


@pytest.mark.parametrize(
    "a, b, expected", [(1, 2, 3), (0, 0, 0), (-1, 1, 0), (100, -100, 0)]
)
def test_add_parameterized(a, b, expected):
    """Test add function with multiple inputs."""
    assert add(a, b) == expected


@pytest.mark.parametrize(
    "a, b, expected", [(5, 2, 3), (0, 0, 0), (1, 1, 0), (-1, -1, 0)]
)
def test_subtract_parameterized(a, b, expected):
    """Test subtract function with multiple inputs."""
    assert subtract(a, b) == expected


def test_add_large_numbers():
    """Test addition with large numbers."""
    assert add(10**10, 10**10) == 2 * 10**10


def test_subtract_identical_numbers():
    """Test subtraction of identical numbers always gives zero."""
    assert subtract(100, 100) == 0
    assert subtract(-42, -42) == 0


def test_multiply_by_zero():
    """Test that multiplying by zero always gives zero."""
    assert multiply(5, 0) == 0
    assert multiply(0, 5) == 0
    assert multiply(0, 0) == 0
