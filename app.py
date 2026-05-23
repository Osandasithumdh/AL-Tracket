import streamlit as st
import pandas as pd
import numpy as np
import time

# 1. පේජ් එකේ මූලික සැකසුම්
st.set_page_config(layout="wide", page_title="Daily Plan - AP Style")

# 2. දිලිසෙන Neon, 3D සහ කැරකෙන (Animation) පෙනුම ලබා දෙන CSS
st.markdown("""
    <style>
    /* මුළු ඇප් එකේම බැක්ග්‍රවුන්ඩ් එක */
    .stApp { background-color: #050505; color: white; font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif; }

    /* 3D කැරකෙන සහ දිලිසෙන මාතෘකාව */
    @keyframes rotateTitle {
        0% { transform: perspective(500px) rotateY(0deg); }
        50% { transform: perspective(500px) rotateY(10deg); }
        100% { transform: perspective(500px) rotateY(0deg); }
    }

    .lightning-title {
        font-size: 60px; font-weight: 800; text-align: center;
        background: linear-gradient(90deg, #a855f7, #06b6d4, #a855f7);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        text-shadow: 0 0 20px rgba(168, 85, 247, 0.8);
        animation: rotateTitle 4s infinite ease-in-out;
        margin-bottom: 20px;
    }

    /* Sidebar Icon Styling */
    .sidebar-icon-box {
        background: linear-gradient(145deg, #1e1e1e, #121212);
        padding: 15px; margin: 15px 0; border-radius: 20px;
        text-align: center; font-size: 25px;
        border: 1px solid rgba(255, 255, 255, 0.1);
        box-shadow: 5px 5px 15px #000, -2px -2px 10px rgba(255,255,255,0.05);
        transition: 0.4s;
    }
    .sidebar-icon-box:hover {
        transform: scale(1.1) rotate(5deg);
        box-shadow: 0 0 20px #06b6d4;
        border: 1px solid #06b6d4;
    }

    /* 3D Card Design */
    .card {
        background: rgba(25, 25, 25, 0.8);
        padding: 25px; border-radius: 25px;
        border: 1px solid rgba(168, 85, 247, 0.2);
        box-shadow: 10px 10px 30px #000;
        transition: 0.3s;
    }
    .card:hover {
        transform: translateY(-10px);
        box-shadow: 0 15px 30px rgba(168, 85, 247, 0.3);
        border: 1px solid #a855f7;
    }

    /* Neon Divider */
    .divider {
        height: 3px;
        background: linear-gradient(90deg, transparent, #06b6d4, transparent);
        margin: 20px 0;
    }
    </style>
""", unsafe_allow_html=True)

# 3. පිටු මාරු කිරීම පාලනය කිරීම (Navigation logic)
if 'page' not in st.session_state:
    st.session_state.page = 'Home'

def change_page(page_name):
    st.session_state.page = page_name

# 4. Sidebar එක නිර්මාණය (අනුරාධ සර්ගේ සයිට් එකේ වගේ අයිකන් පේළිය)
with st.sidebar:
    st.markdown("<h2 style='text-align:center; color:#06b6d4;'>AP.LK</h2>", unsafe_allow_html=True)
    st.markdown("<div style='margin-top:30px;'></div>", unsafe_allow_html=True)
    
    # බොත්තම් (අයිකන් සමඟ)
    if st.button("🏠 Home"): change_page('Home')
    if st.button("📖 Tasks"): change_page('Tasks')
    if st.button("📊 Analytics"): change_page('Analytics')
    if st.button("🔔 Notifications"): change_page('Notifications')
    if st.button("👤 Profile"): change_page('Profile')

# 5. පිටු අනුව UI එක පෙන්වීම
if st.session_state.page == 'Home':
    st.markdown('<div class="lightning-title">⚡ Daily Plan</div>', unsafe_allow_html=True)
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    col1, col2 = st.columns([1, 2])

    with col1:
        st.markdown("""
            <div class="card">
                <h3 style='color:#06b6d4;'>⏱️ Time Tracker</h3>
                <h1 style='text-align:center; text-shadow: 0 0 10px #06b6d4;'>00:30:15</h1>
                <p style='text-align:center; color:#888;'>Current Active Session</p>
            </div>
        """, unsafe_allow_html=True)
        st.write("")
        st.markdown("""
            <div class="card">
                <h3 style='color:#a855f7;'>📖 Current Task</h3>
                <p>• UI Design Implementation</p>
                <p>• Neon Glow Effects Setup</p>
            </div>
        """, unsafe_allow_html=True)

    with col2:
        st.markdown("<div class='card'>", unsafe_allow_html=True)
        st.subheader("🚀 Performance Metrics")
        c1, c2 = st.columns(2)
        with c1:
            st.write("Weekly Workload")
            chart_data = pd.DataFrame(np.random.randn(7, 1), columns=['Work'])
            st.bar_chart(chart_data)
        with c2:
            st.write("Goal Completion")
            chart_data = pd.DataFrame(np.random.randn(7, 1), columns=['Goals'])
            st.area_chart(chart_data)
        
        st.write("Overall Progress History")
        st.line_chart(pd.DataFrame(np.random.randn(20, 2)))
        st.markdown("</div>", unsafe_allow_html=True)

elif st.session_state.page == 'Tasks':
    st.markdown('<div class="lightning-title">📖 Tasks</div>', unsafe_allow_html=True)
    st.markdown("<div class='card'><h3>ඔයාගේ වැඩ ලැයිස්තුව මෙතනින් බලන්න</h3></div>", unsafe_allow_html=True)
    st.checkbox("Create daily declaration")
    st.checkbox("Approve task links")

elif st.session_state.page == 'Analytics':
    st.markdown('<div class="lightning-title">📊 Analytics</div>', unsafe_allow_html=True)
    st.write("Advanced charts and data report will be here.")
    st.line_chart(np.random.randn(50, 3))

# ෆුටර් එක (Footer)
st.markdown("<br><p style='text-align:center; color:#444;'>Powered by AP.LK Style Dashboard</p>", unsafe_allow_html=True)
