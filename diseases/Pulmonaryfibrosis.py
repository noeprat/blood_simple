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


st.markdown('''# Pulmonary fibrosis''')
st.write('''Pulmonary fibrosis is a group of serious lung diseases that affect the respiratory system. Pulmonary fibrosis scars and thickens lung tissue. It impacts the connecting tissue in the lung and the alveoli (air sacs inside the lungs). The lung damage gradually gets worse over time. Hard, stiff lung tissues don’t expand as well as they should, making it harder to breathe.''')
st.link_button('Source', 'https://rupress.org/jem/article/208/7/1339/41120/Integrating-mechanisms-of-pulmonary')

st.markdown('### Epidemiology')
st.write('''Prevalence is estimated to range from 4.0 per 100'000 persons aged 18-34 years to 227.2 per 100'000 among those 75 years or older.''')
st.link_button('Source', 'https://www.atsjournals.org/doi/full/10.1164/rccm.200602-163OC')
