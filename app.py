import streamlit as st
from datetime import datetime

st.set_page_config(layout="wide", page_title="Master Planner Pro")

# CSS - 3D & Animation Effects
st.markdown("""
    <style>
    .stApp { background: #050505; color: white; }
    
    /* 5 Boxes Header Style */
    .header-container { display: flex; justify-content: center; gap: 20px; margin-bottom: 40px; }
    .box {
        width: 120px; height: 120px;
        background: linear-gradient(145deg, #1c1c1c, #0a0a0a);
        border: 2px solid #333; border-radius: 20px;
        display: flex; align-items: center; justify-content: center;
        font-size: 30px; font-weight: bold; color: #06b6d4;
        box-shadow: 10px 10px 20px #000;
        transition: 0.5s; cursor: pointer;
    }
    .box:hover { transform: rotateY(180deg); border-color: #a855f7; box-shadow: 0 0 20px #a855f7; }
    
    .card { background: #151515; padding: 25px; border-radius: 25px; border: 1px solid #333; }
    </style>
""", unsafe_allow_html=True)

# 5 Boxes Header
letters = ["P", "L", "A", "N", "E"]
st.markdown('<div class="header-container">' + 
            "".join([f'<div class="box">{l}</div>' for l in letters]) + 
            '</div>', unsafe_allow_html=True)

st.markdown("<hr>", unsafe_allow_html=True)

# App Content
st.markdown(f"<h1 style='text-align:center;'>⚡ Daily Plan: {datetime.now().strftime('%Y-%m-%d')}</h1>", unsafe_allow_html=True)

col1, col2 = st.columns([1, 1])

with col1:
    st.markdown('<div class="card"><h3>⏱️ Time Tracker</h3>', unsafe_allow_html=True)
    if st.button("Start Timer"): st.write("Timer running...")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="card"><h3>✅ Tasks</h3>', unsafe_allow_html=True)
    task = st.text_input("Add new task...")
    if st.button("Add"): st.write(f"Added: {task}")
    st.markdown('</div>', unsafe_allow_html=True)
