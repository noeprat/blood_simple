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


st.markdown('''# Fatty liver disease''')
st.write('''Fatty liver disease (or steatotic liver disease) involves having excess fat in the liver. Metabolic conditions and heavy alcohol use are risk factors. Depending on the disease type, the fat buildup may not cause problems, or it may lead to liver damage. ''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5643281/')

st.markdown('### Epidemiology')
st.write('''The global prevalence of non-alcoholic fatty liver disease is 25.24%.''')
st.link_button('Source', 'https://journals.lww.com/hep/abstract/2016/07000/global_epidemiology_of_nonalcoholic_fatty_liver.14.aspx')
