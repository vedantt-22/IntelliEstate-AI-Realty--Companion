import streamlit as st
import os
from sidebar import load_sidebar

load_sidebar()
# ---------------- Page Config ---------------- #
st.set_page_config(
    page_title="Gurgaon Real Estate Analytics App",
    page_icon="🏡",
    layout="wide"
)
st.markdown("""
    <style>
    [data-testid="stSidebarNav"] {display: none;}
    </style>
""", unsafe_allow_html=True)
# ---------------- Persistent Dark Mode ---------------- #
if "dark_mode" not in st.session_state:
    st.session_state.dark_mode = False

def toggle_theme():
    st.session_state.dark_mode = not st.session_state.dark_mode

# ---------------- Custom Styles ---------------- #
light_theme = """
    <style>
    body { background-color: white; color: black; }
    .centered { display: flex; flex-direction: column; align-items: center; padding: 2rem; }
    .hero-title { font-size: 42px; font-weight: 800; color: #264653; text-align: center; }
    .intro-text { font-size: 18px; color: #555; text-align: center; max-width: 900px; }
    ul.feature-list { font-size: 17px; color: #333; line-height: 1.8; margin-left: 1.5rem; }
    </style>
"""

dark_theme = """
    <style>
    body { background-color: #111; color: #eee; }
    .centered { display: flex; flex-direction: column; align-items: center; padding: 2rem; }
    .hero-title { font-size: 42px; font-weight: 800; color: #f4a261; text-align: center; }
    .intro-text { font-size: 18px; color: #ccc; text-align: center; max-width: 900px; }
    ul.feature-list { font-size: 17px; color: #ccc; line-height: 1.8; margin-left: 1.5rem; }
    </style>
"""

st.markdown(dark_theme if st.session_state.dark_mode else light_theme, unsafe_allow_html=True)

# ---------------- Main Content ---------------- #
st.markdown("""
<div class="centered">
    <div class="hero-title">Welcome to Gurgaon Real Estate Analytics 👋</div>
    <div class="intro-text">
        Explore sector-wise insights, price trends, bedroom configurations and more to make informed investment and planning decisions across Gurgaon’s property market.
    </div>
</div>

<ul class="feature-list">
    <li>🗺️ <b>Sector GeoMap</b> – Visualize price per sqft across locations</li>
    <li>🌀 <b>WordCloud</b> – Extract popular keywords from property features</li>
    <li>📈 <b>Area vs Price</b> – See how built-up area affects pricing</li>
    <li>📊 <b>Bedroom Distribution</b> – Understand BHK trends by sector</li>
    <li>📉 <b>Price Distribution</b> – Compare prices across property types</li>
</ul>
""", unsafe_allow_html=True)

# ---------------- Footer ---------------- #
st.markdown("""
<hr>
<div style='text-align: center; font-size: 14px;'>
    Built with ❤️ using Streamlit · IntelliEstate © 2025
</div>
""", unsafe_allow_html=True)

