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


st.markdown('''# Gastrointestinal bleeding''')
st.write('''Celiac disease is an inherited autoimmune disorder that causes a reaction in the body to the protein, gluten. Gluten in the digestive system triggers the immune system to produce antibodies against it. These antibodies damage the lining of the small intestine (the mucosa). Damage to the mucosa in the small intestine impairs its ability to absorb nutrients from the food, causing nutritional deficiencies.
Gluten is a protein found in grains — particularly wheat, barley and rye. ''')
st.link_button('Source', 'https://www.gastro.theclinics.com/article/S0889-8553(05)00073-7/abstract')

st.markdown('### Epidemiology')
st.write('''The annual incidence rate of lower gastrointestinal bleeding in the US ranges from 20.5 to 27 cases per 100,000 adult population at risk (0.03%).''')
st.link_button('Source', 'https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2036.2005.02485.x')
