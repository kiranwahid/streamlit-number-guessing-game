import streamlit as st
import random

# Function to play the game
def play_game():
    st.write("# Welcome to Guess the Number Game ❤️")
    
    # Initialize session state to track attempts and guesses
    if "secret_number" not in st.session_state:
        st.session_state.secret_number = random.randrange(50, 100)
    if "attempts_left" not in st.session_state:
        st.session_state.attempts_left = 7
    if "guess_count" not in st.session_state:
        st.session_state.guess_count = 0
    
    # Display remaining attempts
    st.write(f"## You have {st.session_state.attempts_left} attempts left.")
    
    # Input field for user guess
    user_guess = st.number_input("Enter a guess between 50 and 100:🤔", min_value=50, max_value=100, step=1)

    if st.button("Submit Guess"):
        st.session_state.guess_count += 1
        st.session_state.attempts_left -= 1

        if user_guess == st.session_state.secret_number:
            st.success(f"Wow! Congrats 👏 You guessed it right in {st.session_state.guess_count} attempts 😍😍")
            reset_game()
        elif st.session_state.attempts_left == 0:
            st.error(f"Oops, the correct number was {st.session_state.secret_number}😒 ")
            reset_game()
        elif user_guess < st.session_state.secret_number:
            st.warning("Too low. Guess again. 😒")
        else:
            st.warning("Too high. Guess again. 🫡")

# Function to reset the game state
def reset_game():
    if st.button("Play Again"):
        st.session_state.secret_number = random.randrange(50, 100)
        st.session_state.attempts_left = 7
        st.session_state.guess_count = 0
        st.experimental_rerun()

# Streamlit app layout and background color
st.markdown(
    """
    <style>
    body {
        background-color: #ADD8E6;
    }
    </style>
    """, 
    unsafe_allow_html=True
)

# Main game loop
play_game()

