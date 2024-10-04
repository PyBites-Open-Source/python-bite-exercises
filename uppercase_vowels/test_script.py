from script import uppercase_vowels


def test_uppercase_vowels_simple():
    assert uppercase_vowels("abCDefghijkl") == "AbcdEfghIjkl"
    assert uppercase_vowels("This test should pass itself") == "ThIs tEst shOUld pAss ItsElf"
    assert uppercase_vowels("data.jpg foul") == "dAtA jpg fOUl"

def test_uppercase_vowels_punctuation():
    assert uppercase_vowels(".") == " "
    assert uppercase_vowels("-,.?~a") == "     A"
    assert uppercase_vowels("_.aBCEDF") == "  AbcEdf"

def test_uppercase_vowels_files():
    assert uppercase_vowels("sample.mp3") == "sAmplE.mp3"
    assert uppercase_vowels("MUSIC.jpeg") == "musIc.jpeg"
    assert uppercase_vowels("what is file.pdf") == "whAt Is fIlE.pdf"
