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


st.markdown('''# Kidney stones''')
st.write('''Celiac disease is an inherited autoimmune disorder that causes a reaction in the body to the protein, gluten. Gluten in the digestive system triggers the immune system to produce antibodies against it. These antibodies damage the lining of the small intestine (the mucosa). Damage to the mucosa in the small intestine impairs its ability to absorb nutrients from the food, causing nutritional deficiencies.
Gluten is a protein found in grains — particularly wheat, barley and rye. ''')
st.link_button('Source', 'https://www.nature.com/articles/nrdp20168')

st.markdown('### Epidemiology')
st.write('''The overall prevalence of kidney stone disease is around 8.8% of the population.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC9914194/')
