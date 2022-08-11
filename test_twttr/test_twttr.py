from twttr import shorten


def test_shorten_only_letters():
    assert shorten("my name is Vitaly") == "my nm s Vtly"
    assert shorten("my wife's name is Nataly, she is beatifull") == "my wf's nm s Ntly, sh s btfll"


def test_shorten_letters_and_numbers():
    assert shorten("Boing 747") == "Bng 747"
    assert shorten("I am 30 years old") == " m 30 yrs ld"


def test_shorten_only_numbers():
    assert shorten("412874187941") == "412874187941"