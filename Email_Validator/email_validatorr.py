import streamlit as st
import email_validator as ev

st.title('Email Validator')

email = st.text_input('Enter your email address ')
verify = st.button('Verify')

if verify:
    try:
        valid = ev.validate_email(email)
        email = valid.email
        st.success('Email is Valid')

    except ev.EmailNotValidError as e:
        st.error("Invalid Email")



