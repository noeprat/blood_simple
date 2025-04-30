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


st.markdown('''# Cushing syndrome''')
st.write('''Cushing’s syndrome is a rare disorder that results from prolonged and pathological exposure to excess glucocorticoids. Glucocorticoids have pain-relieving and anti-inflammatory effects, which is the reason why they are abused for doping purposes.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3095520/')

st.markdown('### Epidemiology')
st.write('''The incidence of Cushing’s syndrome varies from 2 to 3 cases per million population per year.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3095520/')
