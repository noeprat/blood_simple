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


st.markdown('''# Alcohol use disorder''')
st.write('''Alcohol use disorder is a medical condition involving heavy or frequent alcohol drinking even when it causes problems, emotional distress or physical harm. It is a disease of brain function and requires medical and psychological treatments to control it.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK436003/')

st.markdown('### Epidemiology')
st.write('''AUDs are among the most prevalent mental disorders globally, affecting 8.6% of men and 1.7% of women in 2016.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6966598/')
