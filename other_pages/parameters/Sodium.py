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


st.markdown('''# Sodium''')
st.write('''Sodium is a type of electrolyte which help the nerves and muscles work properly. Electrolytes are electrically charged minerals which help control the amount of fluid and the balance of acids and bases (pH balance) in the body.''')
st.link_button('Source', 'https://www.hsph.harvard.edu/nutritionsource/salt-and-sodium/')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Kidneydisease.py', label='''Kidney disease ''')
st.markdown(' Dehydratation ')
st.page_link('other_pages/diseases/Cirrhosis.py', label=''' Cirrhosis ''')
st.page_link('other_pages/diseases/Addisondiseaserare.py', label=''' Addison disease (rare) ''')
st.page_link('other_pages/diseases/Cushingsyndrome.py', label=''' Cushing syndrome''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Kidneydisease.py', label='''Kidney disease ''')
st.page_link('other_pages/diseases/Cancer.py', label=''' Cancer ''')
st.page_link('other_pages/diseases/Addisondiseaserare.py', label=''' Addison disease (rare) ''')
st.page_link('other_pages/diseases/Malnutrition.py', label=''' Malnutrition''')
