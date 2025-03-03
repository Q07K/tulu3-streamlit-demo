import streamlit as st


def first_chat():
    _ = st.container(height=200, border=False)
    field = st.container()

    with field:
        st.title(body="무엇을 도와드릴까요?")
        user_query = st.chat_input("test", key="user_query")
    return user_query
