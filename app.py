import streamlit as st
import pandas as pd
import plotly.express as px
import time
import json
import os
from datetime import datetime

# --- UI & CSS ---
st.set_page_config(layout="wide")
st.markdown("""
    <style>
    .title-3d { font-size: 40px; font-weight: bold; color: #fff; text-shadow: 2px 2px #ff4b4b; }
    .stButton>button:hover { box-shadow: 0 0 15px #00f2fe; transform: scale(1.05); }
    </style>
""", unsafe_allow_html=True)

# --- Logic ---
if 'subjects' not in st.session_state: st.session_state.subjects = {}
if 'tasks' not in st.session_state: st.session_state.tasks = []

st.markdown("<h1 class='title-3d'>⚡ DAILY PLANNER</h1>", unsafe_allow_html=True)

# --- Subject Add ---
with st.sidebar:
    new_sub = st.text_input("සබ්ජෙක්ට් එක:")
    if st.button("Add Subject"):
        st.session_state.subjects[new_sub] = {"time": 0, "tasks": []}
        st.rerun()

# --- Main Dashboard ---
for sub, data in st.session_state.subjects.items():
    with st.expander(f"📚 {sub}"):
        # Timer
        col1, col2 = st.columns(2)
        with col1:
            st.write(f"⏱️ ගතකල කාලය: {data['time']} තත්පර")
            if st.button("Start Timer", key=f"start_{sub}"):
                # ටයිමර් ලොජික් (පැය/විනාඩි)
                st.session_state.subjects[sub]['time'] += 3600 
                st.rerun()
        
        # Tasks
        task = st.text_input(f"Task for {sub}:", key=f"t_{sub}")
        if st.button("Add Task", key=f"btn_{sub}"):
            st.session_state.tasks.append({"sub": sub, "task": task, "done": False})
            st.rerun()

# --- Task List & Progress ---
st.subheader("📋 කම්ප්ලීට් ටාස්ක්ස්")
for t in st.session_state.tasks:
    col1, col2 = st.columns([4, 1])
    col1.write(f"{'✅' if t['done'] else '⭕'} {t['task']} ({t['sub']})")
    if col2.button("Done", key=t['task']):
        t['done'] = True
        st.rerun()

# --- Analytics (Graph) ---
st.subheader("📈 වැඩ ප්‍රගතිය")
if st.session_state.tasks:
    df = pd.DataFrame(st.session_state.tasks)
    fig = px.bar(df, x='sub', color='sub', title="පැය ගණන අනුව ප්‍රගතිය")
    st.plotly_chart(fig)

# --- Calendar (Simple) ---
st.subheader("📅 කැලැන්ඩරය")
today = datetime.now().day
st.write(f"අද දිනය: {today}")
