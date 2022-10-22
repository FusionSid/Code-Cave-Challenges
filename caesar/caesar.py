import string

text = input("Enter the text: ")
shift = int(input("Enter the shift amount: "))
shift = shift % 26

alphabet = string.ascii_lowercase
shifted_alphabet = alphabet[shift:] + alphabet[:shift]

table = str.maketrans(alphabet, shifted_alphabet)

print(f"Encrypted Text: {text.translate(table)}")
