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


st.markdown('''# Asthma''')
st.write('''Asthma, also called bronchial asthma, is a disease that affects the lungs. It’s a chronic (ongoing) condition. The airways get narrow and swollen, and are blocked by excess mucus. Asthma is broken down into types based on the cause and the severity of symptoms (intermittent or persistent). It can be allergic or non-allergic.''')
st.link_button('Source', 'https://onlinelibrary.wiley.com/doi/full/10.1111/j.1365-2222.2008.02971.x')

st.markdown('### Epidemiology')
st.write('''Asthma affected an estimated 262 million people in 2019 and caused 455 000 deaths.
In the United States, approximately 5% of individuals annually report physician-diagnosed cases of acute bronchitis. The numbers tend to peak during winter, aligning with the seasonal prevalence of respiratory viral infections like influenza, which often coincide with flu season.''')
st.link_button('Source', 'https://www.thelancet.com/pb-assets/Lancet/gbd/summaries/diseases/asthma.pdf')
