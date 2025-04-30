import os
import openai
from openai import OpenAI
import pandas as pd

# Check if parameters.json already exists

def extract_json():
    if not os.path.exists('app_data/parameters.json'):
        # Load the Excel file
        df = pd.read_excel('app_data/parameter.xlsx')

        # Transform the data to JSON
        json_data = df.to_json(orient='records')

        # Save the JSON data to a file
        with open('app_data/parameters.json', 'w') as file:
            file.write(json_data)

    with open('app_data/parameters.json', 'r') as file:
        json_data = file.read()

    # Parse the JSON data
    data = pd.read_json(json_data)

    # Return the parsed data
    return data

def reformat_data(file):
    dict = pd.read_json(file)
    res = "The patient's name is " + dict['patient']['name'] + ".\n"
    res += "The patient's age is " + str(dict['patient']['age']) + ".\n"
    res +=  "The patient's sex is " + str(dict['patient']['sex']) + ".\n"
    res += "The patient's lab is " + dict['lab']['name'] + ".\n"
    for mol in dict['results'].keys():
        if mol not in ['name', 'age', 'sex']:
            res += "The value of " + mol + " is " + str(dict['results'][mol]['value']) + " " + dict['results'][mol]['unit'] + ".\n"
            res += "The reference range for " + mol + " is " + str(dict['results'][mol]['interval_low']) + " - " + str(dict['results'][mol]['interval_high']) + " " + dict['results'][mol]['unit'] + ".\n"
    return res

client = OpenAI(
    api_key=os.getenv('OPENAI_API_KEY')
)

def prompt_from_data():
    #Here we would load info from our excel.

    prompt = "You are a medical assistant here to answer questions related to health issues and blood tests. You have to provide sources when you give information. You must not invent information.\n\n"
    prompt += "You know only a limited number of relevant facts on a few diseases. Those facts are listed after, with sources. Please provide answers only to questions that can be answered using the folloing content. \n\n"
    
    json = extract_json()
    param = json['Blood_parameter']
    test = json['Test']
    role = json['Role']
    sources_role = json['Sources_role']
    diseases_high_level = json['Diseases_high_level']
    diseases_low_level = json['Diseases_low_level']

    prompt = "You are a medical assistant here to answer questions related to health issues and blood tests. You have to provide sources when you give information. You must not invent information. You can provide information on the following topics: \n\n"

    for i in range(len(param)):
        prompt += "Blood parameter: " + param[i]
        prompt += " is evaluated in the following tests: " + test[i] + "."
        prompt += " It has the following role: " + role[i] + "."
        prompt +=" The sources for this information are: " + sources_role[i] + "." 
        prompt +=" Moreover a low value of this parameter can indicate the following diseases: " + diseases_low_level[i] + "." 
        prompt +=" A high value of this parameter can indicate the following diseases: " + diseases_high_level[i] + ".\n\n"

    prompt += "You also know a few things about the patient lab tests !\n\n"
    results = reformat_data("app_data/results.json")
    prompt += results
    
    
    return prompt

class Chatbot:
    def __init__(self):
        self.prompt = prompt_from_data()

    def ask(self, question):
        completion = openai.chat.completions.create(
            model="gpt-4",
            messages=[
                {
                    "role": "system",
                    "content": self.prompt,
                },
                {
                    "role": "user",
                    "content": question,
                },
            ],
        )

        bot_response = completion.choices[0].message.content if completion.choices else "No response."

        return bot_response


