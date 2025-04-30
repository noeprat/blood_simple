import streamlit as st

st.markdown(
    '''
    <style>
    .stApp {
        background-color: #F2D2BD;
        color: black;
    }
    </style>
    ''',
    unsafe_allow_html=True
)


st.markdown('''# Respiratory acidosis''')
st.write('''Respiratory acidosis is a state in which there is usually a failure of ventilation and an accumulation of carbon dioxide.''')
st.link_button('Source', 'https://europepmc.org/article/med/11262556')
