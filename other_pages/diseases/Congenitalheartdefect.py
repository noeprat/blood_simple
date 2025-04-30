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


st.markdown('''# Congenital heart defect''')
st.write('''Congenital heart defects are abnormalities in heart structure that occur before birth. They can affect how blood flows through the heart and out to the rest of the body. They can vary from mild (such as a small hole in the heart) to severe (such as missing or poorly formed parts of the heart).''')
st.link_button('Source', 'https://link.springer.com/article/10.1007/s12013-015-0551-6')

st.markdown('### Epidemiology')
st.write('''The prevalence is 9.1 per 1'000 live births.''')
st.link_button('Source', 'https://www.jacc.org/doi/abs/10.1016/j.jacc.2011.08.025')
