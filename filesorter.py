import os
import shutil
from datetime import datetime

# Function to get the creation or modification date of a file
def get_file_date(file_path):
    stat = os.stat(file_path)
    return datetime.fromtimestamp(stat.st_mtime)

# Function to create a folder if it doesn't exist
def create_folder(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)

# Function to sort files into folders by month and year
def sort_files_by_date(source_folder):
    for root, _, files in os.walk(source_folder):
        for file in files:
            file_path = os.path.join(root, file)
            file_date = get_file_date(file_path)
            year = file_date.year
            month = file_date.strftime('%B')
            destination_folder = os.path.join(source_folder, str(year), month)
            create_folder(destination_folder)
            destination_path = os.path.join(destination_folder, file)
            shutil.move(file_path, destination_path)

if __name__ == "__main__":
    source_folder = "path_to_your_source_folder"
    sort_files_by_date(source_folder)
