KNIGHT = 1
K_MOVES_X = [(2, 1), (-2, 1), (2, -1), (-2, -1)]
K_MOVES_Y = [(1, 2), (2, -1), (-2, 1), (-2, -1)]
ALL_KNIGHTS_MOVES = K_MOVES_X + K_MOVES_Y


def cannot_capture(board: list[list[int]]) -> bool:
    knight_positions = []
    for iy, y in enumerate(board):
        for ix, x in enumerate(board[iy]):
            if x == KNIGHT:
                knight_positions.append((ix, iy))

    for knight in knight_positions:
        for move in ALL_KNIGHTS_MOVES:
            x, y = move
            kx, ky = knight
            try:
                if board[x + kx][y + ky] == KNIGHT:
                    print(
                        f"Knight on ({x}, {y}) can capture knight on ({kx}, {ky}). Skill issue ngl"
                    )
                    return False
            except IndexError:
                pass  # cant move there probs cause its out of board
    return True


tests = [
    [
        [0, 0, 0, 1, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 1, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 1],
        [0, 0, 0, 0, 1, 0, 0, 0],
    ],
    [
        [1, 0, 1, 0, 1, 0, 1, 0],
        [0, 1, 0, 1, 0, 1, 0, 1],
        [0, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 1, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 0, 0, 1, 0, 1],
        [1, 0, 0, 0, 1, 0, 1, 0],
        [0, 0, 0, 1, 0, 1, 0, 1],
    ],
]
for test in tests:
    print(cannot_capture(test))
