import streamlit as st
from src.database.config import supabase
import time
from src.database.db import enroll_student_to_subject

@st.dialog("Quick Enrollment")
def auto_enroll_dialog(subject_code):
    student_id = st.session_state.student_data["student_id"]

    try:
        res = supabase.table("subjects").select("subject_id, name").eq("subject_code", subject_code).execute()

    except Exception as e:
        st.error(f"Database error (subjects): {e}")
        return


    if not res.data:
        st.error("Subject code not found")
        if st.button("close"):
            st.query_params.clear()
            st.rerun()
        return

    subject = res.data[0]


    try:
        check = supabase.table("subject_students").select("*").eq("subject_id", subject["subject_id"]).eq("student_id", student_id).execute()

    except Exception as e:
        st.error(f"Database error (subject_students): {e}")
        return

    
    if check.data:
        st.info("You are already enrolled!")
        if st.button("Got it!"):
            st.query_params.clear()
            st.rerun()
        return

    st.markdown(f"Would you like to enroll in **{subject['name']}**?")

    col1, col2 = st.columns(2)

    with col1:
        if st.button("No Thanks!"):
            st.query_params.clear()
            st.rerun()

    with col2:
        try:
            if st.button("Yes Enroll Now!", type="primary", use_container_width=True):
                enroll_student_to_subject(student_id, subject["subject_id"])
                st.success("Joined sucessfully!")
                st.query_params.clear()
                time.sleep(1.5)
                st.rerun()

        except Exception as e:
            st.error(f"Enrollment failed: {e}")