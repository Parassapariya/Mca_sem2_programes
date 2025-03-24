def process_numbers_file(filename):
    try:
        with open(filename, "r") as file:
            numbers = [int(line.strip()) for line in file if line.strip().isdigit()]
            
            if not numbers:
                print("The file is empty or contains no valid numbers.")
                return
            
            total = sum(numbers)
            max_num = max(numbers)
            min_num = min(numbers)
            
            print("Total Sum:", total)
            print("Maximum Number:", max_num)
            print("Minimum Number:", min_num)
    
    except FileNotFoundError:
        print("File not found. Please check the filename.")
    except ValueError:
        print("File contains invalid data. Ensure it has only numbers.")

filename = "numbers.txt"  # Replace with your file name
process_numbers_file(filename)


# Output:
# Total Sum: 15
# Maximum Number: 5
# Minimum Number: 1