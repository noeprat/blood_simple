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


st.markdown('''# Crohn's disease''')
st.write('''Crohn’s disease is a chronic (lifelong) autoimmune condition that inflames and irritates the digestive tract, most commonly the small and large intestines''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(16)31711-1/fulltext')

st.markdown('### Epidemiology')
st.write('''The prevalence in Europe is 322 per 100,000 people.''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(16)31711-1/fulltext')
