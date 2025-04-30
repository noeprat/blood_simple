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


st.markdown('''# Calcium''')
st.write('''Calcium is a mineral most often associated with healthy bones and teeth. It also plays an important role in blood clotting, helping muscles to contract, and regulating normal heart rhythms and nerve functions. ''')
st.link_button('Source', 'https://www.hsph.harvard.edu/nutritionsource/calcium/')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Hyperparathyroidism.py', label='''Hyperparathyroidism ''')
st.page_link('other_pages/diseases/Cancer.py', label=''' Cancer ''')
st.page_link('other_pages/diseases/Pagetsdiseaseofthebone.py', label=''' Paget's disease of the bone''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Celiacdisease.py', label='''Celiac disease ''')
st.page_link('other_pages/diseases/Kidneystones.py', label=''' Kidney stones ''')
st.markdown(' Renal failure ')
st.page_link('other_pages/diseases/Pancreatitis.py', label=''' Pancreatitis ''')
st.page_link('other_pages/diseases/Osteoporosis.py', label=''' Osteoporosis''')
