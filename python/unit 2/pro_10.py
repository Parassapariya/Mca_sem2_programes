import zipfile

# Function to zip files
def zip_files(zip_name, files):
    with zipfile.ZipFile(zip_name, "w") as zipf:
        for file in files:
            zipf.write(file)
    print(f"Files {files} zipped successfully into {zip_name}")

# Function to unzip files
def unzip_files(zip_name, extract_to):
    with zipfile.ZipFile(zip_name, "r") as zipf:
        zipf.extractall(extract_to)
    print(f"Files extracted successfully to {extract_to}")

# Example usage
files_to_zip = ["marks.txt", "sample.txt"]  # Replace with your files
zip_filename = "my_archive.zip"
extract_folder = "extracted_files"

# Zip files
zip_files(zip_filename, files_to_zip)

# Unzip files
unzip_files(zip_filename, extract_folder)

# Output:
# Files ['marks.txt', 'sample.txt'] zipped successfully into my_archive.zip
# Files extracted successfully to extracted_files
