import os

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
            os.makedirs(os.path.join(area_folder, folder), exist_ok=True)

    print("Practice area-based folder structure created")

# Example usage
base_path = "/path/to/your/practice_area_directory"  # Replace with the path where you want to create the folder structure
create_practice_area_structure(base_path)
