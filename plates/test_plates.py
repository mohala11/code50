from plates import is_valid


def test_correct_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS531") == True
    assert is_valid("CSS550") == True


def test_zerofirstnumber():
    assert is_valid("CS05") == False
    assert is_valid("CSS000") == False


def 



