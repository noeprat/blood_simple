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


st.markdown('''# Inflammatory bowel disease''')
st.write('''Inflammatory bowel disease is a group of disorders that cause chronic inflammation (pain and swelling) in the intestines. It includes Crohn’s disease and ulcerative colitis. Both types affect the digestive system. ''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(07)60750-8/abstract')

st.markdown('### Epidemiology')
st.write('''The prevalence of inflammatory bowel disease exceeds 0.3% in North America, Oceania, and many countries in Europe.''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(17)32448-0/abstract')
