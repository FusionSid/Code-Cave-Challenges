def isbn13(number: str) -> bool:
    _sum = 0
    one_three = "".join("3" if i % 2 else "1" for i in range(len(number)))
    for i in range(len(number)):
        if number[i] == "X":
            _sum += 10 * int(one_three[i])
            continue
        _sum += int(number[i]) * int(one_three[i])
    return _sum % 10 == 0


def isbn10(number: str, convert: bool = False) -> (str | bool):
    if convert:
        number = "978" + number
        for i in range(10):
            number = number[:-1] + (str(i) if i != 10 else "X")
            if isbn13(number):
                return number

    _sum = 0
    numbers = list(str(10 - i) for i in range(len(number)))
    for i in range(len(number)):
        if number[i] == "X":
            _sum += 10 * int(numbers[i])
            continue
        _sum += int(number[i]) * int(numbers[i])

    return _sum % 11 == 0


def validate_number(number: str) -> str:
    if not isbn10(number) and not isbn13(number):
        return "Invalid"
    if isbn13(number):
        return "Valid"
    return isbn10(number, convert=True)  # type: ignore


print(isbn13("9780316066525"))
print(isbn13("0330301824"))
print(validate_number("0316066524"))
