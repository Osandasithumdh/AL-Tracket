import streamlit as st

# ලස්සන තේමාවක් සඳහා
st.set_page_config(page_title="My Daily Plan", page_icon="📝")

st.title("✨ මගේ දෛනික සැලැස්ම (Daily Plan) ✨")

# වැඩ ඇතුලත් කරන්න
task = st.text_input("අද කරන්න තියෙන දේ මෙතන ලියන්න:")

if st.button("Add ➕"):
    if task:
        st.success(f"නියමයි! අද වැඩේ: {task}")
    else:
        st.warning("කරුණාකර වැඩක් ලියන්න!")
