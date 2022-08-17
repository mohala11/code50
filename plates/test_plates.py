from plates import is_valid


def test_correct_plates():
    assert is_valid("CS50") == True
    assert is_valid("CS531") == True
    assert is_valid("CSS550") == True


def test_zerofirstnumber():
    assert is_valid("CS05") == False
    assert is_valid("CSS000") == False


def test_punctuation():
    assert is_valid("CS.50") == False
    assert is_valid("PT,03") == False


def test_letter_after_number():
    assert is_valid("CS50A") == False
    assert is_valid("CSS5AS") == False


def test_noletters_nonumbers():
    assert is_valid("CSDA") == True
    assert is_valid("3124") == False


def test_lenght():
    assert is_valid("CS50") == True
    assert is_valid("CSSSSSS67523525368238578238752") == False




