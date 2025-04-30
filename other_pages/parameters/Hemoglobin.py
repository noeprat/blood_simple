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


st.markdown('''# Hemoglobin''')
st.write('''Hemoglobin is the main component of red blood cells (erythrocytes). It is a protein containing iron which binds to oxygen. Hemoglobin enables the red blood cells to carry oxygen from the lungs to other tissues and organs throughout the body.''')
st.link_button('Source', 'https://www.tandfonline.com/doi/abs/10.3109/10409239509085142')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Polycythemiavera.py', label='''Polycythemia vera ''')
st.page_link('other_pages/diseases/Congenitalheartdefect.py', label=''' Congenital heart defect ''')
st.page_link('other_pages/diseases/Kidneydisease.py', label=''' Kidney disease ''')
st.page_link('other_pages/diseases/Pulmonaryfibrosis.py', label=''' Pulmonary fibrosis''')
st.markdown('**Downregulation could be a sign of:**')
st.markdown('Iron deficiency ')
st.page_link('other_pages/diseases/Cancer.py', label=''' Cancer ''')
st.page_link('other_pages/diseases/Betathalassemia.py', label=''' Beta-thalassemia ''')
st.page_link('other_pages/diseases/Kidneydisease.py', label=''' Kidney disease ''')
st.page_link('other_pages/diseases/Liverdisease.py', label=''' Liver disease ''')
st.page_link('other_pages/diseases/Sicklecelldisease.py', label=''' Sickle cell disease ''')
st.page_link('other_pages/diseases/Autoimmunedisease.py', label=''' Autoimmune disease''')
