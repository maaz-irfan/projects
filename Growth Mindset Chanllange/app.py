import streamlit as st
import random

# Growth Mindset Questions
challenges = [
    {"question": "What can you do differently next time you face a challenge?", "response": ""},
    {"question": "Write about a mistake you made and what you learned from it.", "response": ""},
    {"question": "What is one skill you want to improve, and how will you work on it?", "response": ""}
]

# Streamlit UI
st.title("🚀 Growth Mindset Challenge")
st.write("Every challenge is an opportunity to grow. Answer these questions to reflect and build a growth mindset!")

# Select a random challenge
selected_challenge = random.choice(challenges)

st.subheader("💡 Challenge Question:")
st.write(selected_challenge["question"])

# User input text area
user_response = st.text_area("Your Response", "")

# Submit Button
if st.button("Submit Response"):
    if user_response.strip():
        st.success("✅ Great job! Your response has been submitted.")
    else:
        st.warning("⚠️ Please enter a response before submitting.")

# Motivational Message
st.write("🌱 Remember: Challenges help you grow! Keep learning and improving. 🚀")
