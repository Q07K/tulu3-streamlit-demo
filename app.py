import streamlit as st

from components import chat_component, sidebar_component
from entities.chat_entity import ChatMessageEntity
from styles import button_style, chat_style, font_style, text_style

# Set styles
font_style.set_font()
text_style.set_title()
chat_style.set_user_message_field()
chat_style.disable_user_messagge_icon()
chat_style.disable_ai_messagge_icon()
button_style.set_button()


# Main page
if "messages" not in st.session_state:
    st.session_state.messages = []


sidebar_component.sidebar()

if not st.session_state.messages:
    if user_query := chat_component.first_chat():
        st.session_state.messages.append(
            ChatMessageEntity(
                rule="user",
                content=user_query,
            )
        )
        st.session_state.messages.append(
            ChatMessageEntity(
                rule="ai",
                content="hi",
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
