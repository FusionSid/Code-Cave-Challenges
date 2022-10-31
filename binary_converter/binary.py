def to_binary(number: int) -> str:
    output = ""
    while number > 0:
        output += str(number % 2)
        number //= 2
    return "0" + output[::-1]


def adder(a: int, b: int, c: int) -> tuple:
    half = lambda a, b: (a and b, a ^ b)
    x, y = half(c, a)
    x2, y2 = half(y, b)
    return x or x2, y2


def negative(binary_number: str) -> str:
    inverted = "".join(str(int(not int(i))) for i in binary_number)
    add = "0" * (len(inverted) - 1) + "1"
    negative = ""

    carry = 0
    for i in range(len(inverted)):
        carry, sum = adder(int(inverted[::-1][i]), int(add[::-1][i]), carry)
        negative += str(sum)

    return negative[::-1]


number = int(input("Enter number to convert: "))

binary_number = to_binary(number)
print(f"Number in binary is: ", binary_number)

negative_number = negative(binary_number)
print("The number as a negative is:", negative_number)