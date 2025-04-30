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


st.markdown('''# Beta-thalassemia''')
st.write('''Beta-thalassemia is an inherited blood disorder. It affects the body’s ability to produce normal hemoglobin. Hemoglobin is a protein in red blood cells which allows them to transport oxygen throughout the body. Beta-thalassemia may cause to experience anemia-like symptoms that range from mild to severe. Treatment can consist of blood transfusions and iron chelation therapy.''')
st.link_button('Source', 'https://link.springer.com/article/10.1186/1750-1172-5-11')

st.markdown('### Epidemiology')
st.write('''The total annual incidence of symptomatic individuals is estimated at 1 in 100'000 throughout the world.''')
st.link_button('Source', 'https://link.springer.com/article/10.1186/1750-1172-5-11')
