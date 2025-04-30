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


st.markdown('''# Respiratory alkalosis''')
st.write('''Respiratory alkalosis involves an increase in respiratory rate and/or tidal volume (hyperventilation). Hyperventilation occurs most often as a response to hypoxia, metabolic acidosis, increased metabolic demands (as fever), pain, or anxiety.''')
st.link_button('Source', 'https://europepmc.org/article/med/11262557')
