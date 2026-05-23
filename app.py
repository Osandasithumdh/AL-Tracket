import streamlit as st
import time

st.set_page_config(layout="wide", page_title="Master Planner Pro")

# CSS - 3D & Neon Styling
st.markdown("""
    <style>
    .stApp { background: #050505; color: white; }
    .neon-card { 
        background: #111; padding: 25px; border-radius: 20px; 
        border: 1px solid #333; box-shadow: 10px 10px 20px #000;
        margin-bottom: 20px;
    }
    .stButton>button { width: 100%; border-radius: 10px; background: #06b6d4; color: white; }
    </style>
""", unsafe_allow_html=True)

# Session State for Tasks and Timer
if 'tasks' not in st.session_state: st.session_state.tasks = []

# Sidebar
with st.sidebar:
    st.title("🚀 Planner")
    page = st.radio("Menu", ["⏱️ Stopwatch", "✅ Tasks"])

# 1. Stopwatch Page
if page == "⏱️ Stopwatch":
    st.title("⏱️ Stopwatch")
    if 'start_time' not in st.session_state: st.session_state.start_time = 0
    
    col1, col2 = st.columns(2)
    if col1.button("Start"): st.session_state.start_time = time.time()
    if col2.button("Reset"): st.session_state.start_time = 0
    
    display = st.empty()
    if st.session_state.start_time != 0:
        elapsed = time.time() - st.session_state.start_time
        display.markdown(f"## {elapsed:.2f} seconds")

# 2. Task Manager Page
elif page == "✅ Tasks":
    st.title("📝 My Tasks")
    new_task = st.text_input("Add a task...")
    if st.button("Add Task") and new_task:
        st.session_state.tasks.append({"task": new_task, "done": False})
    
    st.write("---")
    for i, t in enumerate(st.session_state.tasks):
        c1, c2 = st.columns([0.1, 0.9])
        if c1.checkbox("", key=i):
            t['done'] = True
        
        if t['done']:
            st.markdown(f"~~{t['task']}~~ ✅")
        else:
            st.write(t['task'])
