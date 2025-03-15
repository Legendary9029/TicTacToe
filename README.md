# 🎮 Tic-Tac-Toe AI & PvP

A modern and responsive Tic-Tac-Toe game built with **Streamlit**. Play against an **AI opponent** or challenge a **friend in PvP mode**!

---

## 🚀 Features

✅ **AI Mode** - Play against an AI that makes smart moves.  
✅ **Player vs Player (PvP) Mode** - Two players can play locally.  
✅ **Smart AI Turns** - AI plays automatically after the player's move.  
✅ **Instant UI Updates** - No need to press buttons twice!  
✅ **Winning Screen** - Displays the winner in a visually appealing way.  
✅ **Reset Button** - Easily restart the game after completion.  
✅ **Color-coded Buttons** - "X" and "O" buttons have distinct colors for better visibility.  
✅ **Responsive UI** - Works seamlessly on desktop and mobile devices.  

---

## 📂 Project Structure
```
├── backend
│   ├── main.py   # FastAPI backend
│   ├── ai_logic.py # AI logic using Minimax
├── frontend
│   ├── app.py   # Streamlit frontend
├── run.py      # Script to start both backend & frontend
├── README.md   # Project documentation
```

## 🛠️ Installation & Setup

### 1️⃣ **Clone the Repository**
```bash
git clone https://github.com/Legendary9029/tic-tac-toe-streamlit.git
cd tic-tac-toe-streamlit
```

### 2️⃣ **Create a Virtual Environment** (Optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On macOS/Linux
venv\Scripts\activate  # On Windows
```

### 3️⃣ **Install Dependencies**
```bash
pip install -r requirements.txt
```

### 4️⃣ **Run the Application**
```bash
python run.py
```

This will automatically start both the **backend (FastAPI)** and **frontend (Streamlit)**.

---

## 🎮 How to Play?

### 🆚 **Select Game Mode**
- **AI Mode:** Play against the AI (You: "X", AI: "O").
- **Player vs Player Mode:** Two players take turns manually.

### 🎯 **Game Rules**
- Click on an empty square to place your move.
- The game alternates turns automatically.
- Win by placing three marks in a row, column, or diagonal.
- If the board is full and no one wins, it's a draw.
- A reset button appears after a game finishes.

---

## 🛠️ Tech Stack
- **Frontend:** Streamlit (Python)
- **Backend:** FastAPI (Python)
- **AI Logic:** Minimax Algorithm for Smart AI Moves
- **State Management:** Streamlit Session State

---

## 🤝 Contributing
Want to improve this project? Feel free to contribute!

1. **Fork the repository**
2. **Create a new branch** (`feature-improvement`)
3. **Commit your changes**
4. **Push to GitHub** and create a Pull Request

---

## 📜 License
This project is open-source and available under the **MIT License**.

---

## 📬 Contact
For any questions or improvements, reach out to me at:  
📧 **Email:** adityasinha1304@gmail.com   
🔗 **GitHub:** [Legendary9029](https://github.com/legendary9029)

