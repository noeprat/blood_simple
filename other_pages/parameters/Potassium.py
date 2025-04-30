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


st.markdown('''# Potassium''')
st.write('''Potassium is a type of electrolyte which helps muscles to contract and supports normal blood pressure. Electrolytes are electrically charged minerals which help control the amount of fluid and the balance of acids and bases (pH balance) in the body.''')
st.link_button('Source', 'https://www.hsph.harvard.edu/nutritionsource/potassium/')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Kidneydisease.py', label='''Kidney disease ''')
st.page_link('other_pages/diseases/Addisondiseaserare.py', label=''' Addison disease (rare) ''')
st.page_link('other_pages/diseases/Alcoholusedisorder.py', label=''' Alcohol use disorder''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Cushingsyndrome.py', label='''Cushing syndrome ''')
st.page_link('other_pages/diseases/Kidneydisease.py', label=''' Kidney disease ''')
st.page_link('other_pages/diseases/Alcoholusedisorder.py', label=''' Alcohol use disorder''')
