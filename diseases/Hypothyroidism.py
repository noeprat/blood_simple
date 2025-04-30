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


st.markdown('''# Hypothyroidism''')
st.write('''Thyroid is a butterfly-shaped gland in the front of the neck, which makes hormones that control the way the body uses energy. Hypothyroidism means the thyroid gland makes less thyroid hormones than the body needs.
The most common form of hypothyroidism is an disease called Hashimoto’s thyroiditis.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC8987680/')

st.markdown('### Epidemiology')
st.write('''The prevalence of hypothyroidism ranges from 1% to 2%, rising to 7% in individuals aged between 85 and 89 years.''')
st.link_button('Source', 'https://www.nature.com/articles/nrendo.2018.18')
