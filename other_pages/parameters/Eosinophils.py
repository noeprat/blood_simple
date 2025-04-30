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


st.markdown('''# Eosinophils''')
st.write('''Eosinophils are a type of white blood cell that protect the body from parasites. Eosinophils are larger than most cells and make up less than 5% of all white blood cells in the body.''')
st.link_button('Source', 'https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2222.2008.02958.x')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Cancer.py', label='''Cancer ''')
st.page_link('other_pages/diseases/Eosinophilicesophagitis.py', label=''' Eosinophilic esophagitis ''')
st.page_link('other_pages/diseases/Asthma.py', label=''' Asthma ''')
st.page_link('other_pages/diseases/Bronchitis.py', label=''' Bronchitis ''')
st.page_link('other_pages/diseases/Pneumonia.py', label=''' Pneumonia''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Cushingsyndrome.py', label='''Cushing syndrome ''')
st.page_link('other_pages/diseases/Sepsis.py', label=''' Sepsis''')
