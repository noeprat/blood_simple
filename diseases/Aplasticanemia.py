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


st.markdown('''# Aplastic anemia''')
st.write('''Aplastic anemia is a rare but serious blood disorder. It happens when the bone marrow can’t make enough blood cells and platelets. People with aplastic anemia have an increased risk of serious infections, bleeding issues, heart issues and other complications. ''')
st.link_button('Source', 'https://www.nejm.org/doi/full/10.1056/nejmra1413485?casa_token=p-1dXocC9fQAAAAA:fxzU_E_w138JFUy4UtBa9S3-TjbvXzgua4SXaMUUZOmxeCA8ni7ZFzL1xSYI2dS8UfEOjw5oUSNDDH4U&casa_token=6qpx_w_l_Z4AAAAA:hfeFQ063fQDXgSsxD7-1umC0EjhVSYKVQ0eb6hFbvCGJ6IbcWzvASn1IGB8Qr9MJ_JbrAFD5fa5o73xG')

st.markdown('### Epidemiology')
st.write('''Aplastic anemia has an estimated incidence of around 1–2 cases per million per year, that is about three-fold higher in East Asia.''')
st.link_button('Source', 'https://haematologica.org/article/view/4811')
