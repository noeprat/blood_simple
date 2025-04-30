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


st.markdown('''# Heart failure''')
st.write('''Heart failure means that the heart is unable to pump blood around the body properly. It usually happens because the heart has become too weak or stiff.''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S1054880711001529')

st.markdown('### Epidemiology')
st.write('''An estimated 64.3 million people are living with heart failure worldwide.''')
st.link_button('Source', 'https://onlinelibrary.wiley.com/doi/full/10.1002/ejhf.1858')
