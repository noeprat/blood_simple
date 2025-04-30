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


st.markdown('''# HIV''')
st.write('''Human immunodeficiency virus (HIV) is the virus that causes acquired immune deficiency syndrome (AIDS). HIV weakens the immune system by destroying the T-cells until it is unable to fight off even minor illnesses. AIDS is the final and most serious stage of an HIV infection. People with AIDS have very low counts of certain white blood cells and severely damaged immune systems.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC4924471/')

st.markdown('### Epidemiology')
st.write('''Globally, 39.0 million people were living with HIV at the end of 2022. ''')
st.link_button('Source', 'https://www.who.int/data/gho/data/themes/hiv-aids')
