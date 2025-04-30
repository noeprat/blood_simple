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


st.markdown('''# Sickle cell disease''')
st.write('''Sickle cell disease is the most common inherited blood disorder. It affects the red blood cells. A protein called hemoglobin, located within red blood cells and carrying oxygen, is abnormal. Normal red blood cells are round and flexible, which allows them to move easily through small blood vessels (capillaries) in the body to deliver oxygen to organs and tissues. In sickle cell disease, abnormal hemoglobin S changes the shape of the red blood cell to a crescent shape and causes them to become rigid, lack flexibility and stick together. This can block blood flow, preventing oxygen from getting to the vital organs and tissues throughout the body. ''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(10)61029-X/fulltext')

st.markdown('### Epidemiology')
st.write('''The prevalence of sickle-cell disease is highest in sub-Saharan Africa. More than 230 000 affected children are born in this region every year (0.74% of the births), which is about 80% of the global total. By comparison, the yearly estimate of affected births in North America is 2600 and 1300 in Europe.''')
st.link_button('Source', 'https://www.thelancet.com/journals/lancet/article/PIIS0140-6736(10)61029-X/fulltext')
