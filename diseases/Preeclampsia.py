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


st.markdown('''# Preeclampsia''')
st.write('''Preeclampsia is a serious blood pressure condition that develops during pregnancy. People with preeclampsia often have high blood pressure (hypertension) and high levels of protein in their urine (proteinuria). Preeclampsia typically develops after the 20th week of pregnancy. It can also affect other organs in the body and be dangerous for both the mom and her developing fetus. ''')
st.link_button('Source', 'https://www.ahajournals.org/doi/full/10.1161/01.HYP.0000188408.49896.c5')

st.markdown('### Epidemiology')
st.write('''The overall preeclampsia rate was 3.1% and the incidence increased sharply with gestation; early- and late-onset preeclampsia rates were 0.38% and 2.72%, respectively. ''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S0002937813008594?casa_token=JRlnd8SfXdwAAAAA:1wUCNHubNUOXbW3jtFuotDoVTR8kOMezvZxwSKm8JqpnK9Pxc4H6d3EchUpNyjF_luuyKoO52r9h')
