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


st.markdown('''# Cholangitis''')
st.write('''Cholangitis is inflammation in the bile ducts, the tubes that carry bile from the liver to other organs in the digestive system. Acute cholangitis is usually caused by an infection or something blocking the bile ducts, such as a gallstone.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK558946/')

st.markdown('### Epidemiology')
st.write('''On average, in the United States, there are less than 200,000 cases of acute cholangitis annually. The average age of individuals affected is 50 to 60 years old. ''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK558946/')
