import os

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
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    print("Document-based folder structure created")

# Example usage
base_path = "Document-Based"  # Replace with the path where you want to create the folder structure
create_document_based_structure(base_path)
