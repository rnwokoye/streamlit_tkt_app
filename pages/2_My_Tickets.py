import streamlit as st
import pandas as pd
from create_tkt import conn


officer = st.session_state.name
username = st.session_state.username
st.title(f"Tickets for {officer}")


def get_my_tickets():
    query = f""" 
    SELECT * FROM traffic_tickets WHERE officer_name = '{username}';
    """

    if officer is not None:
        data = conn.query(query)
        st.dataframe(data)


if st.button("Get Tickets"):
    get_my_tickets()
