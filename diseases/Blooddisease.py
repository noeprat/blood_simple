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


st.markdown('''# Blood disease''')
st.write('''Blood is a body fluid that delivers necessary substances such as nutrients and oxygen to the cells, and transports metabolic waste products away from those same cells. 
Common blood disorders include anemia, sickle cell disease, bleeding disorders such as hemophilia, blood clots, and blood cancers such as leukemia, lymphoma, and myeloma.''')
st.link_button('Source', 'https://www.hematology.org/education/patients/blood-disorders#:~:text=Common%20blood%20disorders%20include%20anemia,may%20have%20a%20blood%20condition.')
