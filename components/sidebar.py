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


    st.button("Dashboard", width="stretch",
            icon=":material/dashboard:")
    
    st.button("Preprocessing", width="stretch",
            icon=":material/monitoring:")
    
    st.button("Training", width="stretch",
        icon=":material/mediation:")
    
    st.button("Testing", width="stretch",
            icon=":material/analytics:")
    
    st.button("Experiments", width="stretch",
            icon=":material/assignment:")
    
    st.button("Settings", width="stretch",
            icon=":material/settings:")

    with st.container(border=True):

        st.markdown("""
            <div class="title-project">CURRENT PROJECT</div>
            """, unsafe_allow_html=True)

        st.write("*Model:*")
        st.caption("EEGNeX v5")

        st.write("*Dataset:*")
        st.caption("Neonatal EEG")