import os

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
        os.makedirs(os.path.join(client_folder, folder), exist_ok=True)

    print(f"Model client folder structure created for client: {client_name}")

# Example usage
base_path = "/path/to/your/model_directory"  # Replace with the path where you want to create the folder structure
client_name = "Model_Client"  # Replace with the actual client name
create_model_client_structure(base_path, client_name)
