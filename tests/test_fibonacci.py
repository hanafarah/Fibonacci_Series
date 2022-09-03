# pylint: disable=missing-docstring
"""
The test module for Fibonancci
It is a total of 7 test cases
"""
import pytest
from fibonacci import Fibonacci


def test_fibonacci_value_not_int():
    """
    If constructed with a value other than an integer
    Fibonacci constuctor should raise a ValueError.
    """
    with pytest.raises(ValueError):
        Fibonacci("123Y")


def test_fibonacci_value_of_0():
    """
    If constructed with a value of 0, the iterator should produce the values [0] as a list.

    """
    for num in Fibonacci(0):
        assert num == [0]


def test_fibonacci_value_of_1():
    """
    If constructed with a value of 0, the iterator should produce the values [0, 1] as a list.

    """
    assert list(Fibonacci(1)) == [1]


def test_fibonacci_value_of_2():
    """
    If the value is 2, the iterator should produce the values [0, 1, 1].

   """
    assert list(Fibonacci(2)) == [1, 1]


def test_fibonacci_value_of_4():
    """
    If constructed with a value of 4, the iterator should produce the

    values [0, 1, 1, 2, 3] if cast as a list.

    """
    assert list(Fibonacci(4)) == [1, 1, 2, 3]


def test_fibonacci_value_of_10():
    """
    If constructed with a value of 10, the iterator should

    produce the values [0, 1, 1, 3, 5, 8, 13, 21, 34, 55] if cast as a list.

    """

    assert list(Fibonacci(10)) == [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_fibonacci_negative_value():
    """
    Given a negative value, the iterator should produce an empty list.

    """
    with pytest.raises(ValueError):
        raise ValueError(-100)
