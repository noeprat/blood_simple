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


st.markdown('''# Rheumatoid arthritis''')
st.write('''Rheumatoid arthritis is an autoimmune disease that is chronic. The immune system attacks the tissue lining the joints on both sides of the body.''')
st.link_button('Source', 'https://www.mdpi.com/2073-4409/10/11/2857')

st.markdown('### Epidemiology')
st.write('''The global prevalence estimate of rheumatoid arthritis is 0.46%''')
st.link_button('Source', 'https://link.springer.com/article/10.1007/s00296-020-04731-0')
