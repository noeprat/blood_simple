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


st.markdown('''# Hepatitis''')
st.write('''Hepatitis is inflammation in the liver. Inflammation is the body’s response to an infection or injury. Many things can injure the liver and trigger hepatitis. Toxic chemicals, heavy substance use, viral infections and bile flow problems are a few examples. 
Hepatitis is most commonly caused by the virus hepatovirus A, B, C, D, and E.''')
st.link_button('Source', 'https://www.who.int/news-room/questions-and-answers/item/hepatitis')

st.markdown('### Epidemiology')
st.write('''In 2015, an estimated 257 million people were living with chronic Hepatitis B virus infection, and 71 million people with chronic Hepatitis C virus infection.''')
st.link_button('Source', 'https://iris.who.int/bitstream/handle/10665/255016/9789241565455-eng.pdf')
