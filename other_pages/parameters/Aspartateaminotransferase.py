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


st.markdown('''# Aspartate aminotransferase''')
st.write('''AST and ALT are both commonly considered liver enzymes, but there are greater amounts of AST in other parts of the body, such as the heart, skeletal muscles and pancreas. Because of this, ALT is considered to be more directly tied to the liver health.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/000991209080062N')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Hepatitis.py', label='''Hepatitis ''')
st.page_link('other_pages/diseases/Cirrhosis.py', label=''' Cirrhosis ''')
st.page_link('other_pages/diseases/Liverdisease.py', label=''' Liver disease ''')
st.page_link('other_pages/diseases/Mononucleosis.py', label=''' Mononucleosis ''')
st.page_link('other_pages/diseases/Pancreatitis.py', label=''' Pancreatitis ''')
st.page_link('other_pages/diseases/Heartattack.py', label=''' Heart attack ''')
st.page_link('other_pages/diseases/Hypothyroidism.py', label=''' Hypothyroidism''')
st.markdown('**Downregulation could be a sign of:**')
st.markdown('Typically not problematic.')
