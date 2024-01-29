import streamlit as st

from create_tkt import *
from login import log_in

# from create_tkt import *


st.title("Traffic Ticket Assignement :male-pilot: 	:vertical_traffic_light:")
# :camera:

log_in()
name = st.session_state.name
st.write(name)
if name is not None:
    if is_admin(name):
        admin_page.display_data()
    else:
        insert_offense(run_program(name))
