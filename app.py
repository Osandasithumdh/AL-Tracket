import streamlit as st
import datetime
import calendar
import time
import random

# --- UI Config ---
st.set_page_config(layout="wide")

# --- Dynamic Color Scheme (මාසෙන් මාසෙට වෙනස් වෙනවා) ---
def get_month_color():
    month = datetime.datetime.now().month
    colors = {1: "#FF5733", 2: "#33FF57", 3: "#3357FF", 4: "#FF33A1", 5: "#A133FF", 6: "#FFD433", 7: "#33FFF5", 8: "#FF8C33", 9: "#8CFF33", 10: "#33FF8C", 11: "#FF3333", 12: "#5733FF"}
    return colors.get(month, "#9b51e0")

ui_color = get_month_color()

# --- CSS (3D & Neon Effects) ---
st.markdown(f"""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@400;700&display=swap');
    .stApp {{ font-family: 'Noto Sans Sinhala', sans-serif; }}
    .title-3d {{ color: white; text-shadow: 2px 2px 0px #aaa, 4px 4px 0px {ui_color}; font-size: 50px; font-weight: bold; }}
    .stButton>button {{ border-radius: 20px; transition: 0.3s; }}
    .stButton>button:hover {{ box-shadow: 0 0 20px {ui_color}; transform: scale(1.05); }}
    </style>
""", unsafe_allow_html=True)

# --- Header Section ---
st.markdown("<h1 class='title-3d'>⚡ Daily Planner</h1>", unsafe_allow_html=True)

# --- Subject Management ---
if 'subjects' not in st.session_state: st.session_state.subjects = []

col1, col2 = st.columns([2, 1])
with col1:
    new_sub = st.text_input("සබ්ජෙක්ට් එකේ නම:")
    if st.button("Add Subject"):
        if new_sub:
            st.session_state.subjects.append({"name": new_sub, "tasks": [], "time": 0})
            st.rerun()

# --- Dashboard View ---
st.divider()
for sub in st.session_state.subjects:
    with st.expander(f"📁 {sub['name']} (Click to Open)"):
        # මෙතන ටයිමර් සහ ටාස්ක් කොටස් එකතු කරන්න ඕනේ
        st.write("ටයිමර් සහ ටාස්ක් පැනල් එක මෙතනට එනවා...")
