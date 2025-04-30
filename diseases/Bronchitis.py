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


st.markdown('''# Bronchitis''')
st.write('''Bronchitis is an inflammation of the airways leading into the lungs. When the airways (trachea and bronchi) get irritated, they swell up and fill with mucus, causing coughing. The cough can last days to a couple of weeks. It is the main symptom of bronchitis. Viruses are the most common cause of acute bronchitis. Smoke and other irritants can cause acute and chronic bronchitis.''')
st.link_button('Source', 'https://www.atsjournals.org/doi/full/10.1164/rccm.201210-1843CI')

st.markdown('### Epidemiology')
st.write('''The prevalence of chronic bronchitis varies throughout the world, ranging from 3.4%-22.0% in the general population''')
st.link_button('Source 1', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6596437')
st.link_button('Source 2', 'https://www.ncbi.nlm.nih.gov/books/NBK448067/')
