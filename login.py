import streamlit as st
import streamlit_authenticator as stauth
import yaml
from yaml.loader import SafeLoader


def log_in():
    with open("config.yaml") as file:
        config = yaml.load(file, Loader=SafeLoader)

    authenticator = stauth.Authenticate(
        config["credentials"],
        config["cookie"]["name"],
        config["cookie"]["key"],
        config["cookie"]["expiry_days"],
        config["preauthorized"],
    )

    authenticator.login()

    if st.session_state["authentication_status"]:
        st.write(f'Welcome *{st.session_state["name"]}*')
        authenticator.logout(location="sidebar")
    elif st.session_state["authentication_status"] is False:
        st.error("Username/password is incorrect")
    elif st.session_state["authentication_status"] is None:
        st.warning("Please enter your username and password")
