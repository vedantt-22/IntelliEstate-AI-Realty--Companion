import streamlit as st
import os

def load_sidebar():
    # IntelliEstate Title
    st.sidebar.markdown("## 🏡 IntelliEstate")
    st.sidebar.success("👈 Select a section to begin exploring!")

    # Home Link
    st.sidebar.page_link("Home.py", label="🏠 Home")

    # Pages Section
    st.sidebar.markdown("### 📂 pages")
    pages_dir = "pages"
    if os.path.exists(pages_dir):
        for file in sorted(os.listdir(pages_dir)):
            if file.endswith(".py"):
                page_path = f"{pages_dir}/{file}"
                page_name = file.replace(".py", "").replace("_", " ").title()
                icon = "📄"
                if "analysis" in file.lower():
                    icon = "📊"
                elif "predictor" in file.lower():
                    icon = "💸"
                elif "recommender" in file.lower():
                    icon = "🏠"
                st.sidebar.page_link(page_path, label=f"{icon} {page_name}")

    # Theme Setup
    if "dark_mode" not in st.session_state:
        st.session_state.dark_mode = False

    def toggle_theme():
        st.session_state.dark_mode = not st.session_state.dark_mode

    st.sidebar.markdown("---")
    st.sidebar.button("🌗 Toggle Dark Mode", on_click=toggle_theme, key="sidebar_toggle")
