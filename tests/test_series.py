from math_series.series import lucas, fibonacci, sum_series


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
    assert lucas(0, 2, 1) == 2


def test_lucas_one():
    assert lucas(1, 2, 1) == 2


def test_lucas_two():
    assert lucas(2, 2, 1) == 1


def test_lucas_three():
    assert lucas(3, 2, 1) == 3


def test_lucas_four():
    assert lucas(4, 2, 1) == 4


def test_sum_series_fib():
    assert sum_series(7) == 8


def test_sum_series_lucas():
    assert sum_series(7, 2, 1) == 18
