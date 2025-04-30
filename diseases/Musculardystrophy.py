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


st.markdown('''# Muscular dystrophy''')
st.write('''Muscular dystrophy is a group of diseases that cause progressive weakness and loss of muscle mass. In muscular dystrophy, abnormal genes (mutations) interfere with the production of proteins needed to form healthy muscle.''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(02)07815-7/abstract')

st.markdown('### Epidemiology')
st.write('''The combined prevalence for all muscular dystrophies ranges between 19.8 and 25.1 per 100,000 person-years.''')
st.link_button('Source', 'https://karger.com/ned/article/43/3-4/259/226690/Prevalence-of-Muscular-Dystrophies-A-Systematic')
