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


st.markdown('''# Syphilis''')
st.write('''Syphilis is a sexually transmitted infection (STI) that spreads after having vaginal, anal or oral sex with someone who has the infection. A bacteria causes it. Antibiotic medication treats syphilis. Untreated syphilis can lead to serious health problems, including blindness and damage to the brain, heart, eyes and nervous system.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S1079210405002258?casa_token=soVKl0VuxSgAAAAA:Id6Tj2pan4NNH7zqqrHGDaXjRYl0VLz-War92rI5Awk_pJ9VcJHdOe1WBUDoisYrdmN-8Y9LENNi')

st.markdown('### Epidemiology')
st.write('''Thanks to penicillin, the prevalence of syphilis fell to less than 1% in most populations by 1960. In 2020, WHO estimated that 7.1 million adults aged 15–49 acquired syphilis globally.''')
st.link_button('Source', 'https://www.who.int/news-room/fact-sheets/detail/syphilis')
