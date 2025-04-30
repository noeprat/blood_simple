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


st.markdown('''# Cancer''')
st.write('''Cancer is a group of diseases involving abnormal cell growth with the potential to invade or spread to other parts of the body.
The most common cancers are breast, lung, colon and rectum and prostate cancers.''')
st.link_button('Source', 'https://www.who.int/en/news-room/fact-sheets/detail/cancer')

st.markdown('### Epidemiology')
st.write('''Cancer is a leading cause of death worldwide, accounting for nearly 10 million deaths in 2020.''')
st.link_button('Source 1', 'https://www.who.int/en/news-room/fact-sheets/detail/cancer')
st.link_button('Source 2', 'https://ascopubs.org/doi/abs/10.1200/JCO.2005.05.2308')
