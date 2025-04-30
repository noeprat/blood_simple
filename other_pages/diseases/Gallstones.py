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


st.markdown('''# Gallstones''')
st.write('''Gallstones (cholelithiasis) are hardened, concentrated pieces of bile that form in the gallbladder or bile ducts. The liver makes bile, and the bile ducts carry it to the different organs in the biliary tract.''')
st.link_button('Source', 'https://www.nature.com/articles/nrdp201624')

st.markdown('### Epidemiology')
st.write('''The prevalence of gallstones in the United States represents 10% to 15% of the adult population.''')
st.link_button('Source', 'https://www.gastro.theclinics.com/article/S0889-8553(10)00017-8/fulltext')
