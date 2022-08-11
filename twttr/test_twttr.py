from twttr import convert


def convert_only_letters():
    assert convert("my name is Vitaly") == "m nm s Vtly"
    assert convert("my wife's name in Nataly") == "m wf's nm s Ntly"

def converts_letters_and_numbers()