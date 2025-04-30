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


st.markdown('''# Albumin''')
st.write('''Albumin is a protein made by the liver. Albumin enters the bloodstream and helps keep fluid from leaking out of the blood vessels into other tissues. It is also carries hormones, vitamins, and enzymes throughout the body. ''')
st.link_button('Source', 'https://www.mdpi.com/2673-8392/1/1/9')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.markdown('Dehydratation ')
st.page_link('other_pages/diseases/Hypothyroidism.py', label=''' Hypothyroidism''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Liverdisease.py', label='''Liver disease ''')
st.page_link('other_pages/diseases/Kidneydisease.py', label=''' Kidney disease ''')
st.page_link('other_pages/diseases/Malnutrition.py', label=''' Malnutrition ''')
st.page_link('other_pages/diseases/Crohnsdisease.py', label=''' Crohn's disease ''')
st.page_link('other_pages/diseases/Hyperthyroidism.py', label=''' Hyperthyroidism''')
