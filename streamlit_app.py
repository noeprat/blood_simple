# Start with:
# python -m streamlit run streamlit_app.py
# or:
# streamlit run streamlit_app.py

import os
import streamlit as st
#from st_pages import show_pages_from_config
from st_pages import Page, Section, show_pages, add_page_title


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

#show_pages_from_config()

st.markdown('# Welcome to Blood Simple !')

st.markdown('### *Decoding your blood drop by drop*')

st.markdown("""
            Blood results are hard to interpret, and having results out of range can be scary.
            Blood Simple is here to help you understand all your results. It provides simple information about all parameters measured, descriptions of potential diseases linked to abnormal values and scientific references in case you want to learn more.
            Your privacy is preserved as no data extracted is stored on a central server.
""")

st.markdown('# Get started')

show_pages(
    [
        Page("streamlit_app.py", "Home", "🏠"),
        Page("pages/load.py", "Load your data", "📤"),
        Page("pages/verify.py", "Verify your data", "🔍"),
        Page("pages/chatbot.py", "Chatbot", "💬"),
        Page("pages/feedback.py", "Give your feedback", "💭"),
        Section(name="Parameters", icon="🩸"),
        # Pages after a section will be indented unless you explicitly say in_section=False
        Page("other_pages/parameters/Alaninetransaminase.py", "Alanine transaminase"),
        Page("other_pages/parameters/Albumin.py"),
        Page("other_pages/parameters/Alkalinephosphatase.py", "Alkaline phosphatase"),
        Page("other_pages/parameters/Aspartateaminotransferase.py", "Aspartate aminotransferase"),
        Page("other_pages/parameters/Basophils.py"),
        Page("other_pages/parameters/Bicarbonate.py"),
        Page("other_pages/parameters/Bilirubin.py"),
        Page("other_pages/parameters/Bloodureanitrogen.py", "Blood urea nitrogen"),
        Page("other_pages/parameters/Calcium.py"),
        Page("other_pages/parameters/Chloride.py"),
        Page("other_pages/parameters/Creatinine.py"),
        Page("other_pages/parameters/Eosinophils.py"),
        Page("other_pages/parameters/Glucose.py"),
        Page("other_pages/parameters/Hematocrit.py"),
        Page("other_pages/parameters/Hemoglobin.py"),
        Page("other_pages/parameters/Lymphocytes.py"),
        Page("other_pages/parameters/Meancorpuscularhemoglobin.py", "Mean corpuscular hemoglobin"),
        Page("other_pages/parameters/Meancorpuscularhemoglobinconcentration.py", "Mean corpuscular hemoglobin concentration"),
        Page("other_pages/parameters/Meancorpuscularvolume.py", "Mean corpuscular volume"),
        Page("other_pages/parameters/Meanplateletvolume.py", "Mean platelet volume"),
        Page("other_pages/parameters/Monocytes.py"),
        Page("other_pages/parameters/Neutrophils.py"),
        Page("other_pages/parameters/Plateletcount.py", "Platele count"),
        Page("other_pages/parameters/Potassium.py"),
        Page("other_pages/parameters/Redbloodcount.py", "Red blood count"),
        Page("other_pages/parameters/Redcelldistributionwidth.py", "Red celld istribution width"),
        Page("other_pages/parameters/Sodium.py"),
        Page("other_pages/parameters/Totalprotein.py", "Total protein"),
        Page("other_pages/parameters/Whitebloodcellcount.py", "White blood cell count"),
        
        Section(name="Diseases", icon="🦠"),
        Page("other_pages/diseases/Addisondiseaserare.py", "Addison disease (rare)"),
        Page("other_pages/diseases/Alcoholusedisorder.py", "Alcohol use disorder"),
        Page("other_pages/diseases/Anemia.py"),
        Page("other_pages/diseases/Aplasticanemia.py"),
        Page("other_pages/diseases/Asthma.py"),
        Page("other_pages/diseases/Autoimmunedisease.py", "Autoimmune disease"),
        Page("other_pages/diseases/Barttersyndromerare.py", "Bartter syndrome (rare)"),
        Page("other_pages/diseases/Betathalassemia.py"),
        Page("other_pages/diseases/Blooddisease.py", "Blood disease"),
        Page("other_pages/diseases/Bronchitis.py"),
        Page("other_pages/diseases/Cancer.py"),
        Page("other_pages/diseases/Cardiovasculardisease.py", "Cardiovascular disease"),
        Page("other_pages/diseases/Celiacdisease.py", "Celiac disease"),
        Page("other_pages/diseases/Cholangitis.py"),
        Page("other_pages/diseases/Cholecystitis.py"),
        Page("other_pages/diseases/Chronickidneydisease.py", "Chronic kidney disease"),
        Page("other_pages/diseases/Cirrhosis.py"),
        Page("other_pages/diseases/Congenitalheartdefect.py", "Congenital heart defect"),
        Page("other_pages/diseases/Crohnsdisease.py", "Crohns disease"),
        Page("other_pages/diseases/Cushingsyndrome.py", "Cushing syndrome"),
        Page("other_pages/diseases/DiGeorgesyndromerare.py", "Di George syndrome (rare)"),
        Page("other_pages/diseases/Diabetes.py"),
        Page("other_pages/diseases/Emphysema.py"),
        Page("other_pages/diseases/Eosinophilicesophagitis.py", "Eosinophilic esophagitis"),
        Page("other_pages/diseases/Fattyliverdisease.py", "Fatty liver disease"),
        Page("other_pages/diseases/Gallstones.py"),
        Page("other_pages/diseases/Gastrointestinalbleeding.py", "Gastrointestinal bleeding"),
        Page("other_pages/diseases/HIV.py"),
        Page("other_pages/diseases/Heartattack.py", "Heart attack"),
        Page("other_pages/diseases/Heartfailure.py", "Heart failure"),
        Page("other_pages/diseases/Hemolyticanemia.py"),
        Page("other_pages/diseases/Hemolyticuremicsyndrome.py", "Hemolyticuremic syndrome"),
        Page("other_pages/diseases/Hepatitis.py"),
        Page("other_pages/diseases/Hodgkinlymphoma.py", "Hodgkin lymphoma"),
        Page("other_pages/diseases/Hyperparathyroidism.py"),
        Page("other_pages/diseases/Hyperthyroidism.py"),
        Page("other_pages/diseases/Hyponatremia.py"),
        Page("other_pages/diseases/Hypothyroidism.py"),
        Page("other_pages/diseases/Immunethrombocytopenia.py", "Immune thrombocytopenia"),
        Page("other_pages/diseases/Infection.py"),
        Page("other_pages/diseases/Inflammatoryboweldisease.py", "Inflammatory bowel disease"),
        Page("other_pages/diseases/Ketoacidosis.py"),
        Page("other_pages/diseases/Kidneydisease.py", "Kidney disease"),
        Page("other_pages/diseases/Kidneystones.py", "Kidney stones"),
        Page("other_pages/diseases/Leukemia.py"),
        Page("other_pages/diseases/Liverdisease.py", "Liver disease"),
        Page("other_pages/diseases/Lupus.py"),
        Page("other_pages/diseases/Lymedisease.py", "Lyme disease"),
        Page("other_pages/diseases/Lymphoma.py"),
        Page("other_pages/diseases/Malnutrition.py"),
        Page("other_pages/diseases/Metabolicacidosis.py", "Metabolic acidosis"),
        Page("other_pages/diseases/Metabolicalkalosis.py", "Metabolic alkalosis"),
        Page("other_pages/diseases/Mononucleosis.py"),
        Page("other_pages/diseases/Musculardystrophy.py", "Muscular dystrophy"),
        Page("other_pages/diseases/Myelodysplasticsyndrome.py", "Myelodysplastic syndrome"),
        Page("other_pages/diseases/Myelofibrosis.py"),
        Page("other_pages/diseases/Osteoporosis.py"),
        Page("other_pages/diseases/Osteosarcoma.py"),
        Page("other_pages/diseases/Pagetsdiseaseofthebone.py", "Pagets disease of the bone"),
        Page("other_pages/diseases/Pancreatitis.py"),
        Page("other_pages/diseases/Perniciousanemia.py", "Pernicious anemia"),
        Page("other_pages/diseases/Pneumonia.py"),
        Page("other_pages/diseases/Polycythemiavera.py", "Polycythemia vera"),
        Page("other_pages/diseases/Preeclampsia.py"),
        Page("other_pages/diseases/Pulmonaryfibrosis.py", "Pulmonary fibrosis"),
        Page("other_pages/diseases/Respiratoryacidosis.py", "Respiratory acidosis"),
        Page("other_pages/diseases/Respiratoryalkalosis.py", "Respiratory alkalosis"),
        Page("other_pages/diseases/Rheumatoidarthritis.py", "Rheumatoid arthritis"),
        Page("other_pages/diseases/Sarcoidosis.py"),
        Page("other_pages/diseases/Sepsis.py"),
        Page("other_pages/diseases/Severecombinedimmunodeficiencyrare.py", "Severe combined immunodeficiency (rare)"),
        Page("other_pages/diseases/Sicklecelldisease.py", "Sickle cell disease"),
        Page("other_pages/diseases/Syphilis.py"),
        Page("other_pages/diseases/Thrombocytosis.py"),
        Page("other_pages/diseases/Tuberculosis.py"),
        Page("other_pages/diseases/Wilsondiseaserare.py", "Wilson disease (rare)"),
        Page("other_pages/diseases/WiskottAldrichsyndromerare.py", "Wiskott-Aldrich syndrome (rare)")
    ]
)

