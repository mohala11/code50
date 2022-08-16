from bank import value


def test_value_hello():
    assert value("hello") == 0
    assert value("HELLO") == 0
    assert value("Hello, i'm David") == 0


def test_value_h():
    assert value("Hi") == "$20"
    assert value("Hihao") == "$20"
    assert value("Hallo, dude") == "$20"


def test_value_any():
    assert value("74287419784") == "$100"
    assert value("Nihao") == "$100"
    assert value("shdhfakjfja") == "$100"
