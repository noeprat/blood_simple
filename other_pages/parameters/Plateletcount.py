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


st.markdown('''# Platelet count''')
st.write('''Platelets are tiny blood cells that bud from cells in the bone marrow (the spongy tissue inside of bones). Platelets form clots when there is damage to a blood vessel. ''')
st.link_button('Source', 'https://link.springer.com/chapter/10.1007/978-3-642-29423-5_1')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Infection.py', label='''Infection ''')
st.page_link('other_pages/diseases/Cancer.py', label=''' Cancer''')
st.markdown('**Downregulation could be a sign of:**')
st.markdown('Vitamin B12 deficiency ')
st.markdown(' Iron deficiency ')
st.markdown(' Severe bleeding ')
st.page_link('other_pages/diseases/Kidneydisease.py', label=''' Kidney disease''')
