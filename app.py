import streamlit as st
import time
import json
import os
from datetime import datetime

# දත්ත ගොනුව
DATA_FILE = "data.json"

# දත්ත පටවා ගැනීම
def load_data():
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    return {"tasks": [], "logs": []}

# දත්ත සුරැකීම
def save_data(data):
    with open(DATA_FILE, "w") as f:
        json.dump(data, f)

# UI සැකසුම
st.set_page_config(page_title="Task Planner", layout="wide")
data = load_data()

st.title("✨ මගේ වැඩ සැලසුම")

# ටාස්ක් එක එකතු කිරීම
task_name = st.text_input("ටාස්ක් එක ලියන්න:")
if st.button("Add Task"):
    if task_name:
        data["tasks"].append({"name": task_name, "id": str(time.time())})
        save_data(data)
        st.rerun()

# ටාස්ක් ලැයිස්තුව සහ ටයිමර් එක
st.divider()
for task in data["tasks"]:
    col1, col2 = st.columns([2, 1])
    with col1:
        st.subheader(task["name"])
    with col2:
        if st.button(f"Start {task['name']}", key=task["id"]):
            # රවුම් රූපයකින් පෙන්වීම සඳහා progress bar එක
            progress_bar = st.progress(0)
            status_text = st.empty()
            
            # පැයක ටයිමර් එක (තත්පර 3600)
            # පහසුව සඳහා මෙතන තත්පර 10ක ඇනිමේෂන් එකක් දාලා තියෙන්නේ
            for i in range(101):
                progress_bar.progress(i)
                status_text.text(f"පැය සම්පූර්ණ වෙමින් පවතී... {i}%")
                time.sleep(0.1)
            
            st.success(f"{task['name']} - පැය සම්පූර්ණයි! 🎉")
            time.sleep(1)
            st.rerun()

st.divider()
