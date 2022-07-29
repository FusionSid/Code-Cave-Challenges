def wordrank(text: str) -> str:
    text = text.upper().replace(".", "")
    words = dict(zip(text.split(), [0 for i in range(len(text))]))
    for key in words:
        total = 0
        for char in key:
            total += ord(char) - 64
        words[key] = total
    word = sorted(words)[0].lower()
    return word


print(wordrank("The quick brown fox."))
