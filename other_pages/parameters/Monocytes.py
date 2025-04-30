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


st.markdown('''# Monocytes''')
st.write('''Monocytes are a type of white blood cell that reside in the blood and tissues to find and destroy germs (viruses, bacteria, fungi and protozoa) and eliminate infected cells. These cellular firefighters differentiate into two types of cells: dendritic cells which ask other cells in the immune system for backup to fight germs, and macrophages which capture and digest the invading microorganisms.''')
st.link_button('Source', 'https://www.nature.com/articles/nri.2017.28')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Lupus.py', label='''Lupus ''')
st.page_link('other_pages/diseases/Rheumatoidarthritis.py', label=''' Rheumatoid arthritis ''')
st.markdown(' Blood disorder ')
st.page_link('other_pages/diseases/Cancer.py', label=''' Cancer ''')
st.page_link('other_pages/diseases/Leukemia.py', label=''' Leukemia ''')
st.page_link('other_pages/diseases/Lymphoma.py', label=''' Lymphoma ''')
st.page_link('other_pages/diseases/Cardiovasculardisease.py', label=''' Cardiovascular disease ''')
st.page_link('other_pages/diseases/Mononucleosis.py', label=''' Mononucleosis ''')
st.page_link('other_pages/diseases/Sarcoidosis.py', label=''' Sarcoidosis''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Aplasticanemia.py', label='''Aplastic anemia ''')
st.page_link('other_pages/diseases/Infection.py', label=''' Infection ''')
st.markdown(' Burn injuries ')
st.page_link('other_pages/diseases/HIV.py', label=''' HIV''')
