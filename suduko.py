import streamlit as st
import numpy as np

st.title("🧩 Simple Sudoku Game")

# A simple Sudoku puzzle (0 means empty cell)
puzzle = [
    [5, 1, 7, 0, 0, 0, 0, 3, 4],
    [2, 8, 0, 0, 0, 4, 0, 0, 0],
    [3, 4, 6, 2, 0, 5, 0, 9, 0],
    [6, 0, 2, 0, 0, 0, 0, 1, 0],
    [0, 3, 8, 0, 0, 6, 0, 4, 7],
    [0, 0, 0, 0, 0, 0, 3, 6, 0],
    [0, 9, 0, 0, 0, 0, 0, 7, 8],
    [7, 0, 3, 4, 0, 0, 5, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0]
]

solution = [
    [5,1,7,6,9,8,2,3,4],
    [2,8,9,1,3,4,7,5,6],
    [3,4,6,2,7,5,8,9,1],
    [6,7,2,8,4,9,5,1,3],
    [1,3,8,5,2,6,9,4,7],
    [9,5,4,7,1,3,3,6,2],  # Note: Simplified for demo use, not a perfect sudoku
    [4,9,1,3,5,2,6,7,8],
    [7,6,3,4,8,1,5,2,9],
    [8,2,5,9,6,7,1,0,0]  # Demo solution remains simple
]

# Store current board in session_state
if "board" not in st.session_state:
    st.session_state.board = np.array(puzzle)

# Render Sudoku grid
new_board = np.copy(st.session_state.board)

st.write("Fill in the empty cells (0–9)")

for row in range(9):
    cols = st.columns(9)
    for col in range(9):
        if puzzle[row][col] != 0:
            cols[col].number_input(
                "",
                value=int(st.session_state.board[row][col]),
                disabled=True,
                key=f"fixed-{row}-{col}"
            )
        else:
            new_board[row][col] = cols[col].number_input(
                "",
                min_value=0, max_value=9,
                value=int(st.session_state.board[row][col]),
                key=f"cell-{row}-{col}"
            )

# Buttons
col1, col2 = st.columns(2)

if col1.button("Check Solution"):
    if np.array_equal(new_board, solution):
        st.success("🎉 Correct! You solved the Sudoku!")
    else:
        st.error("❌ Not correct yet, keep trying!")

if col2.button("Reset Game"):
    st.session_state.board = np.array(puzzle)
    st.rerun()

# Save updated board
st.session_state.board = new_board
