import streamlit as st
import pandas as pd
import numpy as np
import time

# Page Configuration
st.set_page_config(layout="wide", page_title="Advanced Daily Planner")

# Custom CSS for Neon, 3D, and Responsive UI
st.markdown("""
    <style>
    .stApp { background-color: #050505; color: #E0E0E0; }
    
    /* Sidebar Styling - Enlarged Boxes */
    [data-testid="stSidebar"] { background-color: #0f0f0f; width: 250px; }
    .icon-btn { 
        background: linear-gradient(145deg, #1c1c1c, #0a0a0a);
        padding: 20px; margin: 10px; border-radius: 20px;
        text-align: center; border: 1px solid #333;
        box-shadow: 10px 10px 20px #000; transition: 0.3s;
    }
    .icon-btn:hover { border-color: #06b6d4; box-shadow: 0 0 20px #06b6d4; }
    
    /* 3D Glassmorphism Card */
    .card {
        background: rgba(20, 20, 20, 0.7);
        padding: 30px; border-radius: 30px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 20px 20px 60px #000, -20px -20px 60px #1a1a1a;
    }
    
    .neon-text { text-shadow: 0 0 10px #a855f7; font-weight: bold; }
    </style>
""", unsafe_allow_html=True)

# Navigation Logic
if 'page' not in st.session_state: st.session_state.page = 'Planner'

with st.sidebar:
    st.markdown("<h1 style='text-align:center; color:#06b6d4;'>⚡ PLANNER</h1>", unsafe_allow_html=True)
    if st.button("🏠 Dashboard"): st.session_state.page = 'Planner'
    if st.button("✅ My Tasks"): st.session_state.page = 'Tasks'

# Main Page Content
if st.session_state.page == 'Planner':
    st.markdown("<h1 style='text-align:center;'>⚡ Daily Plan</h1>", unsafe_allow_html=True)
    
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.markdown('<div class="card"><h3>⏱️ Time Tracker</h3>', unsafe_allow_html=True)
        # Timer Placeholder
        timer_val = st.empty()
        if st.button("▶ Start / ⏹️ Stop Timer"):
            for i in range(100):
                timer_val.write(f"<h1 style='color:#06b6d4;'>{i} Min</h1>", unsafe_allow_html=True)
                time.sleep(1)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<br><div class="card"><h3>📝 Add Daily Tasks</h3>', unsafe_allow_html=True)
        task = st.text_input("Enter task...")
        if st.button("Add Task"): st.success("Task Added!")
        st.markdown('</div>', unsafe_allow_html=True)

    with col2:
        st.markdown('<div class="card"><h3>📊 Productivity Summary</h3>', unsafe_allow_html=True)
        # Replacing complex charts with clear Metrics and simpler visual feedback
        col_a, col_b = st.columns(2)
        col_a.metric("Total Hours", "5.5h", "1.2h")
        col_b.metric("Tasks Done", "8", "2")
        
        # Simple Progress Bar for total day goal
        st.write("Day Completion Progress")
        st.progress(65)
        st.markdown('</div>', unsafe_allow_html=True)
