#app.py

import streamlit as st
from components.sidebar import sidebar
from components.content import content
from components.statistic_panel import statistic_panel


st.set_page_config(page_title="SYNAPS", layout="wide")


with open('styles/style.css', encoding='utf-8') as f:
    st.markdown(f'<style>{f.read()}</styles>', unsafe_allow_html=True)


left_col, center_col, right_col = st.columns([1, 5, 1.5], gap="medium", border=True)


with left_col:
    sidebar()


#with center_col:
    #content()

#with right_col:
    #statistic_panel()
