from bugy import divide


def test_divide_returns_int():
    result = divide(10, 2)
    assert isinstance(result, int)
    assert result == 5