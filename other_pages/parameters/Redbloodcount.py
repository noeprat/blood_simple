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


st.markdown('''# Red blood count''')
st.write('''Red blood cells carry oxygen throughout the body, which powers the cells. The characteristics of the red blood cells provide information about how successfully they can transport oxygen.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S1357272502000870?casa_token=FevVP4blcocAAAAA:2C7Cd-vQXXFptaW4y1O-LiosPXs2KkN7a6Vl72yO2YOsM1vM1VGH6PrPt5LTGFTcj_RazyrSQmq-')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Polycythemiavera.py', label='''Polycythemia vera ''')
st.page_link('other_pages/diseases/Congenitalheartdefect.py', label=''' Congenital heart defect ''')
st.page_link('other_pages/diseases/Emphysema.py', label=''' Emphysema''')
st.markdown('**Downregulation could be a sign of:**')
st.page_link('other_pages/diseases/Anemia.py', label='''Anemia ''')
st.markdown(' Severe bleeding ')
st.page_link('other_pages/diseases/Cancer.py', label=''' Cancer ''')
st.page_link('other_pages/diseases/Leukemia.py', label=''' Leukemia ''')
st.page_link('other_pages/diseases/Lymphoma.py', label=''' Lymphoma ''')
st.markdown(' B12 deficiency')
