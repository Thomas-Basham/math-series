from math_series.series import fibonacci
from math_series.series import lucas


def test_fibonacci_zero():
    assert fibonacci(0) == 0


def test_fibonacci_one():
    assert fibonacci(1) == 0


def test_fibonacci_two():
    assert fibonacci(2) == 1


def test_fibonacci_three():
    assert fibonacci(3) == 1


def test_fibonacci_four():
    assert fibonacci(4) == 2


def test_fibonacci_five():
    assert fibonacci(5) == 3


def test_lucas_zero():
    assert lucas(0) == 2


def test_lucas_one():
    assert lucas(1) == 2


def test_lucas_two():
    assert lucas(2) == 1


def test_lucas_three():
    assert lucas(3) == 3


def test_lucas_four():
    assert lucas(4) == 4
