import streamlit as st


def history_block(title: str):
    left_field, right_field = st.columns([0.8, 0.2])

    with left_field.container():
        st.button(
            label=title,
            key=f"title_{title}",
            use_container_width=True,
        )

    with right_field.container():
        st.button(
            label="🗑️",
            key=f"delete_{title}",
            use_container_width=True,
        )
