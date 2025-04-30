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


st.markdown('''# Sarcoidosis''')
st.write('''Sarcoidosis is a condition that causes the immune system to overreact and make lumps or nodules called granulomas. Granulomas can be found almost anywhere in the body, but they are most commonly found in the lungs or lymph nodes. There can also be noticeable symptoms of granulomas in the skin, eyes or muscles.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S0272523108000312?casa_token=Yc-fdo-I-TUAAAAA:ozLujerkqDbmLvA_XFIqOeOqGW_Wc4KSfV8s4iXHRXRigljCzrzhSswoTJ-2eMAwliYbjiYo8FJd')

st.markdown('### Epidemiology')
st.write('''Recent studies report a prevalence of sarcoidosis greater than 0.05% of the population.''')
st.link_button('Source', 'https://journals.sagepub.com/doi/full/10.1177/2040622318790197')
