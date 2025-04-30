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


st.markdown('''# Metabolic alkalosis''')
st.write('''Metabolic alkalosis is when bases or alkali build up in the body fluids. In metabolic alkalosis there is excess of bicarbonate in the body fluids. Bicarbonate is a base. It’s a form of carbon dioxide — a waste byproduct after the body converts food to energy.''')
st.link_button('Source', 'https://journals.lww.com/jasn/fulltext/2000/02000/metabolic_alkalosis.20.aspx')
