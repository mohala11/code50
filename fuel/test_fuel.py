import pytest
from fuel import convert, gauge


def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def test_ok():
    assert convert("1/4") == 25 and gauge(25) == "25%"
    assert convert()