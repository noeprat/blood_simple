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


st.markdown('''# Osteosarcoma''')
st.write('''Osteosarcoma (osteogenic sarcoma) is a type of cancer that starts in the bones. Cancer cells create tumors, and those tumors create immature, irregular, diseased bone. It is most often seen in teenagers, with the average age of diagnosis of osteosarcoma being 15.''')
st.link_button('Source 1', 'https://www.tandfonline.com/doi/abs/10.1080/07357907.2020.1768401')
st.link_button('Source 2', 'https://www.nature.com/articles/s41571-021-00519-8')

st.markdown('### Epidemiology')
st.write('''The incidence of osteosarcoma in the general population is 2–3 per million of people per year, but is higher in adolescence, in which the annual incidence peaks at 8–11 per million of people per year at 15–19 years of age.''')
st.link_button('Source', 'https://www.tandfonline.com/doi/abs/10.1080/07357907.2020.1768401')
