import itertools
from typing import Optional


class Sudoku:
    def __init__(self, game: str) -> None:
        __game: list[int] = list(map(int, game))

        # check if the user is being a bitch and gave invalid input
        if len(__game) != 81:
            raise ValueError(
                "game string input must be 81 chars in length (skill issue)"
            )

        self.board = [__game[i : i + 9] for i in range(0, len(__game), 9)]

    def get_row(self, row_number: int) -> list[int]:
        try:
            row = self.board[row_number]
        except IndexError:
            raise ValueError(
                "Invalid Input: The row number must be an integer from 0-8 (inclusive)"
            )
        return row

    def get_col(self, column_number: int) -> list[int]:
        columns = list(zip(*self.board))
        try:
            column = list(columns[column_number])
        except IndexError:
            raise ValueError(
                "Invalid Input: The column number must be an integer from 0-8 (inclusive)"
            )
        return column

    def get_sqr(self, n: int, m: Optional[int] = None) -> list[int]:
        boxes = self.__get_boxes()

        if m is None:
            try:
                box = list(boxes[n])
            except IndexError:
                raise ValueError(
                    "Invalid Input: The box number must be an integer from 0-8 (inclusive)"
                )
            return box

        boxes = [boxes[i : i + 3] for i in range(0, len(boxes), 3)]
        return boxes[n // 3][m // 3]

    def __get_boxes(self) -> list[list[int]]:
        # this functions code is so fucking sketchy
        boxes = []

        # get all boxes
        rows_in_three = [
            [row[i : i + 3] for i in range(0, len(row), 3)] for row in self.board
        ]
        cols_in_three = zip(*rows_in_three)

        for three_boxes in cols_in_three:
            boxes_split = [
                three_boxes[i : i + 3] for i in range(0, len(three_boxes), 3)
            ]
            for split_box in boxes_split:
                box = list(itertools.chain(*split_box))
                boxes.append(box)

        # reorder boxes so left-right, top-bottom
        reordered_boxes: list[list[int]] = list(
            itertools.chain(*zip(*[boxes[i : i + 3] for i in range(0, len(boxes), 3)]))
        )
        return reordered_boxes


game = Sudoku(
    "417950030000000700060007000050009106800600000000003400900005000000430000200701580"
)
assert game.board == [
    [4, 1, 7, 9, 5, 0, 0, 3, 0],
    [0, 0, 0, 0, 0, 0, 7, 0, 0],
    [0, 6, 0, 0, 0, 7, 0, 0, 0],
    [0, 5, 0, 0, 0, 9, 1, 0, 6],
    [8, 0, 0, 6, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 4, 0, 0],
    [9, 0, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 4, 3, 0, 0, 0, 0],
    [2, 0, 0, 7, 0, 1, 5, 8, 0],
]
assert game.get_row(0) == [4, 1, 7, 9, 5, 0, 0, 3, 0]
assert game.get_col(8) == [0, 0, 0, 6, 0, 0, 0, 0, 0]
assert game.get_sqr(1) == [9, 5, 0, 0, 0, 0, 0, 0, 7]
assert game.get_sqr(1, 8) == [0, 3, 0, 7, 0, 0, 0, 0, 0]
assert game.get_sqr(8, 3) == [0, 0, 5, 4, 3, 0, 7, 0, 1]
