import streamlit as st

from entities.chat_message_entity import ChatMessageEntity
from styles import chat_message_style, text_style
from widgets.chat_widgets import first_chat
from widgets.common.slider import hyperparameter_slider

# Set styles
text_style.set_title()
chat_message_style.set_user_message_field()
chat_message_style.disable_user_messagge_icon()
chat_message_style.disable_ai_messagge_icon()

# Main page
with st.sidebar:
    st.subheader(body="Models")
    st.selectbox(
        label="Model Name",
        options=["Tülu3-8B", "Tülu3-70B"],
        key="model_name",
    )
    st.subheader(body="Hyperparameters")
    hyperparameter_slider(name="Max Token")
    hyperparameter_slider(name="Temperature")
    hyperparameter_slider(name="Top K")

if "messages" not in st.session_state:
    st.session_state.messages = []

if not st.session_state.messages:
    if user_query := first_chat():
        st.session_state.messages.append(
            ChatMessageEntity(
                rule="user",
                content=user_query,
            )
        )
        st.rerun()
else:
    for message in st.session_state.messages:
        message: ChatMessageEntity
        with st.chat_message(name=message.rule):
            st.markdown(body=message.content)

    if user_query := st.chat_input():
        with st.chat_message(name="user"):
            st.markdown(body=user_query)
        st.session_state.messages.append(
            ChatMessageEntity(
                rule="user",
                content=user_query,
            )
        )

        with st.chat_message(name="ai"):
            st.markdown(body="hi")
        st.session_state.messages.append(
            ChatMessageEntity(
                rule="ai",
                content="hi",
            )
        )
