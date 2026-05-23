import streamlit as st
import time
from datetime import datetime

# Page config
st.set_page_config(layout="wide", page_title="Master Planner Pro")

# CSS - Advanced 3D & Neon UI
st.markdown("""
    <style>
    .stApp { background: #050505; color: white; }
    
    /* 3D Rotating Header */
    .header-box { display: flex; justify-content: center; gap: 20px; margin-bottom: 40px; }
    .box {
        width: 100px; height: 100px;
        background: linear-gradient(145deg, #1a1a1a, #0d0d0d);
        border: 2px solid #06b6d4; border-radius: 20px;
        display: flex; align-items: center; justify-content: center;
        font-size: 30px; font-weight: 800; color: #a855f7;
        box-shadow: 0 0 15px rgba(6, 182, 212, 0.5);
        transition: 0.6s; cursor: pointer;
    }
    .box:hover { transform: rotateY(180deg); border-color: #a855f7; box-shadow: 0 0 30px #a855f7; }

    /* Cards */
    .card {
        background: #111; padding: 25px; border-radius: 25px;
        border: 1px solid #333; box-shadow: 10px 10px 20px #000;
    }
    </style>
""", unsafe_allow_html=True)

# 1. Header (PLANE)
st.markdown('<div class="header-box">' + 
            "".join([f'<div class="box">{l}</div>' for l in ["P","L","A","N","E"]]) + 
            '</div>', unsafe_allow_html=True)

# 2. Sidebar - AP Style
with st.sidebar:
    st.image("master_planner_logo.png", width=120) # මෙතනට ඔයාගේ ලෝගෝ එක දෙන්න
    st.markdown("<h2 style='text-align:center; color:#06b6d4;'>AP DASHBOARD</h2>", unsafe_allow_html=True)
    menu = st.radio("", ["🏠 Home", "✅ Tasks", "⏱️ Timer", "📅 Calendar"])

# 3. Main Logic
if menu == "🏠 Home":
    st.title("⚡ Daily Overview")
    st.markdown('<div class="card"><h3>Welcome to your 3D Planner</h3></div>', unsafe_allow_html=True)

elif menu == "✅ Tasks":
    st.title("📝 Task Management")
    task = st.text_input("Add task")
    if st.button("Add"): st.write("Task Added!")
    st.markdown('<div class="card">○ Task 1<br>○ Task 2</div>', unsafe_allow_html=True)

elif menu == "⏱️ Timer":
    st.title("⏱️ Focus Timer")
    if st.button("Start Timer"):
        st.write("Timer Active!")

elif menu == "📅 Calendar":
    st.title("📅 Calendar")
    st.date_input("Date")
