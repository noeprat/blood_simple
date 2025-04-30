import streamlit as st
import pandas as pd
from streamlit import session_state as ss
import json
import re

parameters_df = pd.read_excel('data/parameters.xlsx')

if 'has_submitted' not in ss:
    ss['has_submitted'] = False

def create_page_name(df):
    page_name = {
        "Haemoglobin": "Hemoglobin.py",
        "Platelet Count": "Plateletcount.py"
    }   #an example made manually


    for index, row in df.iterrows():
        # Extract information from the row
        alt_params = row[0].split(';')
        first_param = alt_params[0].strip()
        first_param_clean = re.sub(r'[^\w]', '', first_param)
        file_name = f"{first_param_clean}.py"

        # Create a new Python file for each row
        for param in alt_params:
            param = param.strip()
            param_clean = re.sub(r'[^\w]', '', param)
            page_name[param_clean] = file_name 
    return page_name



def save_as_json(df, sex, age, dict):
    dict["patient"]["age"] = age
    dict["patient"]["sex"] = sex
    for i, row in df.iterrows():
        dict["results"][row['Test']] = {
            "value": float(row['Result']),
            "interval_low": float(row['Reference range min']),
            "interval_high": float(row['Reference range max']),
            "unit": row['Unit']
        }
    with open('app_data/results.json', 'w') as file:
        json.dump(dict, file)


st.set_page_config(page_title="Verify your data")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #F3CFC6;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

form = st.form(key='my-form')
#name = form.text_input('Name:')

results = pd.read_json('app_data/results.json')
results_dict = results.to_dict()

try:
    index_sex = ['none', 'female', 'male', 'other / does not want to precise'].index(results_dict['patient']['sex'])
except:
    index_sex = 0

gender = form.selectbox('Sex:', ['None', 'Female', 'Male', 'Other / Does not want to precise'], key='sex', index=index_sex)
age = form.number_input('Age:', key='age', min_value=0, max_value=150, step=1, value=int(results_dict['patient']['age']))

blood_samples = results_dict['results']

df = pd.DataFrame(
    [
        {"Test": name, "Result": res['value'], "Reference range min": res['interval_low'], "Reference range max": res['interval_high'], "Unit": res['unit']}
        for name, res in blood_samples.items()
        if name not in ["age", "sex", "name", 'lab']
    ]
)

edited_df = form.data_editor(df, num_rows="dynamic")

st.write('Press submit to confirm your blood tests')
submit = form.form_submit_button('Confirm')

if submit or ss['has_submitted']:
    ss['has_submitted'] = True
    st.dataframe(edited_df.style.apply(
        lambda x: ['background-color: yellow' if float(x['Result']) < float(x['Reference range min']) or float(x['Result']) > float((x['Reference range max'])) else '' for i in x], axis=1
        ),
                 hide_index=True)

    save_as_json(edited_df, ss.sex, ss.age, results_dict)

    too_high_features = []
    too_low_features = []

    for index, row in edited_df.iterrows():
   
        x = row['Result']
        x_inf = row['Reference range min']
        x_sup = row['Reference range max']
        feature = row['Test']

        if x > x_sup:
            too_high_features.append(feature)
        elif x < x_inf:
            too_low_features.append(feature)

    page_name = create_page_name(parameters_df)


    # manual adjustments
    page_name['RBC Count'] = "Redbloodcount.py"
    page_name['Total WBC Count'] = "Whitebloodcellcount.py"

    st.markdown("## You have a higher rate than reference for the following quantities:")
    for feature in too_high_features:
        if feature in page_name.keys():
            st.page_link("other_pages/parameters/"+ page_name[feature], label=feature)  
        else:
            st.markdown(feature)
        st.write("  \n")

    st.markdown("## You have a lower rate than reference for the following quantities:")
    for feature in too_low_features:
        if feature in page_name.keys():
            st.page_link("other_pages/parameters/"+ page_name[feature], label=feature)  
        else:
            st.markdown(feature)
        st.write("  \n") 


