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


st.markdown('''# Pancreatitis''')
st.write('''Pancreatitis is inflammation in the pancreas. Inflammation causes swelling and pain. The pancreas is an organ sitting between the stomach and the spine. It is involved in digestion and regulating the blood sugar (glucose).''')
st.link_button('Source 1', 'https://www.hopkinsmedicine.org/health/conditions-and-diseases/pancreatitis')
st.link_button('Source 2', 'https://www.sciencedirect.com/science/article/pii/S1743919115010730')

st.markdown('### Epidemiology')
st.write('''The incidence of acute pancreatitis is around 30 cases per 100'000 population overall per year.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4489350/')
