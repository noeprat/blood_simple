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


st.markdown('''# Glucose''')
st.write('''Inside the cell, the glucose acts as an energy source as it undergoes the process of glycolysis. Properly maintained glucose levels are necessary for normal function in a number of tissues, including the brain, which consumes approximately 60% of blood glucose.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/books/NBK560599/')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Diabetes.py', label='''Diabetes ''')
st.page_link('other_pages/diseases/Hyperthyroidism.py', label=''' Hyperthyroidism ''')
st.page_link('other_pages/diseases/Cushingsyndrome.py', label=''' Cushing syndrome ''')
st.page_link('other_pages/diseases/Pancreatitis.py', label=''' Pancreatitis''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Liverdisease.py', label='''Liver disease ''')
st.page_link('other_pages/diseases/Kidneydisease.py', label=''' Kidney disease ''')
st.page_link('other_pages/diseases/Hypothyroidism.py', label=''' Hypothyroidism ''')
st.page_link('other_pages/diseases/Addisondiseaserare.py', label=''' Addison disease (rare)''')
