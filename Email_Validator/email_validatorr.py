import streamlit as st
import email_validator as ev

st.title('Email Validator')

your_mail = st.text_input('Enter your email address ')
verify = st.button('Verify')

if verify:
    try:
        valid = ev.validate_email(your_mail)
        your_mail = valid.your_mail
        st.success('Email is Valid')

    except ev.EmailNotValidError as e:
        st.error("Invalid Email")



