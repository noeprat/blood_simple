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


st.markdown('''# Wilson disease (rare)''')
st.write('''Wilson disease is a rare genetic condition that occurs when the body accumulates too much copper, especially in the liver and brain. The body needs a small amount of copper from food to stay healthy, but without treatment, Wilson disease can lead to high copper levels that cause life-threatening organ damage.''')
st.link_button('Source 1', 'https://www.nature.com/articles/s41572-018-0018-3')
st.link_button('Source 2', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(07)60196-2/abstract')

st.markdown('### Epidemiology')
st.write('''The prevalence of Wilson disease is 1 in 29,000-40,000 people. ''')
st.link_button('Source', 'https://aasldpubs.onlinelibrary.wiley.com/doi/pdf/10.1002/hep.30911')
