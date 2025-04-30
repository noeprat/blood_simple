import pandas as pd
import os
import re

df = pd.read_excel('data/parameters.xlsx')

for index, row in df.iterrows():
    # Extract information from the row
    param = row[0].split(';')[0].strip() 
    role = row[3]          
    source = row[4]
    disease_high = row[5].split(';')
    disease_low = row[6].split(';')
    
    # Create a new Python file for each row
    param_clean = re.sub(r'[^\w]', '', param)
    file_name = f"{param_clean}.py"
    output_dir = 'other_pages/parameters'
    file_path = os.path.join(output_dir, file_name)
    
    with open(file_name, 'w') as file:
        file.write(f"import streamlit as st\n\n")
   
        file.write(f"st.markdown(\n")
        file.write(f"    '''\n")
        file.write(f"    <style>\n")
        file.write(f"    .stApp {{\n")
        file.write(f"        background-color: #F2D2BD;\n")
        file.write(f"        color: black;\n")
        file.write(f"    }}\n")
        file.write(f"    </style>\n")
        file.write(f"    ''',\n")
        file.write(f"    unsafe_allow_html=True\n")
        file.write(f")\n\n")

        file.write(f"\nst.markdown('''# {param}''')\n")
        file.write(f"st.write('''{role}''')\n")
        file.write(f"st.link_button('Source', '{source}')\n")

        file.write(f"\nst.markdown('### Associated diseases')\n")
        file.write(f"st.markdown('**Upregulation could be a sign of:**')\n")
        for disease in disease_high:
            disease_clean = re.sub(r'[^\w]', '', disease)
            if os.path.exists(f"other_pages/diseases/{disease_clean}.py"):
                file.write(f"st.page_link('other_pages/diseases/{disease_clean}.py', label='''{disease}''')\n")
            else:
                file.write(f"st.markdown('{disease}')\n")
        file.write(f"st.markdown('**Downregulation could be a sign of:**')\n")
        for disease in disease_low:
            disease_clean = re.sub(r'[^\w]', '', disease)
            if os.path.exists(f"other_pages/diseases/{disease_clean}.py"):
                file.write(f"st.page_link('other_pages/diseases/{disease_clean}.py', label='''{disease}''')\n")
            else:
                file.write(f"st.markdown('{disease}')\n")
    
    print(f"Created file: {file_name}")

print("All parameter files created successfully.")
