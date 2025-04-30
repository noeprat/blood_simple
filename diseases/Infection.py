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


st.markdown('''# Infection''')
st.write('''Infectious diseases are illnesses caused by harmful agents (pathogens) that get into the body. The most common causes are viruses, bacteria, fungi and parasites. Infectious diseases usually spread from person to person, through contaminated food or water and through bug bites. Some infectious diseases are minor and some are very serious.''')
st.link_button('Source', 'https://www.nature.com/articles/nature06536')

st.markdown('### Epidemiology')
st.write('''Infectious diseases remain one of the leading causes of morbidity and mortality around the world accounting for more than 52 million (33%) annual deaths worldwide. Half of the world's population remains at risk of emerging and re-emerging infectious diseases. ''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9852260/')
