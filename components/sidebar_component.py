import streamlit as st

from widgets.chat_history_widget import history_block
from widgets.slider_widget import hyperparameter_slider


def sidebar():
    with st.sidebar:
        with st.expander(label="Model Settings", icon="⚙️"):
            st.subheader(body="Model")
            st.selectbox(
                label="Model Name",
                options=["Tülu3-8B", "Tülu3-70B"],
                key="model_name",
                label_visibility="collapsed",
            )
            st.subheader(body="Hyperparameters")
            hyperparameter_slider(name="Max Token")
            hyperparameter_slider(
                name="Temperature", min_value=0.0, max_value=1.0
            )
            hyperparameter_slider(name="Top K")

            st.subheader(body="Prompt")
            st.text_area(label="system prompt")

        st.subheader(body="Chat history")
        for i in range(10):
            history_block(title=str(i))
