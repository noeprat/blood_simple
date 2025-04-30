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


st.markdown('''# Total protein''')
st.write('''A total serum protein test measures the total amount of protein in the blood. It also measures the amounts of two major groups of proteins in the blood: albumin and globulin. 
Albumin is made mainly in the liver. It helps keep the blood from leaking out of blood vessels. It also helps carry some medicines and other substances through the blood and is important for tissue growth and healing.
Globulin is made up of different proteins called alpha, beta, and gamma types. Some globulins are made by the liver, while others are made by the immune system.''')
st.link_button('Source', 'https://www.healthlinkbc.ca/tests-treatments-medications/medical-tests/total-serum-protein')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.markdown('Dehydratation ')
st.page_link('other_pages/diseases/Blooddisease.py', label=''' Blood disease ''')
st.page_link('other_pages/diseases/Kidneydisease.py', label=''' Kidney disease ''')
st.page_link('other_pages/diseases/Liverdisease.py', label=''' Liver disease''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Malnutrition.py', label='''Malnutrition ''')
st.page_link('other_pages/diseases/Kidneydisease.py', label=''' Kidney disease ''')
st.page_link('other_pages/diseases/Liverdisease.py', label=''' Liver disease ''')
st.page_link('other_pages/diseases/Crohnsdisease.py', label=''' Crohn's disease ''')
st.page_link('other_pages/diseases/Hyperthyroidism.py', label=''' Hyperthyroidism ''')
st.page_link('other_pages/diseases/Heartfailure.py', label=''' Heart failure''')
