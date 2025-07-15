import streamlit as st
import random
import base64

# Add background function
def set_bg_from_local(image_file):
    with open(image_file, "rb") as image:
        encoded = base64.b64encode(image.read()).decode()
    bg_img = f"""
    <style>
    [data-testid="stAppViewContainer"] {{
        background-image: url("data:image/png;base64,{encoded}");
        background-size: cover;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    [data-testid="stHeader"], [data-testid="stToolbar"] {{
        background-color: rgba(0,0,0,0);
    }}
    </style>
    """
    st.markdown(bg_img, unsafe_allow_html=True)
# 1. PAGE SETUP
st.set_page_config(page_title="Snake Water Gun Game", page_icon="🐍", layout="centered")
set_bg_from_local("background.jpeg")
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
            st.balloons()
        else:
            result = "😢 You Lost! Try again!"
            st.error(result)

# 5. FOOTER
st.markdown("---")
st.markdown("<center> Created by Kinjal✨</center>", unsafe_allow_html=True)
