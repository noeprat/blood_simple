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


st.markdown('''# Metabolic acidosis''')
st.write('''Metabolic acidosis is when acids build up in the body fluids. It can develop when too many acids in the blood wipe out bicarbonate (a base) or when too much bicarbonate in the blood is lost as a result of kidney disease.''')
st.link_button('Source', 'https://www.nature.com/articles/nrneph.2010.33')

st.markdown('### Epidemiology')
st.write('''Metabolic acidosis occurs in about 20% of patients with chronic kidney disease.''')
st.link_button('Source', 'https://karger.com/kdd/article/7/6/452/824539/Metabolic-Acidosis-in-Patients-with-CKD')
