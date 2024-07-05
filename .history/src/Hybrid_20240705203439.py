import os

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
            os.makedirs(os.path.join(client_folder, folder, year), exist_ok=True)

    print(f"Hybrid folder structure created for client: {client_name}")

# Example usage
base_path = "/path/to/your/hybrid_directory"  # Replace with the path where you want to create the folder structure
client_name = "Client_Name"  # Replace with the actual client name
create_hybrid_structure(base_path, client_name)
