import streamlit as st
import random

# 1. PAGE SETUP
st.set_page_config(page_title="Snake Water Gun Game", page_icon="🐍", layout="centered")

# 2. HEADER
st.title("🐍 Snake - Water - Gun Game")

# 3. USER NAME
if "username" not in st.session_state:
    st.session_state.username = ""

if st.session_state.username == "":
    name = st.text_input("Enter your name to begin:", key="name_input")
    if name:
        st.session_state.username = name
        st.rerun()
else:
    st.success(f"👋 Hello, {st.session_state.username}!")
    st.write("🎮 Here is a game I made just for you. Have fun!")

    # 4. GAME LOGIC (no images)
    choices = ['Snake', 'Water', 'Gun']
    user_choice = st.selectbox("Choose your move:", choices)

    if st.button("Play"):
        computer_choice = random.choice(choices)

        st.write(f"🧍 You chose: **{user_choice}**")
        st.write(f"🤖 Computer chose: **{computer_choice}**")

        # Game Result Logic
        if user_choice == computer_choice:
            result = "😐 It's a Tie!"
            st.info(result)
        elif (user_choice == 'Snake' and computer_choice == 'Water') or \
             (user_choice == 'Water' and computer_choice == 'Gun') or \
             (user_choice == 'Gun' and computer_choice == 'Snake'):
            result = "🎉 You Win!"
            st.success(result)
        else:
            result = "😢 You Lost! Try again!"
            st.error(result)

# 5. FOOTER
st.markdown("---")
st.markdown("<center>💖 Created with love by Kinjal 💖</center>", unsafe_allow_html=True)
