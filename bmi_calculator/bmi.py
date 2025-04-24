import streamlit as st

st.title("💪 BMI Calculator")

weight = st.number_input("⚖️ Enter your weight in kg", min_value=1.0)

# Select height input unit
unit = st.selectbox("📏 Choose height unit", ["Centimeters (cm)", "Feet (ft)"])

if unit == "Centimeters (cm)":
    height = st.number_input("📏 Enter your height in cm", min_value=50.0, max_value=300.0)
    height_m = height / 100  # Convert cm to meters
else:
    height_ft = st.number_input("📏 Enter your height in feet", min_value=1.0, max_value=9.0)
    height_m = height_ft * 0.3048  # Convert ft to meters

if st.button("🧮 Calculate BMI"):
    bmi = weight / (height_m ** 2)
    st.success(f"✅ Your BMI is: **{bmi:.2f}**")

    # BMI Categories
    if bmi < 18.5:
        st.warning("😟 You are **underweight**. Eat well and stay healthy!")
    elif 18.5 <= bmi < 24.9:
        st.info("🎉 You are in the **normal weight** range. Great job!")
    elif 25 <= bmi < 29.9:
        st.warning("⚠️ You are **overweight**. Time for a little fitness! 🏃")
    else:
        st.error("🚨 You are in the **obese** range. Please take care! ❤️‍🩹")
