
import streamlit as st

def main():
    st.header("This is title")
    name = st.text_input("Enter your name")  # put in any variable sothat use in python fnx.


    col1, col2 = st.columns(2, gap="small")

    with col1:
        if st.button("Hi", type="primary", key="btn1", width="stretch"):
            print("Hi", name)

    with col2:
        if st.button("Bye", type="secondary", key="btn2", width="stretch"):
            print("Bye", name)

    st.markdown("""
        <div>
        <img src="https://th.bing.com/th/id/OIGP.hxKopWQ0tuZ7ZnAf5kO5?w=193&h=135&c=8&rs=1&qlt=90&r=0&o=6&dpr=1.2&pid=3.1&rm=2" />
        <h1>Snap Class </h1>
        </div> 
        <style>
           .st-key-btn2 button{
                background-color: orange !important;
            }
        </style>
""", unsafe_allow_html=True)

main()

    