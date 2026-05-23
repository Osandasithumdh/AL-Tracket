import streamlit as st
import pandas as pd
import numpy as np

# Page Layout
st.set_page_config(layout="wide", page_title="Daily Plan")

# Custom CSS for Dark Mode & Styling
st.markdown("""
    <style>
    .main { background-color: #0e1117; }
    .title-text { 
        font-size: 40px; font-weight: bold; 
        background: -webkit-linear-gradient(left, #a855f7, #06b6d4); 
        -webkit-background-clip: text; -webkit-text-fill-color: transparent; 
    }
    .card { background-color: #1c1f26; padding: 20px; border-radius: 15px; margin-bottom: 20px; }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<div class="title-text">⚡ Daily Plan</div>', unsafe_allow_html=True)
st.write("---")

# Layout: Creating Columns for the Dashboard
col1, col2 = st.columns([1, 2])

with col1:
    st.markdown('<div class="card"><h3>⏱️ Time Tracker</h3><p>Active Task Tracking...</p></div>', unsafe_allow_html=True)
    st.markdown('<div class="card"><h3>📖 Tasks</h3><ul><li>Create work declaration</li><li>Complete report</li></ul></div>', unsafe_allow_html=True)

with col2:
    # Charts Section
    st.subheader("📊 Performance Analytics")
    
    c3, c4 = st.columns(2)
    with c3:
        st.write("Weekly Work Trends")
        st.bar_chart(pd.DataFrame(np.random.randn(10, 1)))
    with c4:
        st.write("Project Distribution")
        st.area_chart(pd.DataFrame(np.random.randn(10, 1)))
    
    st.write("Overall Progress")
    st.line_chart(pd.DataFrame(np.random.randn(10, 2)))
