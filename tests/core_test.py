import pytest

from src.core_logic import detect_winner, is_valid_move, mark_winner


@pytest.mark.parametrize(
    "row,col,expected",
    [(5, 0, True), (4, 0, False)],
)
def test_is_valid_move(row, col, expected):
    board = [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 1, 0, 0],
        [0, 0, 0, 1, 2, 0, 0],
        [0, 0, 2, 2, 1, 0, 0],
        [0, 0, 1, 1, 2, 0, 0],
    ]
    assert is_valid_move(board, row, col) == expected


@pytest.mark.parametrize(
    "board,expected",
    (
        # (
        #     [
        #         [0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 1, 0, 0, 0],
        #         [0, 0, 0, 1, 2, 0, 0],
        #         [0, 0, 0, 1, 2, 0, 0],
        #         [0, 0, 0, 1, 2, 0, 0]
        #     ],
        #     1,
        # ),
        (
            [
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, 0, 0, 0],
                [0, 2, 0, 1, 0, 0, 0],
                [0, 2, 0, 1, 0, 0, 0],
                [0, 2, 0, 1, 0, 0, 0],
            ],
            1,
        ),
    ),
)
def test_detect_winner(board, expected):
    assert detect_winner(board) == expected


@pytest.mark.parametrize(
    "board,winner,expected",
    (
        # (
        #     [
        #         [0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 1, 0, 0],
        #         [0, 0, 0, 1, 2, 0, 0],
        #         [0, 0, 1, 2, 1, 0, 0],
        #         [0, 1, 1, 1, 2, 0, 0]
        #     ],
        #     1,
        #     [
        #         [0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 0, 0, 0],
        #         [0, 0, 0, 0, 3, 0, 0],
        #         [0, 0, 0, 3, 2, 0, 0],
        #         [0, 0, 3, 2, 1, 0, 0],
        #         [0, 3, 1, 1, 2, 0, 0]
        #     ]
        # ),
        # winner right down
        (
            [
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [2, 0, 2, 0, 0, 0, 0],
                [1, 0, 1, 2, 0, 0, 0],
                [2, 0, 2, 1, 2, 0, 0],
                [1, 0, 1, 2, 1, 2, 0],
            ],
            2,
            [
                [0, 0, 0, 0, 0, 0, 0],
                [1, 0, 0, 0, 0, 0, 0],
                [2, 0, 3, 0, 0, 0, 0],
                [1, 0, 1, 3, 0, 0, 0],
                [2, 0, 2, 1, 3, 0, 0],
                [1, 0, 1, 2, 1, 3, 0],
            ],
        ),
    ),
)
def test_mark_winner(board, winner, expected):
    mark_winner(board, winner)
    assert board == expected
