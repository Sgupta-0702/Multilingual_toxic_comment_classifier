import zipfile
import os

# Define the path to the zip file and the directory to extract its contents to
zip_file_path = 'C:\\Users\\saanc\\Desktop\\git\\new\\jigsaw-multilingual-toxic-comment-classification.zip'  # Replace 'your-zip-file.zip' with your zip file name
extract_to_path = 'C:\\Users\\saanc\\Desktop\\git\\new\\extracted_files'

# Create the directory if it doesn't exist
os.makedirs(extract_to_path, exist_ok=True)

# Open the zip file and extract all contents
with zipfile.ZipFile(zip_file_path, 'r') as zip_ref:
    zip_ref.extractall(extract_to_path)

print(f"Extracted all files to {extract_to_path}")
