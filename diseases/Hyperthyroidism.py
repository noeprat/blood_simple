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


st.markdown('''# Hyperthyroidism''')
st.write('''Thyroid is a butterfly-shaped gland in the front of the neck, which makes hormones that control the way the body uses energy. Hyperthyroidism means the thyroid gland makes more thyroid hormones than the body needs. This hypermetabolic state is leading to an increased demand for glucose. 
It may be caused by Graves disease (an autoimmune disease in which the body’s own cells attack the thyroid gland).''')
st.link_button('Source 1', 'https://academic.oup.com/edrv/article/31/5/663/2354765')
st.link_button('Source 2', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8987680/')

st.markdown('### Epidemiology')
st.write('''The prevalence of overt hyperthyroidism ranges from 0.2% to 1.3%.''')
st.link_button('Source', 'https://www.nature.com/articles/nrendo.2018.18')
