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


st.markdown('''# Hodgkin lymphoma''')
st.write('''Hodgkin lymphoma is a type of cancer that develops in the lymph system. The lymph system is part of the immune system. It helps protect the body from infection and disease.''')
st.link_button('Source', 'https://www.jci.org/articles/view/61245')

st.markdown('### Epidemiology')
st.write('''A total of 83'000 new cases of Hodgkin lymphoma and 23'000 deaths from it were estimated in 2020.''')
st.link_button('Source', 'https://onlinelibrary.wiley.com/doi/abs/10.1002/ijc.33948?casa_token=eZQHo0VRFCEAAAAA:JEy5W8diM6MathEAyztin1VGWFAoJae-6pOIBfUimDB2YMGvMo2GQ4YcUfo4FekEGkMKK5Mat0jELH7r')
