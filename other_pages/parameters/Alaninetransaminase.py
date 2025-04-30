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


st.markdown('''# Alanine transaminase''')
st.write('''Alanine transaminase is an enzyme mainly found in the liver, though it exists in other parts of the body. An enzyme is a type of protein in a cell that acts as a catalyst and allows certain bodily processes to happen. ''')
st.link_button('Source', 'https://jamanetwork.com/journals/jamainternalmedicine/article-abstract/614597')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Fattyliverdisease.py', label='''Fatty liver disease ''')
st.page_link('other_pages/diseases/Hepatitis.py', label=''' Hepatitis ''')
st.page_link('other_pages/diseases/Cirrhosis.py', label=''' Cirrhosis ''')
st.page_link('other_pages/diseases/Liverdisease.py', label=''' Liver disease ''')
st.page_link('other_pages/diseases/Mononucleosis.py', label=''' Mononucleosis''')
st.markdown('**Downregulation could be a sign of:**')
st.markdown('Typically not problematic.')
