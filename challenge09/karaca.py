VOWELS = ["a", "e", "i", "o", "u"]
print(
    "".join(
        str(VOWELS.index(i)) if i in VOWELS else i
        for i in input("Enter text: ").lower()[::-1]
    )
    + "aca"
)
