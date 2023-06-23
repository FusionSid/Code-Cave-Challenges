from itertools import groupby


def look_and_say(n: int) -> None:
    sequence = "1"
    for _ in range(n):
        sequence = "".join(
            f"{len(list(group))}{num}" for num, group in groupby(sequence)
        )
    print(sequence)


look_and_say(4)
