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


st.markdown('''# Neutrophils''')
st.write('''Neutrophils are a type of white blood cell that act as the immune system’s first line of defense. Neutrophils capture and destroy the invading bacteria or microorganisms by setting traps and ingesting them. ''')
st.link_button('Source', 'https://www.cell.com/immunity/pdf/S1074-7613(21)00250-8.pdf')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Infection.py', label='''Infection ''')
st.page_link('other_pages/diseases/Leukemia.py', label=''' Leukemia''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Infection.py', label='''Infection ''')
st.page_link('other_pages/diseases/Hepatitis.py', label=''' Hepatitis ''')
st.page_link('other_pages/diseases/Tuberculosis.py', label=''' Tuberculosis ''')
st.page_link('other_pages/diseases/Sepsis.py', label=''' Sepsis ''')
st.page_link('other_pages/diseases/Lymedisease.py', label=''' Lyme disease ''')
st.page_link('other_pages/diseases/Leukemia.py', label=''' Leukemia ''')
st.markdown(' Vitamin deficiency ')
st.page_link('other_pages/diseases/Crohnsdisease.py', label=''' Crohn’s disease ''')
st.page_link('other_pages/diseases/Lupus.py', label=''' Lupus ''')
st.page_link('other_pages/diseases/Rheumatoidarthritis.py', label=''' Rheumatoid arthritis''')
