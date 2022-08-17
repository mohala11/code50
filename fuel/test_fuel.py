import pytest
from fuel import convert, gauge


def test_value():
    with pytest.raises(ValueError):
        convert("cat/dog")


def test_zero():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")


def 