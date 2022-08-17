from bank import value


def test_value_hello():
    assert value("hello") == 0
    assert value("hello, i'm David") == 0
    assert value("HELLO") == 0


def test_value_h():
    assert value("hi") == 20
    assert value("hihao") == 20
    assert value("hallo, dude") == 20
    assert value("HALLO, DUDE") == 20


def test_value_any():
    assert value("74287419784") == 100
    assert value("NIHAO") == 100
    assert value("nihao") == 100
    assert value("shdhfakjfja") == 100
