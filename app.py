import streamlit as st
import pandas as pd
import numpy as np

# Page configuration
st.set_page_config(layout="wide", page_title="Daily Plan")

# Custom CSS for Neon Glow, 3D effects, and Colorful UI
st.markdown("""
    <style>
    /* Dark Background */
    .stApp { background-color: #050505; color: white; }
    
    /* Sidebar Icons Style */
    [data-testid="stSidebar"] {
        background-color: #121212;
        padding-top: 50px;
    }
    
    .icon-box {
        background: linear-gradient(145deg, #1e1e1e, #0f0f0f);
        padding: 15px; margin: 10px; border-radius: 15px;
        text-align: center; font-size: 24px;
        box-shadow: 0 0 10px rgba(0,255,255,0.2);
        transition: 0.3s;
    }
    
    /* 3D Lightning Title */
    .lightning-title {
        font-size: 50px; font-weight: 800;
        text-align: center;
        text-shadow: 0 0 20px #a855f7, 0 0 40px #06b6d4;
        background: -webkit-linear-gradient(left, #a855f7, #06b6d4);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        margin-bottom: 30px;
    }
    
    /* Neon Glow Cards */
    .card {
        background: rgba(30, 30, 30, 0.6);
        padding: 20px; border-radius: 20px;
        border: 1px solid rgba(255,255,255,0.1);
        box-shadow: 0 0 15px rgba(168, 85, 247, 0.3);
        margin-bottom: 20px;
    }
    </style>
""", unsafe_allow_html=True)

# Sidebar with colorful buttons
with st.sidebar:
    st.markdown("### ANURA")
    icons = ["🏠", "📖", "🔔", "📊", "🛍️", "👤", "📄"]
    for icon in icons:
        st.markdown(f'<div class="icon-box">{icon}</div>', unsafe_allow_html=True)

# Main Title
st.markdown('<div class="lightning-title">⚡ Daily Plans & Task</div>', unsafe_allow_html=True)

# Main Dashboard Grid
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="card"><h3>⏱️ Time Tracker</h3><p style="font-size:30px; color:#06b6d4;">00:30</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>📖 Task</h3><p>• Review Project</p><p>• Update Code</p></div>', unsafe_allow_html=True)

with col2:
    c1, c2 = st.columns(2)
    with c1:
        st.write("📈 Weekly Trends")
        st.bar_chart(pd.DataFrame(np.random.randn(10, 1)))
    with c2:
        st.write("📊 Project Distribution")
        st.area_chart(pd.DataFrame(np.random.randn(10, 1)))
    
    st.write("🚀 Overall Progress")
    st.line_chart(pd.DataFrame(np.random.randn(10, 2)))
