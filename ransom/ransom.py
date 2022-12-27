import collections


def can_build(string1: str, string2: str) -> bool:
    count = collections.Counter(string1)
    for char in string2:
        if not count.get(char, 0):
            return False
        count[char] -= 1
    return True


tests = [
    ("aPPleAL", "PAL", True),
    ("aPPleAL", "apple", False),
    ("a", "", True),
    ("aa", "aaa", False),
]
for test in tests:
    assert can_build(*test[:2]) == test[-1]
