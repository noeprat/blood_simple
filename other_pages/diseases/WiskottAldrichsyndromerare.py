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


st.markdown('''# Wiskott-Aldrich syndrome (rare)''')
st.write('''Wiskott-Aldrich syndrome is a rare genetic immunodeficiency that keeps a child's immune system from functioning properly. It also makes it difficult for a child's bone marrow to produce platelets, making a child prone to bleeding. It occurs mostly in males.''')
st.link_button('Source', 'https://nyaspubs.onlinelibrary.wiley.com/doi/abs/10.1111/nyas.12049?casa_token=tBiMOHzZ5O8AAAAA:3jiUJdTMZxIjieYhBeQdn0Z4GQO4hER8cq9rcjuz8oN715lYaIqT1hFwWqcH-t3aSyUuxsOH2AoWlbl6')

st.markdown('### Epidemiology')
st.write('''The estimated incidence of Wiskott-Aldrich syndrome is 1 in every 100'000 live births.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK539838/')
