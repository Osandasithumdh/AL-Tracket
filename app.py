import streamlit as st

st.title("MY DAILY PLAN 📝")

task = st.text_input("අද කරන්න තියෙන වැඩේ ලියන්න:")

if st.button("Add"):
    st.write("ඔයා එකතු කළා: " + task)
