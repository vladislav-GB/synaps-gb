#sidebar.py

import streamlit as st


def sidebar():

    st.markdown("""
    <div class="logo">SYNAPS</div>
    """, unsafe_allow_html=True)

    st.markdown("""
    <div class="subtitle">research platform</div>
    """, unsafe_allow_html=True)

    st.markdown(
        '<div class="divider"></div>',
        unsafe_allow_html=True
    )

    st.button("Preprocessing")
    st.button("Training")
    st.button("Testing")
    st.button("Settings")