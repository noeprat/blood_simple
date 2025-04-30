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


st.markdown('''# White blood cell count''')
st.write('''White blood cells, also known as leukocytes, are responsible for protecting the body from infection. As part of the immune system, white blood cells circulate in the blood and respond to injury or illness. The white blood cells are in the bloodstream and travel through blood vessel walls and tissues to locate the site of an infection.''')
st.link_button('Source', 'https://europepmc.org/article/NBK/nbk563148')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Infection.py', label='''Infection ''')
st.page_link('other_pages/diseases/Sepsis.py', label=''' Sepsis ''')
st.markdown(' Allergic reaction ')
st.page_link('other_pages/diseases/Autoimmunedisease.py', label=''' Autoimmune disease ''')
st.page_link('other_pages/diseases/Lymphoma.py', label=''' Lymphoma ''')
st.page_link('other_pages/diseases/Leukemia.py', label=''' Leukemia''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Aplasticanemia.py', label='''Aplastic anemia ''')
st.page_link('other_pages/diseases/Leukemia.py', label=''' Leukemia ''')
st.markdown(' Chemotherapy ')
st.markdown(' Vitamin B12 deficiency ')
st.page_link('other_pages/diseases/HIV.py', label=''' HIV''')
