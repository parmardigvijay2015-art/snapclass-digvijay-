import streamlit as st
from src.components.header import header_home
from src.components.footer import footer_home
from src.ui.base_layout import style_base_layout, style_background_home


def home_screen():
    header_home()
    style_background_home()
    style_base_layout()

    
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("I'm Student")
        st.image("https://img.icons8.com/emoji/1200/person-student.jpg", width=120)
        if st.button("Student Portal", type= "primary", icon=":material/arrow_outward:", icon_position="right"):
            st.session_state["login-type"] = "student"
            st.rerun()
        
    with col2:
        st.subheader("I'm Teacher")
        st.image("https://png.pngtree.com/png-vector/20220719/ourmid/pngtree-people-avatar-icons---teacher-speaker-symbol-front-vector-png-image_37974884.png", width=100)
        if st.button("Teacher Portal", type= "primary", icon=":material/arrow_outward:", icon_position="right"):
            st.session_state["login-type"] = "teacher"
            st.rerun()

    footer_home()