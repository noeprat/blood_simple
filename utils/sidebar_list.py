import os

def load_pages(folder_path):
    filenames = sorted(os.listdir(folder_path))
    for filename in filenames:
        page_path = os.path.join(folder_path, filename)
        print(f'Page("{page_path}"),')

param_folder_path = "other_pages/parameters"
load_pages(param_folder_path)

diseases_folder_path = "other_pages/diseases"
load_pages(diseases_folder_path)
