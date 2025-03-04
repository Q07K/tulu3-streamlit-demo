import streamlit as st

from widgets.slider_widget import hyperparameter_slider


def sidebar():
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
