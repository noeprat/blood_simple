import streamlit as st

container_1 = st.container()
container_1.empty() 


def print_fdbk():
    print(st.session_state.fbk)
    st.session_state.qry = ""

st.markdown('# Help us improve Blood Simple !')


with st.form("feedback_form"):
    satisfaction = st.select_slider(
        "How do you feel about this app ?",
        options=["Please stop coding apps", "Very unsatisfied", "Quite unsatisfied", "Neutral", "Quite satisfied", "Very satisfied", "Bloody satisfied"]
        )

    feedback = st.text_input('Write below any question or comment about this app.', key='fbk')
    submitted_feedback = st.form_submit_button('Submit feedback', on_click=print_fdbk)
    
    if submitted_feedback:
        st.write('Opinion:',satisfaction)
        st.write(feedback)
        st.markdown('\n**Thank you for your input !**')
