def nearest_vowel(letter: str) -> str:
    return "aaaeeeeiiiiioooooouuuuuyyy"[ord(letter) - 97]


# testing
assert nearest_vowel("b") == "a"
assert nearest_vowel("s") == "u"
assert nearest_vowel("c") == "a"
assert nearest_vowel("i") == "i"
