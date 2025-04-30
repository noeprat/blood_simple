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


st.markdown('''# Cholecystitis''')
st.write('''Cholecystitis is an inflammation in the gallbladder. The gallbladder is a small, pear-shaped organ under the liver, which stores the bile made by the liver. It sends bile to the small intestine after a meal to help digest fats.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S0039610908000972')

st.markdown('### Epidemiology')
st.write('''Acute cholecystitis, typically due to gallstone obstruction of the cystic duct, affects approximately 200,000 people in the United States annually.''')
st.link_button('Source', 'https://jamanetwork.com/journals/jama/article-abstract/2789654')
