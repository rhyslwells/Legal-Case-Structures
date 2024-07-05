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
        os.makedirs(os.path.join(base_path, folder), exist_ok=True)

    print("Litigation process-based folder structure created")

# Example usage
base_path = "/path/to/your/litigation_directory"  # Replace with the path where you want to create the folder structure
create_litigation_process_based_structure(base_path)
