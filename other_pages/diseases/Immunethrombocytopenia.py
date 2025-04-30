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


st.markdown('''# Immune thrombocytopenia''')
st.write('''Immune thrombocytopenia is a form of low platelet count, a condition that keeps the blood from clotting. When the blood cannot make clots, one may bruise easily, bleed a lot when hurt or start bleeding for no reason. Immune thrombocytopenia happens when the immune system clears the platelets from circulation, and the platelet level goes down. ''')
st.link_button('Source', 'https://ashpublications.org/hematology/article/2010/1/377/278337/Immune-Thrombocytopenia')

st.markdown('### Epidemiology')
st.write('''The prevalence of immune thrombocytopenia is ranging from 9.5 to 23.6 per 100'000 people.''')
st.link_button('Source', 'https://ashpublications.org/hematology/article/2010/1/377/278337/Immune-Thrombocytopenia')
