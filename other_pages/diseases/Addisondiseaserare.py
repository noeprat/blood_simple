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


st.markdown('''# Addison disease (rare)''')
st.write('''Addison's disease, also known as primary adrenal insufficiency, is a rare disorder of the adrenal glands. The adrenal glands are two small glands that sit on top of the kidneys. They produce two essential hormones: cortisol and aldosterone. Major symptoms include fatigue, gastrointestinal abnormalities, and changes in skin color (pigmentation).''')
st.link_button('Source', 'https://www.hopkinsmedicine.org/health/conditions-and-diseases/underactive-adrenal-glands--addisons-disease')

st.markdown('### Epidemiology')
st.write('''The total number of people affected by Addison's disease ranges from 4 to 11 per 100'000 of the population. In adults, the typical age of the disease presentation is 30 to 50 years and is more frequently seen in women. ''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK441994/')
