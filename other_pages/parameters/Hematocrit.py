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


st.markdown('''# Hematocrit''')
st.write('''A hematocrit test measures the percentage of red blood cells in the blood. Red blood cells carry oxygen throughout the body, which oxygen powers the cells.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S1357272502000870?casa_token=FevVP4blcocAAAAA:2C7Cd-vQXXFptaW4y1O-LiosPXs2KkN7a6Vl72yO2YOsM1vM1VGH6PrPt5LTGFTcj_RazyrSQmq-')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Cardiovasculardisease.py', label='''Cardiovascular disease ''')
st.markdown(' Dehydratation ')
st.markdown(' Smoking ')
st.markdown(' Testosterone use')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Leukemia.py', label='''Leukemia ''')
st.page_link('other_pages/diseases/Hemolyticanemia.py', label=''' Hemolytic anemia ''')
st.page_link('other_pages/diseases/Hyponatremia.py', label=''' Hyponatremia ''')
st.page_link('other_pages/diseases/Kidneydisease.py', label=''' Kidney disease ''')
st.page_link('other_pages/diseases/Hypothyroidism.py', label=''' Hypothyroidism''')
