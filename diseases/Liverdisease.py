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


st.markdown('''# Liver disease''')
st.write('''The liver is a vital organ which turns nutrients into chemicals the body needs, and filters out poisons. 
There are several types of liver disease. Some are genetic, while others are caused by viruses or other illnesses, or by toxins, such as drugs or alcohol. Hepatitis, fatty liver disease and liver cancer are some of them.''')
st.link_button('Source', 'https://pubmed.ncbi.nlm.nih.gov/36990226/#:~:text=Abstract,related%20deaths%20occur%20in%20men.')

st.markdown('### Epidemiology')
st.write('''Liver disease is responsible for 4% of all deaths worldwide.''')
st.link_button('Source', 'https://pubmed.ncbi.nlm.nih.gov/36990226/#:~:text=Abstract,related%20deaths%20occur%20in%20men.')
