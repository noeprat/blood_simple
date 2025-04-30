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


st.markdown('''# Mean corpuscular hemoglobin''')
st.write('''Mean corpuscular hemoglobin is the average amount of hemoglobin in the red blood cells. Hemoglobin is an important protein that allows red blood cells to carry oxygen.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S1357272502000870?casa_token=FevVP4blcocAAAAA:2C7Cd-vQXXFptaW4y1O-LiosPXs2KkN7a6Vl72yO2YOsM1vM1VGH6PrPt5LTGFTcj_RazyrSQmq-')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Anemia.py', label='''Anemia ''')
st.markdown(' Vitamin B12 deficiency ')
st.markdown(' Folate deficiency ')
st.page_link('other_pages/diseases/Liverdisease.py', label=''' Liver disease ''')
st.page_link('other_pages/diseases/Leukemia.py', label=''' Leukemia ''')
st.page_link('other_pages/diseases/Hypothyroidism.py', label=''' Hypothyroidism''')
st.markdown('**Downregulation could be a sign of:**')
st.markdown('Iron deficiency ')
st.page_link('other_pages/diseases/Betathalassemia.py', label=''' Beta-thalassemia ''')
st.page_link('other_pages/diseases/Sicklecelldisease.py', label=''' Sickle cell disease''')
