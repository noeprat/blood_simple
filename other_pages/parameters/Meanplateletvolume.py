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


st.markdown('''# Mean platelet volume''')
st.write('''An MPV blood test measures the average size of the platelets. Platelets are tiny blood cells that bud from cells in the bone marrow (the spongy tissue inside of bones). Platelets form clots when there is damage to a blood vessel. ''')
st.link_button('Source', 'https://link.springer.com/chapter/10.1007/978-3-642-29423-5_1')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Cancer.py', label='''Cancer ''')
st.page_link('other_pages/diseases/Diabetes.py', label=''' Diabetes ''')
st.page_link('other_pages/diseases/Cardiovasculardisease.py', label=''' Cardiovascular disease ''')
st.page_link('other_pages/diseases/Preeclampsia.py', label=''' Preeclampsia ''')
st.page_link('other_pages/diseases/Crohnsdisease.py', label=''' Crohn’s disease ''')
st.page_link('other_pages/diseases/Hyperthyroidism.py', label=''' Hyperthyroidism ''')
st.page_link('other_pages/diseases/Immunethrombocytopenia.py', label=''' Immune thrombocytopenia''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Aplasticanemia.py', label='''Aplastic anemia ''')
st.page_link('other_pages/diseases/Lupus.py', label=''' Lupus ''')
st.page_link('other_pages/diseases/WiskottAldrichsyndromerare.py', label=''' Wiskott-Aldrich syndrome (rare) ''')
st.page_link('other_pages/diseases/Thrombocytosis.py', label=''' Thrombocytosis''')
