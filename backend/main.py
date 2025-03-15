from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

class BoardState(BaseModel):
    board: list

def check_winner(board):
    """Check for a winner in the Tic-Tac-Toe game."""
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            return row[0]

    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            return board[0][col]

    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        return board[0][2]

    return None  # No winner yet

def get_ai_move(board):
    """Simple AI move (random empty spot)."""
    for i in range(3):
        for j in range(3):
            if board[i][j] == "":
                return (i, j)
    return None  # Board full

@app.post("/check-winner/")
async def check_winner_api(board_data: BoardState):
    winner = check_winner(board_data.board)
    return {"winner": winner}

@app.post("/ai-move/")
async def ai_move_api(board_data: BoardState):
    move = get_ai_move(board_data.board)
    return {"move": move}
