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


st.markdown('''# Lymphocytes''')
st.write('''Lymphocytes are a type of white blood cell. They play an important role in the immune system, which helps the body fight disease and infection. There are two main types of lymphocytes: T lymphocytes which directly attack and kill infected cells and tumor cells, and B lymphocytes which make antibodies (proteins that target viruses, bacteria and other foreign invaders).''')
st.link_button('Source', 'https://ashpublications.org/blood/article/112/5/1570/25424/B-lymphocytes-how-they-develop-and-function ; https://www.annualreviews.org/content/journals/10.1146/annurev-immunol-032712-095956')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Hepatitis.py', label='''Hepatitis ''')
st.page_link('other_pages/diseases/Syphilis.py', label=''' Syphilis ''')
st.page_link('other_pages/diseases/Mononucleosis.py', label=''' Mononucleosis ''')
st.page_link('other_pages/diseases/Tuberculosis.py', label=''' Tuberculosis ''')
st.page_link('other_pages/diseases/HIV.py', label=''' HIV ''')
st.page_link('other_pages/diseases/Hypothyroidism.py', label=''' Hypothyroidism ''')
st.page_link('other_pages/diseases/Lymphoma.py', label=''' Lymphoma ''')
st.page_link('other_pages/diseases/Leukemia.py', label=''' Leukemia''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/HIV.py', label='''HIV ''')
st.page_link('other_pages/diseases/Tuberculosis.py', label=''' Tuberculosis ''')
st.page_link('other_pages/diseases/Hepatitis.py', label=''' Hepatitis ''')
st.page_link('other_pages/diseases/Hodgkinlymphoma.py', label=''' Hodgkin lymphoma ''')
st.page_link('other_pages/diseases/Lupus.py', label=''' Lupus ''')
st.page_link('other_pages/diseases/Severecombinedimmunodeficiencyrare.py', label=''' Severe combined immunodeficiency (rare) ''')
st.page_link('other_pages/diseases/DiGeorgesyndromerare.py', label=''' DiGeorge syndrome (rare) ''')
st.page_link('other_pages/diseases/WiskottAldrichsyndromerare.py', label=''' Wiskott-Aldrich syndrome (rare)''')
