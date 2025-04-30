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


st.markdown('''# Autoimmune disease''')
st.write('''An autoimmune disease is the result of the immune system accidentally attacking the body instead of protecting it. It's unclear why the immune system does this.
There are over 100 known autoimmune diseases. Common ones include lupus, rheumatoid arthritis, Crohn’s disease and ulcerative colitis.''')
st.link_button('Source', 'https://www.nejm.org/doi/full/10.1056/NEJM200108023450506?casa_token=lmvEJzKQPAkAAAAA:zZwHtPiGnkbLYTpGxrO0pFHd8dqSgc31uugdvHTobRVIbWeadk10SsyqaWlyWaCTasLEmpHa8zGpScZu&casa_token=dWokji3SXtQAAAAA:Xy60RGVFCLRMrTNyWYe_cYNehIvz1f8MCxnw-FDMAHcvzKPKaTaFhAbG4cnFMriTJgSujXNQYsDST3Cd')

st.markdown('### Epidemiology')
st.write('''Prevalence rates range from less than 5 per 100'000 (e.g. chronic active hepatitis, uveitis) to more than 500 per 100'000 (Grave disease, rheumatoid arthritis, thyroiditis). ''')
st.link_button('Source', 'https://www.sciencedirect.com/science/article/pii/S1568997203000065?casa_token=hRWUqTZIWU0AAAAA:SHBAKUF-HMaIA-V6ek0ScwXJxVHmj5yDhEb6x4DqwpjuTK2mq3tC708c7sD6Gs2jXOuL5HTC9WMs')
