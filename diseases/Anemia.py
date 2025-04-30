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


st.markdown('''# Anemia''')
st.write('''Anemia is a blood disorder that happens when there is not enough red blood cells or the red blood cells do not work as they should. Some types of anemia are inherited, but people may also acquire or develop the condition during their lifetimes.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK499994/')

st.markdown('### Epidemiology')
st.write('''Anemia is an extremely common disease affecting up to one-third of the global population. In many cases, it is mild and asymptomatic and requires no management. The prevalence is more than 20% of individuals who are older than the age of 85.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK499994/')
