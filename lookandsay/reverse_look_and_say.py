from itertools import groupby


def reverse_look_and_say(sequence: str) -> str:
    return "".join(
        int(group[0]) * group[1]
        for group in [list(sequence[i : i + 2]) for i in range(0, len(sequence), 2)]
    )


def look_and_say() -> None:
    sequence = "1"
    while True:
        past_sequence = sequence
        sequence = "".join(
            f"{len(list(group))}{num}" for num, group in groupby(sequence)
        )
        assert reverse_look_and_say(sequence) == past_sequence


# testing
look_and_say()
