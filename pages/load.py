import streamlit as st
from PyPDF2 import PdfReader
from pydantic import BaseModel, Field
from typing import List

from llama_index.program.openai import OpenAIPydanticProgram
from llama_index.core import ChatPromptTemplate
from llama_index.core.llms import ChatMessage
from llama_index.llms.openai import OpenAI

import os
from typing import Union
import json
import pytesseract
from pdf2image import convert_from_path
import tempfile
from PIL import Image
import io


st.set_page_config(page_title="Load your results")
st.title("Load your results")

api_key = os.getenv("OPENAI_API_KEY")
llm = OpenAI(api_key=api_key)


class CallSummary(BaseModel):
    """Data model for a blood test result"""

    molecules: List[List[Union[str, float, int]]] = Field(
        description="List of molecules present in the analysis. Each molecule is represented by a list of 5 values: [name, value, interval_low, interval_high, unit]"
    )
    lab_name: str = Field(description="Name of the lab")
    patient_age: int = Field(description="Age of the patient")
    patient_sex: str = Field(description="Sex of the patient, one of 'None', 'Male', 'Female'")
    patient_name: str = Field(description="Name of the patient")

prompt = ChatPromptTemplate(
    message_templates=[
        ChatMessage(
            role="system",
            content=(
                "You are an expert assitant for extracting data from lab results. When you don't know the answer, put -1 for numbers and also -1 for text and units. If you have a list of molecules + value, and after a list of number1/number3 and both lists ahe the same number of items, you can assume that the second list corresponds to the protein intervals. \n"  
            ),
        ),
        ChatMessage(
            role="user",
            content=(
                "Here is the extraction: \n"
                "------\n"
                "{transcript}\n"
                "------"
            ),
        ),
    ]
)

program = OpenAIPydanticProgram.from_defaults(
    output_cls=CallSummary,
    llm=llm,
    prompt=prompt,
    verbose=False,
)

def list_to_dict(output):
    
    patient = {
        "name": output.patient_name,
        "age": output.patient_age,
        "sex": output.patient_sex.lower()
    }

    molecules = output.molecules
    results = {}
    for molecule in molecules:
        results[molecule[0]] = {
            "value": molecule[1],
            "interval_low": molecule[2],
            "interval_high": molecule[3],
            "unit": molecule[4]
        }
    
    lab_summary = {
        "patient": patient,
        "lab": output.lab_name,
        "results": results
    }

    return lab_summary

def save_summary_as_json(summary):
    with open("app_data/results.json", "w") as file:
        json.dump(summary, file)

def main():
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

    # File uploader
    uploaded_file = st.file_uploader("Upload a file", type=["pdf", "png", "jpg"])

    if uploaded_file is not None:
        s = ""
        is_pdf = uploaded_file.type == "application/pdf"
        # Read the PDF file
        if is_pdf:
            pdf = PdfReader(uploaded_file)
            s = ""
            for page in pdf.pages:
                s = s + str(page.extract_text())
            if s == "":
                pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"

                with tempfile.NamedTemporaryFile(delete=False) as tmp:
                    tmp.write(uploaded_file.getvalue())
                    temp_path = tmp.name
                images = convert_from_path(temp_path)

                for image in images:
                    # Convert image to grayscale
                    image = image.convert('L')

                    # Use pytesseract to extract text
                    text = pytesseract.image_to_string(image)

                    s = s + text
        else:
            pytesseract.pytesseract.tesseract_cmd = "C:\\Program Files\\Tesseract-OCR\\tesseract.exe"
            image = Image.open(io.BytesIO(uploaded_file.read()))
            s = pytesseract.image_to_string(image)
        output = program(transcript=str(s))
        lab_summary = list_to_dict(output)
        save_summary_as_json(lab_summary)
    st.page_link('pages/verify.py', label = '**Verify your data and get your analysis**')

if __name__ == "__main__":
    main()
