def base64_encode(text: str, hex: bool = False) -> str:
    BASE_64_ALPHABET = (
        "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789+/"
    )

    # convert entire thing to binary
    binary = (
        "{:08b}".format(int(bytes.fromhex(text).hex(), 16))
        if hex
        else "".join(format(ord(i), "08b") for i in text)
    )

    # split into 6 bit chunks
    chunks = [[j for j in binary[i : i + 6]] for i in range(0, len(binary), 6)]

    # convert all binary numbers to base10 for array index
    chunks = [
        int("".join(i), base=2)
        if len(i) == 6
        else int("".join(i) + ("0" * (6 - len(i))), base=2)
        for i in chunks
    ]

    # encoded result without any padding yet
    pre_padding = "".join(BASE_64_ALPHABET[i] for i in chunks)

    # add final padding to make the length a multiple of 4
    padding = abs(len(pre_padding) - (4 * round(len(pre_padding) / 4))) * "="

    return pre_padding + padding


def test():
    """
    Generate random strings and pass them through my encoder
    if the encoded result matches the result produced by the
        official built in library the text is successful!
    """
    import base64
    import random
    import string

    for _ in range(100):
        testing_string = "".join(
            [
                random.choice(string.ascii_letters + string.punctuation + string.digits)
                for _ in range(random.randint(0, 100))
            ]
        )
        assert base64.b64encode(testing_string.encode()).decode() == base64_encode(
            testing_string
        )


test()
print(base64_encode("deadbeef", hex=True))  # -> 3q2+7w==
