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


st.markdown('''# Hemolytic anemia''')
st.write('''Hemolytic anemia is a disorder in which red blood cells are destroyed faster than they can be made. The destruction of red blood cells is called hemolysis. Red blood cells carry oxygen to all parts of the body. ''')
st.link_button('Source', 'https://www.aafp.org/pubs/afp/issues/2004/0601/p2599.html')

st.markdown('### Epidemiology')
st.write('''The incidence rate of AIHA was estimated at 2.4 per 100 000 person-years.''')
st.link_button('Source', 'https://onlinelibrary.wiley.com/doi/full/10.1002/ajh.26213')
