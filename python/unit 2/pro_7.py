def copy_file(source, destination):
    try:
        with open(source, "r") as src:
            content = src.read()
        
        with open(destination, "w") as dest:
            dest.write(content)
        
        print(f"File '{source}' copied successfully to '{destination}'")
    
    except FileNotFoundError:
        print("Source file not found. Please check the filename.")

source_file = "source.txt"  # Replace with your source file
destination_file = "copy.txt"  # Replace with your destination file

copy_file(source_file, destination_file)

# Output:
# File 'source.txt' copied successfully to 'copy.txt'