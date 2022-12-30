import itertools


def checklist(array: list[int] | tuple[int]):
    return sorted(array) == list(range(1, 10))


def validate(grid: list[list[int]]) -> bool:
    # check rows
    for row in grid:
        if not checklist(row):
            return False

    # check columns
    for column in list(zip(*grid)):
        if not checklist(column):
            return False

    # 3x3 boxes:
    threes = [[row[i : i + 3] for i in range(0, len(row), 3)] for row in grid]
    three_boxes = zip(*threes)

    for _3boxes in three_boxes:
        boxes = [_3boxes[i : i + 3] for i in range(0, len(_3boxes), 3)]
        for box in boxes:
            if not checklist(list(itertools.chain(*box))):
                return False

    # must be good then
    return True


tests = [
    (
        [
            [1, 5, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, 4],
        ],
        True,
    ),
    (
        [
            [1, 1, 2, 4, 8, 9, 3, 7, 6],
            [7, 3, 9, 2, 5, 6, 8, 4, 1],
            [4, 6, 8, 3, 7, 1, 2, 9, 5],
            [3, 8, 7, 1, 2, 4, 6, 5, 9],
            [5, 9, 1, 7, 6, 3, 4, 2, 8],
            [2, 4, 6, 8, 9, 5, 7, 1, 3],
            [9, 1, 4, 6, 3, 7, 5, 8, 2],
            [6, 2, 5, 9, 4, 8, 1, 3, 7],
            [8, 7, 3, 5, 1, 2, 9, 6, 4],
        ],
        False,
    ),
]
for test, answer in tests:
    assert validate(test) == answer
