# BIO 512 - Project Blood Simple 🧬📊

## 📋 Team Composition

- Name 1: Alice Granboulan
- Name 2: Noé Prat
- Name 3: Nicolas Moyne


## 🎯 Project Details

### Project Name:
`Blood Simple`  

### Short Description:
Blood Simple aim to help people understand their **blood results**. 

Blood results are hard to interpret, especially for non-scientific people. With Blood Simple, they only have to upload a pdf and an interactive window will give them well-documented insights on their blood results. This tool will be impactful as there is a growing interest in understanding one’s own health, and incomprehensible test results are a source of stress. Moreover, it can help patients to understand the doctor's decisions and to improve their health. Lastly, it could help doctors to save some of their precious time by answering some of questions of patients that are non vital for their health.

Blood Simple will be a user-friendly webapp, using image text recognition to extract blood test data from a pdf. The bibliography supporting scientific knowledge will be accessible to users. The privacy of users will be preserved as no data extracted from pdf is stored on a central server. It will be constantly updated, taking into account users' questions.

### Project planning:
| Milestone                 | Tasks |
|--------------------|-------------|
| Ideation (week 8-9) | <ul><li>Literature review (blood data from CBC and BMP). </li><li> Tools for webapp development. </li><li> Loading and processing of pdf or image. </li><li> Creation of a database. </li></ul> |
| Initial prototype development (week 10-11) | <ul><li> Webapp with interactive features. </li><li> Information on the parameter measured, diseases linked to it and potential leverages. </li><li> Chatbot with sourced information. </li></ul>|
| Advanced prototype developemnt (week 12-13) | <ul><li> Combining pdf processing, chatbot and description pages on the webapp. </li><li> Prettier and more user-friendly visualization. </li><li> Integration of different presentations of blood results on pdf. </li><li> Implementation of a tool to ask questions. </li></ul>  |

### Tech Stack:
Type `pip install -r requirements.txt` to get necessary packages. Besides, you will need to install Pytesseract on `C:\\Program Files\\Tesseract-OCR\\`:
- pandas
- numpy
- llama-index
- pydantic
- pytesseract (python library for OCR - installation of Pytesseract software is mandatory)
- PyPDF2
- time
- streamlit
- OpenAI (an API key is necessary)

Once all packages are installed, type `streamlit run streamlit_app.py`.

### Data Sources:
- Complete blood count (CBC) test.
- Comprehensive metabolic panel (CMP) test.
- Scientific papers to support blood parameters description and the diseases related (description and epidemiology).


## 🚀 Getting Started
To kick off your project, consider the following steps:

1. **Project Planning:** Outline your project goals, milestones, and deadlines. Use the 'Issues' feature in this Git repository for task management and tracking progress.
2. **Research:** Conduct a preliminary literature review or research on your topic to gather insights and methodologies that might be beneficial.
3. **Data Collection:** Begin your data collection or secure your data sources as per the project requirements.

## 📈 Assessment
**NOTE**: _Please do not edit anything in this section_

Your project assessments will be recorded and tracked through pre-created issue pages on GitLab. Below is a summary table where your scores will be updated following each assessment.


| Milestone                 | Date | Weight (%) | Score | Notes |
|---------------------------|------|--------|-------|-------|
| [Assessment 1](#1) | `22.04.2024`  | **5%**    | -   | -   |
| [Assessment 2](#2) | `06.05.2024`  | **10%**    | -   | -   |
| [Assessment 3](#3) | `23.05.2024`  | **5%**    | -   | -   |
| [Final Report Assessment](#4) | `30.05.2024`  | **20%**    | -   | -   |

## 📝 Reporting

You and your team will have to present the project multiple times throughout the project phase, 
and we request you to place that all the such presentations in the [presentations directory](presentations/) in this repository. 

Additionally, you will have to submit a Project report at the end of the project phase, which we request you to (eventually) place in the [reports](reports/) directory. 

## ❓ Support
If you have any questions or need assistance with your project, please don't hesitate to reach out to your instructors or TAs. You can also use the 'Discussions' feature in this Git repository for general queries or to seek help from your peers.

