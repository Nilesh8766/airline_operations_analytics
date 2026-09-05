from pathlib import Path
import zipfile
import numpy as np
import pandas as pd

from pathlib import Path


def get_project_path():         #to see project path

    PROJECT_PATH = Path.cwd().parent
    print("Project Path", PROJECT_PATH.resolve())
    return PROJECT_PATH

def create_project_folders(PROJECT_PATH):       #create project folders

    RAW_PATH = PROJECT_PATH / "01_Raw_Data"
    RAW_PATH.mkdir(parents=True, exist_ok=True)
    print("Raw_Path", RAW_PATH.resolve())
    DOCUMENTATION_PATH = PROJECT_PATH / "02_Documentation"
    DOCUMENTATION_PATH.mkdir(parents=True, exist_ok=True)
    print("Documentation_Path", DOCUMENTATION_PATH.resolve())
    return RAW_PATH, DOCUMENTATION_PATH

def create_year_folders(RAW_PATH):      #create years folder in raw data

    RAW_2024_PATH = RAW_PATH / "2024"
    RAW_2024_PATH.mkdir(parents=True, exist_ok=True)
    print("Raw_2024_Path", RAW_2024_PATH.resolve())
    RAW_2025_PATH = RAW_PATH / "2025"
    RAW_2025_PATH.mkdir(parents=True, exist_ok=True)
    print("Raw_2025_Path", RAW_2025_PATH.resolve())
    return RAW_2024_PATH, RAW_2025_PATH

def inspect_zip_files(RAW_2024_PATH):       #returns total zipfile in folder with size

    zip_files = list(RAW_2024_PATH.glob("*.zip"))
    total_zip_file = len(zip_files)
    print(f"Total Zip File: {total_zip_file}")
    for file in zip_files:
        print("File Name:", file.name)
        print(
            "File Size: ",
            round(file.stat().st_size / (1024 * 1024), 2),
            "MB"
        )
        print("File Location", file.resolve())
    return zip_files

def inspect_zip_contents(zip_files, zip_index=0):       #give files inside of zip

    zip_file = zip_files[zip_index]
    with zipfile.ZipFile(zip_file, "r") as z:
        files_inside_zip = z.namelist()
        for file in files_inside_zip:
            print(file)
    return zip_file, files_inside_zip

def create_extract_folder(RAW_2024_PATH, month):        #create folder of month name

    EXTRACT_PATH = RAW_2024_PATH / month
    EXTRACT_PATH.mkdir(parents=True, exist_ok=True)
    print("Extract_Path", EXTRACT_PATH.resolve())
    return EXTRACT_PATH

def extract_zip_file(zip_file, EXTRACT_PATH):       #read and extract files from selected zipfile

    with zipfile.ZipFile(zip_file, "r") as z:
        z.extractall(EXTRACT_PATH)

def find_csv_files(EXTRACT_PATH):       #to get csv file in extract month folder

    csv_files = list(EXTRACT_PATH.rglob("*.csv"))
    for files in csv_files:
        print(files)
    return csv_files

def load_csv_file(csv_files):

    csv_file = csv_files[0]

    df = pd.read_csv(
        csv_file,
        low_memory=False
    )
    return df