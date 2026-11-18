import streamlit as st

# Temporary debug lines
print("--- STREAMLIT SECRETS DEBUG ---")
print("Available keys:", list(st.secrets.keys())) 
print("-------------------------------")


from supabase import create_client, Client

supabase: Client = create_client(
    st.secrets["SUPABASE_URL"],
    st.secrets["SUPABASE_KEY"]
)
# This is call database Instance. On the basis of this we will run all queries. supabase is instance_name       