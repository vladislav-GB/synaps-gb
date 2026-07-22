import streamlit as st

def statistic_panel():
    st.subheader("Model Status")
    st.divider()

    col1, col2 = st.columns(2)
    col1.metric("Accuracy", "94.2%")
    col2.metric("Loss", "0.045")