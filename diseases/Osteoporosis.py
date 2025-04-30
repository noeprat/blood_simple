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


st.markdown('''# Osteoporosis''')
st.write('''Osteoporosis is the loss of bone calcium, making certain bones more prone to fracture (breakage). The vertebral bodies of the spine, the upper femur (hip), and the forearm are at greatest risk.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5335887/')

st.markdown('### Epidemiology')
st.write('''The prevalence of osteoporosis in the world was reported to be 18.3%.''')
st.link_button('Source', 'https://josr-online.biomedcentral.com/articles/10.1186/s13018-021-02772-0')
