import streamlit as st
import random
from textblob import TextBlob

# Growth Mindset Questions
challenges = [
    {"question": "What is something new you learned today?", "response": ""},
    {"question": "How did you handle a difficult situation recently?", "response": ""},
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

# Function to check and correct spelling/grammar
def check_spelling(text):
    corrected_text = str(TextBlob(text).correct())  # AI-based correction
    return corrected_text

# Submit Button
if st.button("Submit Response"):
    if user_response.strip():
        corrected_response = check_spelling(user_response)
        
        if corrected_response != user_response:
            st.warning(f"🔍 Your response contains some mistakes. Do you want to correct it?\n\n**Corrected Version:** {corrected_response}")
        else:
            st.success("✅ Great job! Your response looks good. Keep going!")
    else:
        st.warning("⚠️ Please enter a response before submitting.")

# Motivational Message
st.write("🌱 Remember: Challenges help you grow! Keep learning and improving. 🚀")

# How to run the app:
# In the terminal, type: `streamlit run app.py`
