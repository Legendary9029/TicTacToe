import streamlit as st
import requests  # For API communication

API_URL = "http://127.0.0.1:8000"  # Local FastAPI server

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [["", "", ""], ["", "", ""], ["", "", ""]]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None
    st.session_state.mode = "AI"  # Default mode: AI
    st.session_state.moves = 0
    st.session_state.pending_ai_move = False  # Ensures AI move triggers after rerun
    st.session_state.difficulty = "Medium"  # Default AI difficulty

# Check game state using API
def check_game_state():
    response = requests.post(f"{API_URL}/check-winner/", json={"board": st.session_state.board})
    winner = response.json().get("winner")
    if winner:
        st.session_state.game_over = True
        st.session_state.winner = winner
    elif st.session_state.moves == 9:
        st.session_state.game_over = True
        st.session_state.winner = "Draw"

# AI Move using API
def ai_play():
    if st.session_state.current_player == "O" and not st.session_state.game_over and st.session_state.mode == "AI":
        response = requests.post(
            f"{API_URL}/ai-move/",
            json={"board": st.session_state.board, "difficulty": st.session_state.difficulty.lower()}
        )
        move = response.json().get("move")
        if move:
            i, j = move
            st.session_state.board[i][j] = "O"
            st.session_state.moves += 1
            check_game_state()
            if not st.session_state.game_over:
                st.session_state.current_player = "X"
            st.session_state.pending_ai_move = False  # AI move completed
            st.rerun()

# Reset Game
def reset_game():
    st.session_state.board = [["", "", ""], ["", "", ""], ["", "", ""]]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None
    st.session_state.moves = 0
    st.session_state.pending_ai_move = False  # Reset AI move flag

# UI
st.title("🎮 Tic-Tac-Toe AI 🤖")

# Game Mode Selection
mode = st.radio("Select Mode:", ["AI", "Player vs Player"], index=0)
st.session_state.mode = "AI" if mode == "AI" else "PvP"

# AI Difficulty Selection (Only if playing against AI)
if st.session_state.mode == "AI":
    difficulty = st.selectbox("Select AI Difficulty:", ["Easy", "Medium", "Hard"], index=1)
    st.session_state.difficulty = difficulty

st.markdown(f"### 🟢 Turn: **{st.session_state.current_player}**")

# Display Board
board_placeholder = st.empty()
with board_placeholder.container():
    for i in range(3):
        cols = st.columns(3)
        for j in range(3):
            button_text = st.session_state.board[i][j] or " "
            button_color = "#ffcccc" if button_text == "X" else "#ccffcc" if button_text == "O" else "#f5f5f5"
            if cols[j].button(button_text, key=f"{i}-{j}", help="Click to play", use_container_width=True):
                if not st.session_state.game_over and st.session_state.board[i][j] == "":
                    st.session_state.board[i][j] = st.session_state.current_player
                    st.session_state.moves += 1
                    check_game_state()
                    if not st.session_state.game_over:
                        if st.session_state.mode == "AI":
                            st.session_state.current_player = "O"  # Switch to AI
                            st.session_state.pending_ai_move = True  # Trigger AI next cycle
                        else:
                            st.session_state.current_player = "O" if st.session_state.current_player == "X" else "X"
                    st.rerun()

# Display Winner
if st.session_state.game_over:
    if st.session_state.winner == "Draw":
        st.markdown("<h2 style='text-align: center; color: orange;'>🤝 It's a Draw! 🤝</h2>", unsafe_allow_html=True)
    else:
        st.markdown(f"<h2 style='text-align: center; color: green;'>🏆 {st.session_state.winner} Wins! 🎉</h2>", unsafe_allow_html=True)

    # Reset Button
    if st.button("🔄 Restart Game", key="reset_button"):
        reset_game()
        st.rerun()

# Ensure AI move happens after Streamlit rerun
if st.session_state.pending_ai_move:
    ai_play()
