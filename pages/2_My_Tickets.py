import streamlit as st
import pandas as pd
from create_tkt import conn


st.title("Page 2 Here")


def get_my_tickets():
    officer = st.session_state.username

    query = f""" 
    SELECT * FROM traffic_tickets WHERE officer_name = '{officer}';
    """

    if officer is not None:
        data = conn.query(query)
        st.dataframe(data)


if st.button("Get Tickets"):
    get_my_tickets()
