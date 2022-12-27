def eval_algebra(expression: str) -> int:
    expression = expression.split(" ")
    a = expression[0]
    b = expression[1], expression[2]
    answer = expression[-1]

    if answer == "x":
        b = int(b[1]) if b[0] == "+" else -int(b[1])
        return int(a) + b
    elif a == "x":
        b = int(b[1]) if b[0] == "-" else -int(b[1])
        return int(answer) + b
    elif b[1] == "x":
        result = int(answer) + (int(a) * -1)
        return result if b[0] == "+" else result * -1


# test cases
print(eval_algebra("2 + x = 19"))
print(eval_algebra("4 - x = 1"))
print(eval_algebra("23 + 1 = x"))
print(eval_algebra("x - 2 = 5"))
