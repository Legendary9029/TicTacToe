import random

def check_winner(board):
    """Check if there's a winner or if the game is a draw."""
    winning_combinations = [
        [(0, 0), (0, 1), (0, 2)],
        [(1, 0), (1, 1), (1, 2)],
        [(2, 0), (2, 1), (2, 2)],
        [(0, 0), (1, 0), (2, 0)],
        [(0, 1), (1, 1), (2, 1)],
        [(0, 2), (1, 2), (2, 2)],
        [(0, 0), (1, 1), (2, 2)],
        [(0, 2), (1, 1), (2, 0)]
    ]

    for combo in winning_combinations:
        a, b, c = combo
        if board[a[0]][a[1]] == board[b[0]][b[1]] == board[c[0]][c[1]] and board[a[0]][a[1]] in ["X", "O"]:
            return board[a[0]][a[1]]

    if all(board[i][j] in ["X", "O"] for i in range(3) for j in range(3)):
        return "Draw"

    return None

def get_available_moves(board):
    """Return a list of available moves."""
    return [(i, j) for i in range(3) for j in range(3) if board[i][j] == ""]

def ai_move(board, difficulty="medium"):
    """AI move based on difficulty level."""
    if difficulty == "easy":
        return random.choice(get_available_moves(board))

    if difficulty == "medium":
        return medium_ai(board)

    if difficulty == "hard":
        return minimax_ai(board)

def medium_ai(board):
    """Medium AI that blocks the opponent and tries to win."""
    for mark in ["O", "X"]:
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = mark
            if check_winner(board) == mark:
                board[i][j] = ""  # Undo move
                return move
            board[i][j] = ""  # Undo move

    return random.choice(get_available_moves(board))

def minimax(board, is_maximizing):
    """Minimax algorithm for unbeatable AI."""
    winner = check_winner(board)
    if winner == "O":
        return 1
    if winner == "X":
        return -1
    if winner == "Draw":
        return 0

    if is_maximizing:
        best_score = -float("inf")
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = "O"
            score = minimax(board, False)
            board[i][j] = ""
            best_score = max(best_score, score)
        return best_score
    else:
        best_score = float("inf")
        for move in get_available_moves(board):
            i, j = move
            board[i][j] = "X"
            score = minimax(board, True)
            board[i][j] = ""
            best_score = min(best_score, score)
        return best_score

def minimax_ai(board):
    """Find the best move using Minimax."""
    best_score = -float("inf")
    best_move = None

    for move in get_available_moves(board):
        i, j = move
        board[i][j] = "O"
        score = minimax(board, False)
        board[i][j] = ""
        if score > best_score:
            best_score = score
            best_move = move

    return best_move
