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


st.markdown('''# Tuberculosis''')
st.write('''Tuberculosis is an infectious disease that can cause infection in the lungs or other tissues. It commonly affects the lungs, but it can also affect other organs like the spine, brain or kidneys.''')
st.link_button('Source 1', 'https://www.sciencedirect.com/science/article/pii/S095461110600401X')
st.link_button('Source 2', 'https://onlinelibrary.wiley.com/doi/abs/10.1128/9781555817657.ch2')

st.markdown('### Epidemiology')
st.write('''There were an estimated 8.9 million new cases of tuberculosis in 2004.  About 80% of individuals newly diagnosed with the disease every year live in the 22 most populous countries.''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(06)68384-0/abstract')
