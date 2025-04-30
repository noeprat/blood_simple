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


st.markdown('''# Cirrhosis''')
st.write('''Cirrhosis is scarring of the liver. Scar tissue forms because of injury or long-term disease. Scar tissue cannot make protein, help fight infections, clean the blood, help digest food and store energy. ''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140673608603839/fulltext')

st.markdown('### Epidemiology')
st.write('''The age-standardized incidence of cirrhosis is 20.7 per 100,000 people.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S1542356519308493')
