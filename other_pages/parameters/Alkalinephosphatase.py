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


st.markdown('''# Alkaline phosphatase''')
st.write('''Alkaline phosphatase is an enzyme found throughout the body. An enzyme is a type of protein in a cell that acts as a catalyst and allows certain bodily processes to happen. Despite active research for decades, researchers do not yet know its exact function.''')
st.link_button('Source', 'https://link.springer.com/article/10.1007/s12291-013-0408-y')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Cirrhosis.py', label='''Cirrhosis ''')
st.page_link('other_pages/diseases/Hepatitis.py', label=''' Hepatitis ''')
st.page_link('other_pages/diseases/Mononucleosis.py', label=''' Mononucleosis ''')
st.page_link('other_pages/diseases/Pagetsdiseaseofthebone.py', label=''' Paget's disease of the bone ''')
st.page_link('other_pages/diseases/Osteosarcoma.py', label=''' Osteosarcoma''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Malnutrition.py', label='''Malnutrition ''')
st.markdown(' Zinc deficiency ')
st.markdown(' Magnesium deficiency ')
st.page_link('other_pages/diseases/Hypothyroidism.py', label=''' Hypothyroidism ''')
st.page_link('other_pages/diseases/Wilsondiseaserare.py', label=''' Wilson disease (rare)''')
