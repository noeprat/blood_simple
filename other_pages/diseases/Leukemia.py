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


st.markdown('''# Leukemia''')
st.write('''Leukemia is a cancer of the blood, characterized by the rapid growth of abnormal blood cells. This uncontrolled growth takes place in the bone marrow, where most of the body’s blood is made. Leukemia cells are usually immature (still developing) white blood cells. ''')
st.link_button('Source', 'https://www.aafp.org/pubs/afp/issues/2014/0501/p731.html')

st.markdown('### Epidemiology')
st.write('''The age-adjusted incidence rate of leukemia in the United States is 12.8 per 100'000 persons each year.''')
st.link_button('Source', 'https://www.aafp.org/pubs/afp/issues/2014/0501/p731.html')
