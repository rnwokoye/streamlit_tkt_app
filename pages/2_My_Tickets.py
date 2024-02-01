import streamlit as st
import pandas as pd
from create_tkt import conn


# try:
#     officer = st.session_state.name
#     username = st.session_state.username
# except AttributeError as e:
#     st.warning("No logged on User")

st.title("Officer Tickets")


def get_my_tickets():
    try:
        officer_name = st.session_state.name
        username = st.session_state.username
    except AttributeError as e:
        st.warning("No logged on User")

    query = f"""
    SELECT * FROM traffic_tickets WHERE officer_name = '{officer_name}';
    """

    if officer_name is not None:
        data = conn.query(query, ttl=0)
        st.dataframe(data)


if st.button("Get Tickets"):
    get_my_tickets()
