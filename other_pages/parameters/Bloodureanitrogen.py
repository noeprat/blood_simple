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


st.markdown('''# Blood urea nitrogen''')
st.write('''Urea nitrogen is a waste product that kidneys remove from blood. It is produced by protein degradation in the gut.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK305/')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.markdown('High-protein diet ')
st.markdown(' Dehydratation ')
st.markdown(' Stress ')
st.page_link('other_pages/diseases/Heartattack.py', label=''' Heart attack ''')
st.page_link('other_pages/diseases/Gastrointestinalbleeding.py', label=''' Gastrointestinal bleeding''')
st.markdown('**Downregulation could be a sign of:**')
st.markdown('Low protein diet ')
st.markdown(' Overhydratation ')
st.page_link('other_pages/diseases/Liverdisease.py', label=''' Liver disease''')
