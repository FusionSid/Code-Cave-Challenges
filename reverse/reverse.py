text = input("Enter text: ")
print("".join(i.swapcase() if i.isalpha() else i for i in text[::-1]))
