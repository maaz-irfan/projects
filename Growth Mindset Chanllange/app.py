import streamlit as st
import random
from textblob import TextBlob

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

# Function to check if the response is meaningful
def is_meaningful_text(text):
    words = text.split()
    valid_words = [word for word in words if TextBlob(word).correct() == word]  # Check if each word is valid
    return len(valid_words) > 0  # If at least one word is valid, return True

# Function to check and correct spelling/grammar
def check_spelling(text):
    return str(TextBlob(text).correct())  # AI-based correction

# Submit Button
if st.button("Submit Response"):
    if user_response.strip():
        if is_meaningful_text(user_response):  # Check if text contains valid words
            corrected_response = check_spelling(user_response)
            
            if corrected_response != user_response:
                st.warning(f"🔍 Your response contains some mistakes. Do you want to correct it?\n\n**Corrected Version:** {corrected_response}")
            else:
                st.success("✅ Great job! Your response looks good. Keep going!")
        else:
            st.error("❌ Your response doesn't seem to contain meaningful words. Please enter a valid answer.")
    else:
        st.warning("⚠️ Please enter a response before submitting.")

# Motivational Message
st.write("🌱 Remember: Challenges help you grow! Keep learning and improving. 🚀")
