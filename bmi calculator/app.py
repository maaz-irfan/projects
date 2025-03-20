import streamlit as st

def calculate_bmi(weight, height):
    return weight / (height ** 2)

st.title("BMI Calculator")

weight = st.number_input("Enter your weight (kg)", min_value=0.0, format="%.2f")
height = st.number_input("Enter your height (m)", min_value=0.0, format="%.2f")

if st.button("Calculate BMI"):
    if height > 0:
        bmi = calculate_bmi(weight, height)
        st.write(f"Your BMI is {bmi:.2f}")
        if bmi < 18.5:
            st.write("You are underweight.")
        elif 18.5 <= bmi < 24.9:
            st.write("You have a normal weight.")
        elif 25 <= bmi < 29.9:
            st.write("You are overweight.")
        else:
            st.write("You are obese.")
    else:
        st.write("Height must be greater than 0.")
        
        # To run this Streamlit app on Google Colab, you need to install Streamlit and pyngrok

        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        