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


st.markdown('''# Mononucleosis''')
st.write('''Mononucleosis is a contagious infection caused by a herpes virus called Epstein-Barr. The infection is common among teenagers and young adults. People with mono experience extreme fatigue, fever and body aches.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC3021204/')

st.markdown('### Epidemiology')
st.write('''It is estimated that up to 95% of adults in the world are eventually seropositive to Epstein-Barr virus. The infection is common among teenagers and young adults, but not everyone who has the virus develops mononucleosis symptoms.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK470387/')
