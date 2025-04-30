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


st.markdown('''# Mean corpuscular volume''')
st.write('''Mean corpuscular volume is the average size of the red blood cells. Red blood cells carry oxygen throughout the body, which powers the cells. The characteristics of the red blood cells provide information about how successfully they can transport oxygen.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S1357272502000870?casa_token=FevVP4blcocAAAAA:2C7Cd-vQXXFptaW4y1O-LiosPXs2KkN7a6Vl72yO2YOsM1vM1VGH6PrPt5LTGFTcj_RazyrSQmq-')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Perniciousanemia.py', label='''Pernicious anemia ''')
st.markdown(' Vitamin B12 deficiency ')
st.markdown(' Folate deficiency ')
st.page_link('other_pages/diseases/Liverdisease.py', label=''' Liver disease ''')
st.page_link('other_pages/diseases/Myelodysplasticsyndrome.py', label=''' Myelodysplastic syndrome''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Anemia.py', label='''Anemia ''')
st.page_link('other_pages/diseases/Betathalassemia.py', label=''' Beta-thalassemia''')
