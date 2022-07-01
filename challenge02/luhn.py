card_number = input("Enter a 16 digit card number: ")
card_number = card_number.replace(" ", "")

if len(card_number) != 16 or not card_number.isnumeric():
    print("Card number must be 16 digits")
    quit(0)

pattern = [2, 1]

total = 0

for index, item in enumerate(card_number):
    multiply_amount = pattern[(index % 2)]
    result = int(item) * multiply_amount

    if result > 9:
        result = str(result)
        result = int(result[0]) + int(result[1])

    total += result

if total % 10 == 0:
    print("Valid")
else:
    print("Invalid")
