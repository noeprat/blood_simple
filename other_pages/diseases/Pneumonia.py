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


st.markdown('''# Pneumonia ''')
st.write('''Pneumonia is an infection in the lungs caused by bacteria, viruses or fungi. Pneumonia causes the lung tissue to swell (inflammation) and can cause fluid or pus in the lungs. Bacterial pneumonia is usually more severe than viral pneumonia, which often resolves on its own. Pneumonia can affect one or both lungs.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S0272523121009758')

st.markdown('### Epidemiology')
st.write('''Pneumonia killed more than 808 000 children under the age of 5 in 2017, accounting for 15% of all deaths of children under 5 years.  People at-risk for pneumonia also include adults over the age of 65 and people with preexisting health problems.''')
st.link_button('Source', 'https://www.who.int/health-topics/pneumonia#tab=tab_1')
