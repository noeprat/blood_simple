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


st.markdown('''# DiGeorge syndrome (rare)''')
st.write('''DiGeorge syndrome is a genetic condition caused by a missing piece of chromosome 22. Another name for DiGeorge syndrome is 22q11.2 deletion syndrome. Symptoms can affect the heart, immune system and other body systems, and cause distinct facial characteristics. Treatment to manage the symptoms is lifelong and there is no cure yet for the condition.''')
st.link_button('Source', 'https://www.perinatology.theclinics.com/article/S0095-5108(05)00087-4/fulltext')

st.markdown('### Epidemiology')
st.write('''The incidence of DiGeorge syndrome is 1 in every 3000–6000 births.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC5916974/')
