import streamlit as st
import pandas as pd
from datetime import datetime

st.set_page_config(layout="wide", page_title="Master Planner Pro")

# CSS - Neon & 3D Styling
st.markdown("""
    <style>
    .stApp { background: #0a0a0a; color: white; }
    .card { background: #151515; padding: 25px; border-radius: 25px; border: 1px solid #333; box-shadow: 10px 10px 30px #000; }
    .neon-text { color: #06b6d4; text-shadow: 0 0 10px #06b6d4; font-weight: bold; }
    .task-item { display: flex; align-items: center; justify-content: space-between; padding: 10px; border-bottom: 1px solid #333; }
    </style>
""", unsafe_allow_html=True)

# Session State Initialization
if 'tasks' not in st.session_state: st.session_state.tasks = []

# Sidebar Navigation
with st.sidebar:
    st.markdown("<h2 style='text-align:center;'>🚀 NAVIGATION</h2>", unsafe_allow_html=True)
    page = st.radio("Go to:", ["Dashboard", "Calendar"])

if page == "Dashboard":
    st.markdown("<h1 style='text-align:center;'>⚡ Daily Plan: " + datetime.now().strftime("%Y-%m-%d") + "</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 1])
    
    with col1:
        st.markdown('<div class="card"><h3>⏱️ Time Tracker</h3>', unsafe_allow_html=True)
        timer_col1, timer_col2, timer_col3 = st.columns(3)
        h = timer_col1.number_input("Hr", 0, 24, 0)
        m = timer_col2.number_input("Min", 0, 59, 0)
        s = timer_col3.number_input("Sec", 0, 59, 0)
        if st.button("Start Timer"): st.info(f"Timer set for {h}h {m}m {s}s")
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col2:
        st.markdown('<div class="card"><h3>✅ My Tasks</h3>', unsafe_allow_html=True)
        new_task = st.text_input("New Task")
        if st.button("Add Task"): st.session_state.tasks.append({"task": new_task, "done": False})
        
        for idx, t in enumerate(st.session_state.tasks):
            col_t1, col_t2 = st.columns([0.1, 0.9])
            if col_t1.checkbox("", key=f"check_{idx}"):
                st.markdown(f"~~{t['task']}~~ ✅", unsafe_allow_html=True)
            else:
                st.write(t['task'])
        st.markdown('</div>', unsafe_allow_html=True)

elif page == "Calendar":
    st.markdown("<h1 style='text-align:center;'>📅 Calendar</h1>", unsafe_allow_html=True)
    st.date_input("Select Date")
