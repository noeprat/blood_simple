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


st.markdown('''# Lymphoma''')
st.write('''Lymphoma are cancers of the lymphatic system — the network of tissues, vessels and organs that help the body fight infection. It is considered a blood cancer because the condition starts in white blood cells (lymphocytes) in the lymphatic system. There are two main lymphoma categories — Hodgkin lymphoma and non-Hodgkin lymphoma — and more than 70 lymphoma subtypes.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S0033838908000468')

st.markdown('### Epidemiology')
st.write('''A total of 83 000 new cases of Hodgkin lymphoma and 23 000 deaths from it were estimated in 2020. 
Non-Hodgkin lymphoma ranked as the 5th to 9th most common cancer in most countries worldwide, with almost 510,000 new cases estimated in 2018.''')
st.link_button('Source 1', 'https://onlinelibrary.wiley.com/doi/abs/10.1002/ijc.33948?casa_token=hy8O6uAbXCcAAAAA:84mUHnJuEw7bV987VS9UihEKr1CVGLat9p4BA0zXg-Ooopz9uVYJRyO26fg4imwJR-nSjfNiEYEZgirJ')
st.link_button('Source 2', 'https://link.springer.com/article/10.1007/s10552-019-01155-5')
