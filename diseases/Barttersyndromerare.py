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


st.markdown('''# Bartter syndrome (rare)''')
st.write('''Bartter syndrome is a group of very similar kidney disorders that cause an imbalance of potassium, sodium, chloride, and related molecules in the body.''')
st.link_button('Source', 'https://www.tandfonline.com/doi/full/10.2147/IJNRD.S155397')

st.markdown('### Epidemiology')
st.write('''Bartter syndrome is seen in 1 in 1,000,000 individuals.''')
st.link_button('Source', 'https://www.orpha.net/en/disease/detail/112')
