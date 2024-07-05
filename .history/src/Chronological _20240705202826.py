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
            os.makedirs(os.path.join(year_folder, folder), exist_ok=True)

    print("Chronological folder structure created")

# Example usage
base_path = "/path/to/your/chronological_directory"  # Replace with the path where you want to create the folder structure
create_chronological_structure(base_path)
