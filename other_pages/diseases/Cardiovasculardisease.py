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


st.markdown('''# Cardiovascular disease''')
st.write('''Cardiovascular diseases are conditions affecting the heart or blood vessels. They are usually associated with a build-up of fatty deposits inside the arteries (atherosclerosis) and an increased risk of blood clots. A cardiovascular disease can also be associated with damage to arteries in organs such as the brain, heart, kidneys and eyes.
There are several types of cardiovascular disease. Coronary heart disease, strokes, peripheral arterial disease and aortic disease are the four main types.''')
st.link_button('Source', 'https://www.nhs.uk/conditions/cardiovascular-disease/')

st.markdown('### Epidemiology')
st.write('''Prevalent cases of cardiovascular diseases reached 523 million in 2019. It is the leading cause of disease burden in the world.''')
st.link_button('Source', 'https://www.ncbi.nlm.nih.gov/pmc/articles/PMC7755038/#:~:text=Prevalent%20cases%20of%20total%20CVD,to%2019.7%20million)%20in%202019%20(')
