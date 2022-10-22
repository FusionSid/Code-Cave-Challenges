import re


def haiku(text: str) -> bool:
    text = text.lower()

    lines = text.split("\n")

    if lines != 3:
        print("Bad skill issue only 3 allowed")

    lines = [line.strip() for line in lines]

    lines_counts = []

    for line in lines:
        words = line.split(" ")
        vowel_count = 0
        for word in words:
            vovels = re.findall("[aeiouy]+", word)
            if word.endswith("e") and len(vovels) > 1:
                vowel_count -= 1
            vowel_count += len(vovels)
        lines_counts.append(vowel_count)
    print(lines_counts)
    if lines_counts[0] == 5 and lines_counts[1] == 7 and lines_counts[2] == 5:
        return True
    return False


print(
    haiku("Delightful display \n Snowdrops bow their pure white heads \n To the sun's glory")
)
