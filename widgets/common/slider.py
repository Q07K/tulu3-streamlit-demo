import streamlit as st


def hyperparameter_slider(
    name: str,
    discription: str | None = None,
    min_value: float | None = None,
    max_value: float | None = None,
):
    lower_name = name.lower()
    key = "_".join(lower_name.split())
    st.slider(
        key=key,
        label=name,
        help=discription,
        min_value=min_value,
        max_value=max_value,
    )
