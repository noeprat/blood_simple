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


st.markdown('''# Bicarbonate''')
st.write('''Bicarbonate indicates the amount of carbon dioxide (CO2) in the blood. Electrolytes are electrically charged minerals which help control the amount of fluid and the balance of acids and bases (pH balance) in the body.''')
st.link_button('Source', 'https://www.urmc.rochester.edu/encyclopedia/content.aspx?contenttypeid=167&contentid=bicarbonate')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Addisondiseaserare.py', label='''Addison disease (rare) ''')
st.page_link('other_pages/diseases/Ketoacidosis.py', label=''' Ketoacidosis ''')
st.page_link('other_pages/diseases/Kidneydisease.py', label=''' Kidney disease ''')
st.page_link('other_pages/diseases/Respiratoryalkalosis.py', label=''' Respiratory alkalosis ''')
st.page_link('other_pages/diseases/Metabolicacidosis.py', label=''' Metabolic acidosis''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Cushingsyndrome.py', label='''Cushing syndrome ''')
st.markdown(' Dehydratation ')
st.page_link('other_pages/diseases/Metabolicalkalosis.py', label=''' Metabolic alkalosis ''')
st.page_link('other_pages/diseases/Respiratoryacidosis.py', label=''' Respiratory acidosis ''')
st.page_link('other_pages/diseases/Barttersyndromerare.py', label=''' Bartter syndrome (rare)''')
