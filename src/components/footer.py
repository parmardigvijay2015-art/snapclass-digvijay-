import streamlit as st

def footer_home():
    logo_url= "https://i.ytimg.com/vi/bZCYHpIuJU4/hqdefault.jpg"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p style="font-weight: bold; color: white;">Created with <span style="color: #C51104;">&#x2764;</span> by</p>
            <img src="{logo_url}" style="max-height:50px" />
        </div>
    """, unsafe_allow_html=True)

def footer_dashboard():
    logo_url= "https://i.ytimg.com/vi/bZCYHpIuJU4/hqdefault.jpg"

    st.markdown(f"""
        <div style="margin-top:2rem; display:flex; gap:6px; justify-content:center; items-align:center">
            <p style="font-weight: bold; color: black;">Created with <span style="color: #C51104;">&#x2764</span> by</p>
            <img src="{logo_url}" style="max-height:50px" />
        </div>
    """, unsafe_allow_html=True)