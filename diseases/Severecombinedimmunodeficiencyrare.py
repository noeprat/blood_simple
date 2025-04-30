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


st.markdown('''# Severe combined immunodeficiency (rare)''')
st.write('''Severe combined immunodeficiency (SCID) is one of the most severe types of primary immunodeficiency. Babies born with SCID lack white blood cells called T cells. T cells not only directly attack cells infected with viruses, bacteria, or other microorganisms, but they also cause B cells, another type of white blood cell, to produce antibodies. Essentially, a baby with SCID completely lacks a functional immune system and is extremely vulnerable to severe and life-threatening infections. Without treatment, these children typically do not survive past two years of age.''')
st.link_button('Source', 'https://www.immunology.theclinics.com/article/S0889-8561(15)00051-X/fulltext')

st.markdown('### Epidemiology')
st.write('''The incidence of SCID is estimated to be 1 in 58'000 live-births.''')
st.link_button('Source', 'https://pubmed.ncbi.nlm.nih.gov/25138334/')
