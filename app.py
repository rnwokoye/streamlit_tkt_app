import streamlit as st

from create_tkt import *
from login import log_in
import admin_page

# # from create_tkt import *

# conn = st.connection("cockroachdb", type="sql")
# # with conn.session as s:
# #     st.write(s)


st.title("Traffic Ticket Assignement :male-pilot: 	:vertical_traffic_light:")
# :camera:

log_in()
name = st.session_state.name
if name is not None:
    if is_admin(name):
        admin_page.display_data()
        admin_page.get_test_table()
        admin_page.test_insert_data()
    else:
        insert_offense(run_program(name))
