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


st.markdown('''# Creatinine''')
st.write('''Creatinine is a waste product excreted primarily by the kidneys. It is made when muscles are used and some of the muscle tissue breaks down.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK305/')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Kidneydisease.py', label='''Kidney disease ''')
st.markdown(' Dehydratation')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Liverdisease.py', label='''Liver disease ''')
st.page_link('other_pages/diseases/Musculardystrophy.py', label=''' Muscular dystrophy ''')
st.markdown(' Overhydratation')
