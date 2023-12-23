import streamlit as st
import streamlit_authenticator as stauth


def log_in():
    # Make a deep copy of the authentication config to avoid modifying st.secrets
    authentication_config = dict(st.secrets["credentials"])
    usernames = authentication_config["usernames"]
    # Convert the usernames to lowercase to match the expectation of the stauth.Authenticate class
    authentication_config["usernames"] = {
        key.lower(): value for key, value in usernames.items()
    }

    authenticator = stauth.Authenticate(
        authentication_config,
        st.secrets["cookie"]["name"],
        st.secrets["cookie"]["key"],
        st.secrets["cookie"]["expiry_days"],
        st.secrets["preauthorized"],
    )

    authenticator.login("Login", "main")
    name = st.session_state.name
    username = st.session_state.username

    if st.session_state["authentication_status"]:
        st.write(f'Welcome *{st.session_state["name"]}*')
        authenticator.logout("Logout", "sidebar", key="unique_key")
        if st.button("Reset"):
            authenticator.reset_password(st.session_state["username"], "Reset_password")
        return username, name
    elif st.session_state["authentication_status"] is False:
        st.error("Username/password is incorrect")
        if st.button("Forgot password"):
            authenticator.forgot_password("Forgot_Passsword")
    elif st.session_state["authentication_status"] is None:
        st.warning("Please enter your username and password")
        if st.button("register"):
            authenticator.register_user("Register From")
            st.write("Done")
