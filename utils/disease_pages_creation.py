import pandas as pd
import os
import re

df2 = pd.read_excel('./data/diseases.xlsx')

for index, row in df2.iterrows():
    # Extract information from the row
    disease = row[0]
    desc = row[1]          
    sources_desc = row[2].split(';')
    epid = row[3] if pd.notna(row[3]) else []
    sources_epid = row[4].split(';') if pd.notna(row[4]) else []
    
    # Create a new Python file for each row
    file_name = f"{disease}.py"
    disease_clean = re.sub(r'[^\w]', '', disease)
    file_name = f"{disease_clean}.py"
    output_dir = 'other_pages/diseases'
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

        file.write(f"\nst.markdown('''# {disease}''')\n")
        file.write(f"st.write('''{desc}''')\n")

        if len(sources_desc) == 1:
            source_clean = sources_desc[0].strip()
            file.write(f"st.link_button('Source', '{source_clean}')\n")
        else:
            for i, source in enumerate(sources_desc, 1):
                source_clean = source.strip()
                file.write(f"st.link_button('Source {i}', '{source_clean}')\n")

        if epid:
            file.write(f"\nst.markdown('### Epidemiology')\n")
            file.write(f"st.write('''{epid}''')\n")

            if len(sources_epid) == 1:
                source_clean = sources_epid[0].strip()
                file.write(f"st.link_button('Source', '{source_clean}')\n")
            else:
                for i, source in enumerate(sources_epid, 1):
                    source_clean = source.strip()
                    file.write(f"st.link_button('Source {i}', '{source_clean}')\n")

    
    print(f"Created file: {file_name}")

print("All disease files created successfully.")