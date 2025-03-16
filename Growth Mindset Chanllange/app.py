import streamlit as st
import random
from textblob import TextBlob

# List of challenges
challenges = [
    "What can you do differently next time you face a challenge?",
    "Write about a mistake you made and what you learned from it.",
    "What is one skill you want to improve, and how will you work on it?"
]

# Title and description
st.title("🚀 Growth Mindset Challenge") 
st.write("Every challenge is an opportunity to grow. Reflect and build a growth mindset! 💡")

# Randomly selecting a challenge
selected_challenge = random.choice(challenges)

st.subheader("💡 Challenge Question:")
st.write(f"**{selected_challenge}**")

# User input text area
user_response = st.text_area("✍️ Your Response", "")

# Function to correct spelling
def correct_text(text):
    return str(TextBlob(text).correct())

# Submit Button
if st.button("✅ Submit Response"):
    if user_response.strip():  # Check if input is not empty
        corrected_response = correct_text(user_response)
        
        if corrected_response != user_response:
            st.warning("🔍 Your response contains some spelling mistakes.")
            st.write(f"**Suggested Correction:**\n\n➡️ {corrected_response}")
        else:
            st.success("✅ Your response looks great! Keep it up! 🚀")
    else:
        st.error("⚠️ Please write something before submitting.")

# Motivational Message
st.write("🌱 **Remember:** Every challenge helps you grow! Keep learning and improving. 🚀")
