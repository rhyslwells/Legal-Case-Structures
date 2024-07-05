import os

def create_date_based_structure(base_path):
    years = ["2022", "2023", "2024"]  # Example years

    for year in years:
        os.makedirs(os.path.join(base_path, year), exist_ok=True)

    print("Date-based folder structure created")

# Example usage
base_path = "Date-Based"  # Replace with the path where you want to create the folder structure
create_date_based_structure(base_path)
