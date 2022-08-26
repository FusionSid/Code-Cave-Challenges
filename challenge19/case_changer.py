import re


def toCamelCase(text: str) -> str:
    text = text.split("_")
    for idx, i in enumerate(text):
        if idx == 0:
            continue

        text[idx] = i.capitalize()

    return "".join(text)


def to_snake_case(text: str) -> str:
    return re.sub(r"(?<!^)(?=[A-Z])", "_", text).lower()


print(toCamelCase("hello_edabit"))
print(to_snake_case("helloEdabit"))
