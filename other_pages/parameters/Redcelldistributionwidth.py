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


st.markdown('''# Red cell distribution width''')
st.write('''An RDW (red cell distribution width) blood test measures how varied the red blood cells are in size and volume. Red blood cells carry oxygen throughout the body, which powers the cells. ''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S1357272502000870?casa_token=FevVP4blcocAAAAA:2C7Cd-vQXXFptaW4y1O-LiosPXs2KkN7a6Vl72yO2YOsM1vM1VGH6PrPt5LTGFTcj_RazyrSQmq-')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Anemia.py', label='''Anemia''')
st.markdown('**Downregulation could be a sign of:**')
st.markdown('Typically not problematic.')
