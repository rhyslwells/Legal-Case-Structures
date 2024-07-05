import os

def create_leaf_file(folder_path):
    folder_name = os.path.basename(folder_path)
    file_path = os.path.join(folder_path, f"{folder_name}.txt")
    with open(file_path, 'w') as file:
        file.write('.')

def create_chronological_structure(base_path):
    subfolders = [
        "2022",
        "2023",
        "2024"
    ]

    for year in subfolders:
        year_folder = os.path.join(base_path, year)
        os.makedirs(year_folder, exist_ok=True)

        subfolders = [
            "Pleadings",
            "Orders",
            "Correspondence",
            "Discovery",
            "Motions",
            "Depositions",
            "Research"
        ]

        for folder in subfolders:
            folder_path = os.path.join(year_folder, folder)
            os.makedirs(folder_path, exist_ok=True)
            create_leaf_file(folder_path)

    print("Chronological folder structure created")

def create_client_folder_structure(base_path, client_name):
    subfolders = [
        "Discovery",
        "Proofs of Service",
        "Endorsed Copies",
        "Orders",
        "Correspondence",
        "Pleadings",
        "Client Records",
        "Depositions",
        "Research",
        "Emails",
        "Memos"
    ]

    client_folder = os.path.join(base_path, client_name)
    os.makedirs(client_folder, exist_ok=True)

    for folder in subfolders:
        folder_path = os.path.join(client_folder, folder)
        os.makedirs(folder_path, exist_ok=True)
        create_leaf_file(folder_path)

    print(f"Folder structure created for client: {client_name}")

def create_date_based_structure(base_path):
    years = ["2022", "2023", "2024"]

    for year in years:
        year_folder = os.path.join(base_path, year)
        os.makedirs(year_folder, exist_ok=True)
        create_leaf_file(year_folder)

    print("Date-based folder structure created")

def create_document_based_structure(base_path):
    subfolders = [
        "Petitions",
        "Responses",
        "Motions",
        "Orders",
        "Correspondence",
        "Discovery",
        "Research"
    ]

    for folder in subfolders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        create_leaf_file(folder_path)

    print("Document-based folder structure created")

def create_hybrid_structure(base_path, client_name):
    subfolders = [
        "Pleadings",
        "Orders",
        "Correspondence",
        "Discovery",
        "Motions",
        "Depositions",
        "Research"
    ]

    client_folder = os.path.join(base_path, client_name)
    os.makedirs(client_folder, exist_ok=True)

    for folder in subfolders:
        year_folders = ["2022", "2023", "2024"]
        for year in year_folders:
            folder_path = os.path.join(client_folder, folder, year)
            os.makedirs(folder_path, exist_ok=True)
            create_leaf_file(folder_path)

    print(f"Hybrid folder structure created for client: {client_name}")

def create_practice_area_structure(base_path):
    practice_areas = [
        "Family Law",
        "Criminal Defense",
        "Personal Injury",
        "Corporate Law",
        "Intellectual Property"
    ]

    subfolders = [
        "Case Notes",
        "Correspondence",
        "Pleadings",
        "Client Records",
        "Discovery",
        "Depositions",
        "Research"
    ]

    for area in practice_areas:
        area_folder = os.path.join(base_path, area)
        os.makedirs(area_folder, exist_ok=True)

        for folder in subfolders:
            folder_path = os.path.join(area_folder, folder)
            os.makedirs(folder_path, exist_ok=True)
            create_leaf_file(folder_path)

    print("Practice area-based folder structure created")

def create_litigation_process_based_structure(base_path):
    subfolders = [
        "Pleadings",
        "Discovery",
        "Depositions",
        "Motions",
        "Orders",
        "Correspondence",
        "Evidence"
    ]

    for folder in subfolders:
        folder_path = os.path.join(base_path, folder)
        os.makedirs(folder_path, exist_ok=True)
        create_leaf_file(folder_path)

    print("Litigation process-based folder structure created")

def create_model_client_structure(base_path, client_name):
    subfolders = [
        "Motions",
        "Orders",
        "Correspondence",
        "Pleadings",
        "Discovery",
        "Research",
        "Client Documents"
    ]

    client_folder = os.path.join(base_path, client_name)
    os.makedirs(client_folder, exist_ok=True)

    for folder in subfolders:
        folder_path = os.path.join(client_folder, folder)
        os.makedirs(folder_path, exist_ok=True)
        create_leaf_file(folder_path)

    print(f"Model client folder structure created for client: {client_name}")

# Example usages
base_path = "Chronological"
create_chronological_structure(base_path)

base_path = "Client"
client_name = "Client_Name"
create_client_folder_structure(base_path, client_name)

base_path = "Date-Based"
create_date_based_structure(base_path)

base_path = "Document-Based"
create_document_based_structure(base_path)

base_path = "Hybrid"
client_name = "Client_Name"
create_hybrid_structure(base_path, client_name)

base_path = "Practice Area-Based"
create_practice_area_structure(base_path)

base_path = "Litigation Process-Based"
create_litigation_process_based_structure(base_path)

base_path = "Model Client"
client_name = "Model_Client"
create_model_client_structure(base_path, client_name)
