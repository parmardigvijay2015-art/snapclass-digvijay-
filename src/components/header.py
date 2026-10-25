import streamlit as st


def header_home():

    logo_url = "https://img.magnific.com/premium-vector/professor-icon-icon-colored-shapes_969863-51453.jpg?w=360"

    st.markdown(f"""
        <div style="display: flex; flex-direction: column; aligh-items: center; justify-content: enter margin-bottom: 30px; margin-top: 30px;">
            <img src= {logo_url} style="height: 200px";/>
            <h1 style="text-align: center; color:#E0E3FF">SNAP<br/>CLASS</h1>
        </div>
""", unsafe_allow_html=True)