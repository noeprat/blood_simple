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


st.markdown('''# Chloride''')
st.write('''Chloride is an electrolyte. Electrolytes are electrically charged minerals which help control the amount of fluid and the balance of acids and bases (pH balance) in the body.''')
st.link_button('Source', 'https://www.hsph.harvard.edu/nutritionsource/chloride/')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.markdown('Dehydratation ')
st.page_link('other_pages/diseases/Kidneydisease.py', label=''' Kidney disease ''')
st.page_link('other_pages/diseases/Metabolicacidosis.py', label=''' Metabolic acidosis ''')
st.page_link('other_pages/diseases/Cushingsyndrome.py', label=''' Cushing syndrome ''')
st.page_link('other_pages/diseases/Respiratoryalkalosis.py', label=''' Respiratory alkalosis''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Heartfailure.py', label='''Heart failure ''')
st.page_link('other_pages/diseases/Emphysema.py', label=''' Emphysema ''')
st.page_link('other_pages/diseases/Addisondiseaserare.py', label=''' Addison disease (rare) ''')
st.page_link('other_pages/diseases/Metabolicalkalosis.py', label=''' Metabolic alkalosis''')
