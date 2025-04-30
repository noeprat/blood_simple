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


st.markdown('''# Heart attack ''')
st.write('''A myocardial infarction, commonly known as a heart attack, occurs when blood flow decreases or stops in one of the coronary arteries of the heart, causing infarction (tissue death) to the heart muscle.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6124376/')

st.markdown('### Epidemiology')
st.write('''Heart attack incidence was 208 cases per 100,000 person-years in 2008.''')
st.link_button('Source', 'https://www.nejm.org/doi/full/10.1056/NEJMoa0908610?casa_token=HnFkLuvEfRMAAAAA:wjRFR_g5O3RD3VEA1BAbgmToX-_h5GS1flPXH_9X4V_g89qNiiAoNoxQQEc2VtUV3eJo15-1FQ1jiBBJ')