st.markdown("## Blood test parameters")

st.markdown("""
            Your blood serves numerous roles to maintain your health. 
            To carry out these functions, blood contains a multitude of components, including red blood cells that transport oxygen, nutrients and hormones; white blood cells that remove waste products and support the immune system; plasma that regulates temperature; and platelets that help with clotting.

            Within the blood are also numerous molecules formed as byproducts of **normal biochemical functions**. 
            These molecules indicate how your cells are responding to disease, injury or stress. 
            Thus, molecules in a blood sample can represent a snapshot of the current biochemical state of your body, and analyzing them can provide information about various aspects of your health.
            
            Each parameter has a **reference range**. It is the range of results that is considered to be normal. 
            The ranges are based on the test results from large groups of healthy people. 
            A test may have different reference ranges for different groups of people. For example, there may be separate ranges for children and adults.
            
            Labs use different reference ranges to describe normal results. That is because they often use different testing methods.

            If your test result is higher or lower than the range that applies to you, it may be a sign of a health problem, but not always. 
            The accuracy of certain test results may be affected by eating and drinking certain foods, taking certain medicines or supplements, exercising hard before your test or having a menstrual period at the time of you are tested. 

            Check the "🩸 Parameters" folder for more details on each parameter.
            """
)

st.markdown("## Diseases")

st.markdown("""
            Many possible diseases linked to abnormal blood parameter values are described. 
            
            For each of them, if it is available, you have access to **epidemiology data**. 

            **Incidence** refers to the number of new cases of a disease or health condition that develop within a defined population during a specified period of time.
            It essentially measures the rate of occurrence of new cases.
            
            **Prevalence** refers to the total number of existing cases of a disease or health condition within a defined population at a specific point in time or over a period of time. 
            Prevalence includes both new and existing cases. It provides insights into how widespread a disease or condition is within a population.

            Check the "🦠 Diseases" folder for more details on each parameter.
            """)


