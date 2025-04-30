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


st.markdown('''# Eosinophilic esophagitis''')
st.write('''Eosinophilic esophagitis is an inflammation of the esophagus caused by an overabundance of certain white blood cells. Food allergies are thought to be one cause of the condition. Among the symptoms of eosinophilic esophagitis are heartburn, chest pain and difficulty swallowing.''')
st.link_button('Source', 'https://www.nejm.org/doi/full/10.1056/NEJMra1502863')

st.markdown('### Epidemiology')
st.write('''The incidence of eosinophilic esophagitis has increased over the years. The current estimated annual incidence is approximately 10/100,000 cases.''')
st.link_button('Source', 'https://www.giendo.theclinics.com/article/S1052-5157(17)30082-X/fulltext')
