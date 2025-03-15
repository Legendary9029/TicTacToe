from fastapi import FastAPI
from pydantic import BaseModel
from backend.game_logic import check_winner, ai_move  # Import from game_logic.py

app = FastAPI()

# Store difficulty level globally (default: "medium")
current_difficulty = "medium"


class BoardState(BaseModel):
    board: list


class DifficultyLevel(BaseModel):
    level: str


@app.post("/set-difficulty/")
async def set_difficulty(difficulty_data: DifficultyLevel):
    """API to change AI difficulty level."""
    global current_difficulty
    if difficulty_data.level.lower() not in ["easy", "medium", "hard"]:
        return {"error": "Invalid difficulty level. Choose from 'easy', 'medium', or 'hard'."}

    current_difficulty = difficulty_data.level.lower()
    return {"message": f"Difficulty set to {current_difficulty}"}


@app.post("/check-winner/")
async def check_winner_api(board_data: BoardState):
    """API to check if there's a winner."""
    winner = check_winner(board_data.board)
    return {"winner": winner}


@app.post("/ai-move/")
async def ai_move_api(board_data: BoardState):
    """API for AI move based on difficulty."""
    move = ai_move(board_data.board, difficulty=current_difficulty)
    return {"move": move}
