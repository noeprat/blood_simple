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


st.markdown('''# Basophils''')
st.write('''Basophils are a type of white blood cell that works closely with the immune system to defend the body from allergens, pathogens and parasites. Basophils release enzymes to improve blood flow and prevent blood clots. 
During allergic reactions, basophils release two enzymes: histamine and heparin. Histamine enlarges the blood vessels to improve blood flow and heal the affected area. Heparin is an enzyme that prevents blood from clotting too quickly.''')
st.link_button('Source', 'https://www.nature.com/articles/ni.f.217')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.markdown('Allergic reaction ')
st.page_link('other_pages/diseases/Infection.py', label=''' Infection ''')
st.page_link('other_pages/diseases/Leukemia.py', label=''' Leukemia ''')
st.page_link('other_pages/diseases/Polycythemiavera.py', label=''' Polycythemia vera ''')
st.page_link('other_pages/diseases/Myelofibrosis.py', label=''' Myelofibrosis ''')
st.page_link('other_pages/diseases/Hypothyroidism.py', label=''' Hypothyroidism ''')
st.page_link('other_pages/diseases/Inflammatoryboweldisease.py', label=''' Inflammatory bowel disease ''')
st.page_link('other_pages/diseases/Autoimmunedisease.py', label=''' Autoimmune disease''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Infection.py', label='''Infection ''')
st.page_link('other_pages/diseases/Hyperthyroidism.py', label=''' Hyperthyroidism''')
