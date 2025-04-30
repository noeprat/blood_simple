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


st.markdown('''# Bilirubin''')
st.write('''Bilirubin is an orange-yellow pigment from the breakdown of old red blood cells. The liver sorts bilirubin with other waste products into a fluid called bile. Bile exits the body through the intestines.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S0957583905001442')

st.markdown('### Associated diseases')
st.markdown('**Upregulation could be a sign of:**')
st.page_link('other_pages/diseases/Hemolyticanemia.py', label='''Hemolytic anemia ''')
st.page_link('other_pages/diseases/Sicklecelldisease.py', label=''' Sickle cell disease ''')
st.page_link('other_pages/diseases/Gallstones.py', label=''' Gallstones ''')
st.page_link('other_pages/diseases/Cholecystitis.py', label=''' Cholecystitis ''')
st.page_link('other_pages/diseases/Cholangitis.py', label=''' Cholangitis ''')
st.page_link('other_pages/diseases/Liverdisease.py', label=''' Liver disease''')
st.markdown('**Downregulation could be a sign of:**')
st.markdown('Typically not problematic.')
