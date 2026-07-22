#content.py

import streamlit as st

def content():
    st.title("EEG Signal Analysis")
    st.caption(f"Current section: {st.session_state.get('active_page', 'Dashboard')}")
    st.divider()
    
    # Заглушка под график
    st.info("Plotly Graph Area will be displayed here.")