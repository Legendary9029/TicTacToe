import streamlit as st
import random
import time  # For AI delay

# Initialize session state
if "board" not in st.session_state:
    st.session_state.board = [["", "", ""], ["", "", ""], ["", "", ""]]
    st.session_state.current_player = "X"
    st.session_state.game_over = False
    st.session_state.winner = None
    st.session_state.mode = "AI"  # Default mode: AI
    st.session_state.moves = 0
    st.session_state.pending_ai_move = False  # Ensures AI move triggers after rerun

# Function to check for a win or draw
def check_game_state():
    board = st.session_state.board
    for row in board:
        if row[0] == row[1] == row[2] and row[0] != "":
            st.session_state.game_over = True
            st.session_state.winner = row[0]
            return
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != "":
            st.session_state.game_over = True
            st.session_state.winner = board[0][col]
            return
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != "":
        st.session_state.game_over = True
        st.session_state.winner = board[0][0]
        return
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != "":
        st.session_state.game_over = True
        st.session_state.winner = board[0][2]
        return
    if st.session_state.moves == 9:
        st.session_state.game_over = True
        st.session_state.winner = "Draw"

# AI Move
def ai_play():
    if (
        st.session_state.current_player == "O"
        and not st.session_state.game_over
        and st.session_state.mode == "AI"
    ):
        empty_cells = [(i, j) for i in range(3) for j in range(3) if st.session_state.board[i][j] == ""]
        if empty_cells:
            time.sleep(0.3)  # Short delay for better UX
            i, j = random.choice(empty_cells)
            st.session_state.board[i][j] = "O"
            st.session_state.moves += 1
            check_game_state()
            if not st.session_state.game_over:
                st.session_state.current_player = "X"
            st.session_state.pending_ai_move = False  # AI move completed
            st.rerun()  # Ensure UI updates immediately

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
