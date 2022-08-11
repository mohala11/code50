from twttr import convert


def test_convert_only_letters():
    assert convert("my name is Vitaly") == "my nm s Vtly"
    assert convert("my wife's name is Nataly") == "my wf's nm s Ntly"


def test_converts_letters_and_numbers():
    assert convert("Boing 747") == "Bng 747"
    assert convert("I am 30 years old") == " m 30 yrs ld"


def test_convert_only_numbers():
    assert convert("412874187941") == "412874187941"