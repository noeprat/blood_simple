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


st.markdown('''# Ketoacidosis''')
st.write('''Ketoacidosis occurs when the body starts breaking down fat at a too fast rate. The liver processes the fat into a fuel called ketones, which causes the blood to become acidic.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK534848/')
