import pytest
from fuel import convert, gauge


def test_letters():
    with pytest.raises(ValueError):
        convert()
