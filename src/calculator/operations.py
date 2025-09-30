"""
Basic arithmetic operations for the calculator.

This module provides elementary math functions for the calculator application.
"""


def add(a, b):
    """
    Add two numbers and return the result.

    Args:
        a: First number
        b: Second number

    Returns:
        The sum of a and b
    """
    return a + b


def subtract(a, b):
    """
    Subtract b from a and return the result.

    Args:
        a: Number to subtract from
        b: Number to subtract

    Returns:
        The difference (a - b)
    """
    return a - b


def multiply(a, b):
    """Multiply two numbers and return the result."""
    return a * b


def divide(a, b):
    """
    Divide a by b and return the result.

    Args:
        a: The dividend
        b: The divisor

    Returns:
        The quotient a/b

    Raises:
        ZeroDivisionError: If b is 0
    """
    if b == 0:
        raise ZeroDivisionError("Cannot divide by zero")
    return a / b
