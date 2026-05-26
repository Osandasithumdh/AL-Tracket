import streamlit as st
import time
import json
import os
from datetime import datetime

# --- CSS ලුක් එක (3D Neon Look) ---
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Noto+Sans+Sinhala:wght@400;700&display=swap');
    body, * { font-family: 'Noto Sans Sinhala', sans-serif !important; }
    .stButton>button { border-radius: 15px; background: linear-gradient(45deg, #00f2fe, #9b51e0); color: white; border: none; padding: 10px 20px; font-weight: bold; }
    .stButton>button:hover { transform: scale(1.05); box-shadow: 0 0 20px #00f2fe; }
    </style>
""", unsafe_allow_html=True)

# --- දත්ත සැකසුම ---
DATA_FILE = "data.json"
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f: return json.load(f)
    return {"tasks": []}

def save_data(data):
    with open(DATA_FILE, "w") as f: json.dump(data, f)

data = load_data()
st.title("✨ මගේ වැඩ සැලසුම")

# --- ටාස්ක් ඇඩ් කිරීම ---
new_task = st.text_input("ටාස්ක් එක මෙතන ලියන්න:")
if st.button("Add Task"):
    if new_task:
        data["tasks"].append({"name": new_task, "active": False, "id": str(time.time())})
        save_data(data)
        st.rerun()

# --- ටාස්ක් ලැයිස්තුව සහ ටයිමර් ---
st.divider()
for task in data["tasks"]:
    col1, col2 = st.columns([3, 1])
    with col1:
        st.subheader(task["name"])
    with col2:
        if st.button(f"Start", key=task["id"]):
            task["active"] = True
            save_data(data)
            st.rerun()
    
    if task.get("active"):
        st.write("⏱️ පැය සම්පූර්ණ වෙමින් පවතී...")
        progress_bar = st.progress(0)
        for i in range(101):
            progress_bar.progress(i)
            time.sleep(0.05) # මෙතන 0.05 වෙනුවට වෙලාව අනුව වෙනස් කළ හැක
        
        task["active"] = False
        save_data(data)
        st.success(f"{task['name']} - පැය සම්පූර්ණයි! 🎉")
        st.rerun()

st.divider()
