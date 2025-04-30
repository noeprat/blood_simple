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


st.markdown('''# Kidney disease''')
st.write('''The kidneys are organs that clean the blood, filter extra water out of the blood, and help control the blood pressure. It also help red blood cell production and vitamin D metabolism needed for bone health. 
There are several types of kidney disease. Chronic kidney disease, nephrititis and nephrosis are some of them.''')
st.link_button('Source', 'https://www.thelancet.com/article/S0140-6736(21)00519-5/abstract')
