from twttr import convert


def convert_only_letters():
    assert convert("my name is Vitaly") == "m nm s Vtly"
    assert convert("my wife's name in Nataly") == "m wf's nm s Ntly"


def converts_letters_and_numbers():
    assert convert("Boing 747") == "Bng 747"
    assert convert("I am 30 years old") == "m 30 yrs ld"


def convert_only_numbers():
    assert convert("412874187941") == "412874187941"