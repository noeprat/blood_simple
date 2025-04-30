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


st.markdown('''# Chronic kidney disease''')
st.write('''Chronic kidney disease is a condition in which the kidneys can no longer adequately filter waste products from the blood. The disease is called “chronic” because kidney function slowly decreases over time.''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(11)60178-5/abstract')

st.markdown('### Epidemiology')
st.write('''Chronic kidney disease is a progressive condition that affects >10% of the general population worldwide.''')
st.link_button('Source', 'https://pubmed.ncbi.nlm.nih.gov/35529086/#:~:text=Chronic%20kidney%20disease%20is%20a,experiencing%20diabetes%20mellitus%20and%20hypertension.')
