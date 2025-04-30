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


st.markdown('''# Lupus''')
st.write('''Lupus is a condition that causes inflammation throughout the body. It is an autoimmune disease, which means the immune system damages the body instead of protecting it.
Systemic lupus erythematosus is the most common type of lupus, and means lupus is found throughout the body.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S0896841118305213?casa_token=wXw8nucPAaoAAAAA:rQW57Gwr4BfeF7hwGDHwQ0kFFGIBYUXVKUIQwOA-OJ0ta5ZoKH0CCSnXlxCwlSnicDmA1-wSH3Xi')

st.markdown('### Epidemiology')
st.write('''The incidence of systemic lupus erythematosus in North America is 23.2 per 100'000 person per year.''')
st.link_button('Source', 'https://academic.oup.com/rheumatology/article/56/11/1945/4079913')
