import streamlit as st
import pandas as pd
from datetime import datetime
import time

st.set_page_config(layout="wide", page_title="Master Planner Pro")

# CSS - Advanced 3D, Neon Glow & Animation
st.markdown("""
    <style>
    .stApp { background: #050505; color: white; }
    
    /* 5 BOXES HEADER - PLANE */
    .header-box { display: flex; justify-content: center; gap: 20px; margin-bottom: 50px; }
    .box {
        width: 120px; height: 120px;
        background: linear-gradient(145deg, #1a1a1a, #0d0d0d);
        border: 2px solid #06b6d4; border-radius: 20px;
        display: flex; align-items: center; justify-content: center;
        font-size: 35px; font-weight: 800; color: #a855f7;
        box-shadow: 0 0 20px rgba(6, 182, 212, 0.4);
        transition: 0.6s;
    }
    .box:hover { transform: rotateY(180deg); box-shadow: 0 0 40px #a855f7; }

    /* 3D CARDS */
    .neon-card {
        background: #111; padding: 30px; border-radius: 30px;
        border: 1px solid #333; box-shadow: 10px 10px 30px #000;
        margin-bottom: 20px; transition: 0.3s;
    }
    .neon-card:hover { border: 1px solid #06b6d4; box-shadow: 0 0 20px rgba(6, 182, 212, 0.3); }

    /* SIDEBAR ICONS */
    .side-icon { font-size: 30px; margin: 15px; cursor: pointer; }
    </style>
""", unsafe_allow_html=True)

# 1. Header Boxes (PLANE)
letters = ["P", "L", "A", "N", "E"]
st.markdown('<div class="header-box">' + 
            "".join([f'<div class="box">{l}</div>' for l in letters]) + 
            '</div>', unsafe_allow_html=True)

# 2. Sidebar with 3D Icons
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#06b6d4;'>AP DASHBOARD</h2>", unsafe_allow_html=True)
    menu = ["🏠 Dashboard", "✅ Tasks", "⏱️ Timer", "📅 Calendar"]
    choice = st.radio("MENU", menu)

# 3. Main Dashboard Logic
if choice == "🏠 Dashboard":
    st.title("⚡ Productivity Hub")
    c1, c2 = st.columns(2)
    with c1: st.markdown('<div class="neon-card"><h3>Tasks Pending</h3><p>High Priority: 3</p></div>', unsafe_allow_html=True)
    with c2: st.markdown('<div class="neon-card"><h3>Focus Time</h3><p>Today: 4.5 hrs</p></div>', unsafe_allow_html=True)

elif choice == "✅ Tasks":
    st.title("📝 Task Management")
    task = st.text_input("Enter a new task...")
    if st.button("Add Task"):
        st.success(f"Added: {task}")
    # Simulate list with 3D effect
    st.markdown('<div class="neon-card">○ Do UI Design<br>○ Code Logic<br>○ Deploy</div>', unsafe_allow_html=True)

elif choice == "⏱️ Timer":
    st.title("⏱️ Pomodoro Timer")
    col1, col2 = st.columns(2)
    with col1:
        duration = st.slider("Select Minutes", 1, 60, 25)
    with col2:
        if st.button("Start Focus Session"):
            with st.empty():
                for secs in range(duration * 60, 0, -1):
                    mins, s = divmod(secs, 60)
                    st.write(f"## {mins:02d}:{s:02d}")
                    time.sleep(1)
                st.balloons()

elif choice == "📅 Calendar":
    st.title("📅 Monthly Planner")
    st.date_input("Select Date")
    st.write("---")
    st.write("All features enabled for free!")
