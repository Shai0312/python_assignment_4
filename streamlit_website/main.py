import streamlit as st

# ----- Page Configuration -----
st.set_page_config(
    page_title="My First Website",
    page_icon="🌐",
    layout="centered"
)

# ----- Background Image CSS -----
page_bg_img = '''
<style>
[data-testid="stAppViewContainer"] {
    background-image: url("https://images.unsplash.com/photo-1507525428034-b723cf961d3e");
    background-size: cover;
    background-repeat: no-repeat;
    background-attachment: fixed;
    background-position: center;
    min-height: 100vh;  /* Make sure it covers the whole page */
    # color: #fff; /* Ensuring the text is visible on the background */
}

[data-testid="stSidebar"] {
    background-color: rgba(0, 0, 0, 0.2);  /* Transparent with dark overlay */
    border-radius: 10px;  /* Rounded corners for a smooth look */
    padding-top: 20px;
    color: white
}

[data-testid="stHeader"] {
    # color: #fff;  /* White text for header */
}

[data-testid="stMarkdownContainer"] {
    # color: #fff;  /* White text for markdown */
    # color: white;  
     font-size: 20px;  /* Larger font size for better readability */
}

div[class="css-1v0mbdj"] {
    background-color: rgba(0, 0, 0, 0.3);
    padding: 20px;
    border-radius: 15px;
    margin-top: 20px;
}

.stButton>button {
    background-color: #fd7e14;
    # color: white;
    padding: 10px 20px;
    border-radius: 8px;
    border: none;
}

.stButton>button:hover {
    background-color: #f53b00;
}
</style>
'''

st.markdown(page_bg_img, unsafe_allow_html=True)

# ----- Sidebar Navigation -----
st.sidebar.title("📌 Navigation")
page = st.sidebar.radio("Go to", ("🏠 Home", "ℹ️ About", "📬 Contact"))

# ----- Home Page -----
if page == "🏠 Home":
    st.title("👋 Welcome to My First Python Website")
    st.markdown("This is the **home page** of my very first Python + Streamlit project!")

    name = st.text_input("📝 What's your name?")
    if name:
        st.success(f"Hi **{name}**! 👋 Thanks for visiting my website.")

# ----- About Page -----
elif page == "ℹ️ About":
    st.title("📖 About")
    st.markdown("""
    This is a simple multi-page **Streamlit website** built using Python.  
    I'm learning how to create interactive websites and apps, and this is my first step! 🚀

    **Tech used:**  
    - 🐍 Python  
    - 🧊 Streamlit  
    """)

# ----- Contact Page -----
elif page == "📬 Contact":
    st.title("📬 Contact Me")
    st.write("Have a question or feedback? Drop a message below! 💬")

    with st.form("contact_form"):
        email = st.text_input("📧 Your email")
        message = st.text_area("💬 Your message")
        submitted = st.form_submit_button("📨 Submit")
        if submitted:
            if email and message:
                st.success("✅ Thank you! Your message has been received.")
            else:
                st.warning("⚠️ Please fill in both fields before submitting.")
