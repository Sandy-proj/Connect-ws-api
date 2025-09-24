from datetime import datetime, timezone

from ..constants import M, N, PlayerEnum
from ..core_logic import calculate_row_by_col, detect_winner, mark_winner
from .models import Game


def make_move(
    game: Game,  # type: ignore[arg-type]
    col: int,  # type: ignore[union-attr]
) -> None:
    row = calculate_row_by_col(game.board, col)
    if row is None:
        return
    game.board[row][col] = game.next_player_to_move_sign
    game.move_number += 1

    # Check if this is the winning move.
    winner = detect_winner(game.board)
    if winner:
        mark_winner(game.board, winner)
        game.winner = PlayerEnum(winner)
        game.finished_at = datetime.now(timezone.utc)
    elif game.move_number == N * M + 1:
        game.winner = None
        game.finished_at = datetime.now(timezone.utc)
