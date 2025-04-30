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


st.markdown('''# Hyperparathyroidism''')
st.write('''Celiac disease is an inherited autoimmune disorder that causes a reaction in the body to the protein, gluten. Gluten in the digestive system triggers the immune system to produce antibodies against it. These antibodies damage the lining of the small intestine (the mucosa). Damage to the mucosa in the small intestine impairs its ability to absorb nutrients from the food, causing nutritional deficiencies.
Gluten is a protein found in grains — particularly wheat, barley and rye. ''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(09)60507-9/abstract')

st.markdown('### Epidemiology')
st.write('''Primary hyperparathyroidism is more common in women, the incidence being 66 per 100,000 person-years in females, and 25 per 100,000 person-years in males.''')
st.link_button('Source', 'https://emedicine.medscape.com/article/127351-overview?form=fpf')
