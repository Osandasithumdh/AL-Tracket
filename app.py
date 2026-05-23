import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(layout="wide", page_title="Daily Plan")

# CSS for custom styling (Sidebar and Cards)
st.markdown("""
    <style>
    /* Main Background */
    .stApp { background-color: #0e1117; }
    
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: #1c1f26;
        width: 100px;
    }
    
    /* Title styling */
    .title-text { 
        font-size: 40px; font-weight: bold; 
        background: -webkit-linear-gradient(left, #a855f7, #06b6d4); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
        margin-bottom: 20px;
    }
    
    /* Card design */
    .card { background-color: #1c1f26; padding: 20px; border-radius: 15px; color: white; }
    </style>
""", unsafe_allow_html=True)

# Sidebar with Icons
with st.sidebar:
    st.markdown("### ANURA")
    st.button("🏠")
    st.button("📖")
    st.button("🔔")
    st.button("📊")
    st.button("🛍️")
    st.button("👤")
    st.button("📄")

# Main Content
st.markdown('<div class="title-text">⚡ Daily Plan</div>', unsafe_allow_html=True)

col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="card"><h3>⏱️ Time Tracker</h3><p>00:30</p></div>', unsafe_allow_html=True)
    st.markdown("<br>", unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>📖 Task</h3><p>List of pending tasks here...</p></div>', unsafe_allow_html=True)

with col2:
    # Charts Row 1
    c1, c2 = st.columns(2)
    with c1:
        st.write("Weekly Trends")
        st.bar_chart(pd.DataFrame(np.random.randn(10, 1)))
    with c2:
        st.write("Project Distribution")
        st.area_chart(pd.DataFrame(np.random.randn(10, 1)))
    
    # Chart Row 2
    st.write("Overall Progress")
    st.line_chart(pd.DataFrame(np.random.randn(10, 2)))
