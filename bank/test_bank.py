from bank import value


def test_value_hello():
    assert value("hello") == "$0"
    assert value("HELLO") == "$0"
    assert value("Hello, i'm David") == "$0"

def test_value_h():
    assert value 