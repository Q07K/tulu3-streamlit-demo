import streamlit as st


def set_user_message_field():
    return st.markdown(
        body="""<style>
    .st-emotion-cache-1c7y2kd {
        flex-direction: row-reverse;
        text-align: right;
        border-radius: 25px;
        background-color: #F0EBE3;
        padding: 8px 16px;
    }
    </style>""",
        unsafe_allow_html=True,
    )


def disable_user_messagge_icon():
    return st.markdown(
        body="""<style>
        .st-emotion-cache-1ghhuty {
        display: none;
        }
        </style>""",
        unsafe_allow_html=True,
    )


def disable_ai_messagge_icon():
    return st.markdown(
        body="""<style>
        .st-emotion-cache-bho8sy {
        display: none;
        }
        </style>""",
        unsafe_allow_html=True,
    )
