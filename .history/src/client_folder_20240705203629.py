import os

def create_client_folder_structure(base_path, client_name):
    # Define the subfolders to be created
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

    # Create the main client folder
    client_folder = os.path.join(base_path, client_name)
    os.makedirs(client_folder, exist_ok=True)

    # Create the subfolders within the client folder
    for folder in subfolders:
        os.makedirs(os.path.join(client_folder, folder), exist_ok=True)

    print(f"Folder structure created for client: {client_name}")

# Example usage
base_path = "Client_Name"  # Replace with the path where you want to create the folder structure
client_name = "Client_Name"  # Replace with the actual client name
create_client_folder_structure(base_path, client_name)
