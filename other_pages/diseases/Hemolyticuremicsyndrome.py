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


st.markdown('''# Hemolytic uremic syndrome''')
st.write('''Hemolytic uremic syndrome is a medical condition that blocks the small blood vessels in the kidneys. The blockage destroys the red blood cells (hemolytic anemia) and reduces the number of platelets (thrombocytopenia), which are clotting cells.''')
st.link_button('Source', 'https://journals.lww.com/jasn/fulltext/2005/04000/Hemolytic_Uremic_Syndrome.30.aspx')

st.markdown('### Epidemiology')
st.write('''Hemolytic uremic syndrome has an annual incidence of 0.57 per 100'000 people.''')
st.link_button('Source', 'https://assets.cureus.com/uploads/review_article/pdf/155695/20230621-11290-14ns7a6.pdf')
