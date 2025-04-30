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


st.markdown('''# Diabetes''')
st.write('''Diabetes mellitus is characterized by persistent hyperglycemia (too high glucose levels). It is linked poor glucose metabolism. ''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(10)60484-9/fulltext')

st.markdown('### Epidemiology')
st.write('''10.5% of the adult population has diabetes, with almost half unaware that they are living with the condition.''')
st.link_button('Source', 'https://idf.org/about-diabetes/diabetes-facts-figures/')
