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


st.markdown('''# Malnutrition''')
st.write('''Malnutrition occurs when an organism gets too few (undernutrition) or too many nutrients (overnutrition). It affects the function and recovery of every organ system.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4951875/')

st.markdown('### Epidemiology')
st.write('''The global prevalence of malnutrition is 22.2% in 2017.''')
st.link_button('Source', 'https://globalnutritionreport.org/reports/global-nutrition-report-2018/burden-malnutrition/')
