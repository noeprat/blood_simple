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


st.markdown('''# Sepsis''')
st.write('''Sepsis is a clinical syndrome defined by a systemic response to infection. When there is an infection, the immune system try to fight it, but sometimes it starts damaging the normal tissues and organs, leading to widespread inflammation throughout the body.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S0002934307005566?casa_token=gt5lWXM2lP8AAAAA:9ClDFeHjiaflA32APCHc7LJ5iplb6C4Y_t3LB4xAWYuEu8B1AQj1R4dPQmfLlnwH95DGV6svpn7G')

st.markdown('### Epidemiology')
st.write('''In 2017, an estimated 48.9 million incident cases of sepsis were recorded worldwide and 11.0 million sepsis-related deaths were reported, representing 19.7% of all global deaths. ''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(19)32989-7/fulltext?shortlink%5B0%5D=8441ac39&shortlink%5B1%5D=8441ac39&pid%5B0%5D=Web&pid%5B1%5D=Web&c%5B0%5D=homepage&c%5B1%5D=homepage&wtime=%7Bseek_to_second_number%7D&shortlink%5B0%5D=8441ac39&shortlink%5B1%5D=8441ac39&pid%5B0%5D=Web&pid%5B1%5D=Web&c%5B0%5D=homepage&c%5B1%5D=homepage&wtime=%7Bseek_to_second_number%7D')
