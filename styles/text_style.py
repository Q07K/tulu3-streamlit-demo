import streamlit as st


def set_title():
    return st.markdown(
        body="""<style>
    h1 {
        text-align: center;
    }
    </style>""",
        unsafe_allow_html=True,
    )
