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


st.markdown('''# Lyme disease''')
st.write('''Lyme disease is caused by a bacteria, Borrelia burgdorferi, after an infected tick bites a human. The condition can cause joint pain. Lyme disease is divided into 3 stages: early localized, early disseminated, and late. The early localized disease is distinguished by a red ring-like expanding rash at the site of a recent tick bite.''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(11)60103-7/abstract')

st.markdown('### Epidemiology')
st.write('''Approximately 476'000 people may be diagnosed with Lyme disease each year in the United States.''')
st.link_button('Source', 'https://www.cdc.gov/lyme/datasurveillance/index.html')
