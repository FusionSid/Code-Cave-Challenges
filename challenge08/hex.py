convert = lambda text: " ".join("{:02x}".format(ord(char)) for char in text)
print(f"Converted Text: {convert(input('Enter some text: '))}")
