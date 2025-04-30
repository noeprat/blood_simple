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


st.markdown('''# Polycythemia vera''')
st.write('''Polycythemia vera is a type of chronic leukemia (blood cancer) that causes the bone marrow to produce too many red blood cells. Too many red blood cells can make the blood thick and sluggish and increase the risk of blood clots and complications such as heart attack and stroke.''')
st.link_button('Source', 'https://ashpublications.org/blood/article/100/13/4272/106060/Polycythemia-vera-myths-mechanisms-and-management')

st.markdown('### Epidemiology')
st.write('''The incidence of polycythemia vera ranges from 0.4 to 2.8 per 100 000 per year.''')
st.link_button('Source', 'https://onlinelibrary.wiley.com/doi/abs/10.1111/ejh.12256?casa_token=TGnad9daAO8AAAAA:nxq_UTBCta5l6gMDSPxgy5TMaYX8jGR8UKsQV59uB96ISFcvzLduClmm_BU-h3GOw4elYmQ4KJCvPRo0')
