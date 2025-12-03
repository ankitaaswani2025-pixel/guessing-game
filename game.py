import streamlit as st
import random

st.title("🎯 Guessing Game")

# Initialize the secret number in session state
if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)

if "message" not in st.session_state:
    st.session_state.message = "Guess a number between 1 and 100!"

st.write(st.session_state.message)

# User input
guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

# Check guess button
if st.button("Check Guess"):
    if guess < st.session_state.secret:
        st.session_state.message = "Too low! Try again."
    elif guess > st.session_state.secret:
        st.session_state.message = "Too high! Try again."
    else:
        st.session_state.message = "🎉 Correct! You guessed it!"
        
    st.experimental_rerun()

# Restart game
if st.button("Restart Game"):
    st.session_state.secret = random.randint(1, 100)
    st.session_state.message = "New game started! Guess a number between 1 and 100."
    st.experimental_rerun()
