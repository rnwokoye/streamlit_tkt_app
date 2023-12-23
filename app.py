import streamlit as st
from create_tkt import *
from login import log_in


st.title("Traffic Ticket Assignement :male-pilot: 	:vertical_traffic_light:")
# :camera:

log_in()
username = st.session_state.username
name = st.session_state.name
if username is not None and name is not None:
    if is_admin(name):
        admin_page.display_data()
    else:
        insert_offense(run_program(username))
