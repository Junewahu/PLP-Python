# Ask the user for the filename
filename = input("Enter the filename: ")

# Try to open and read the file
try:
    with open(filename, 'r') as file:
        content = file.read()
except FileNotFoundError:
    print(f"The file {filename} does not exist.")
    exit()
except IOError:
    print(f"An error occurred while trying to read {filename}.")
    exit()

# Modify the content (convert to uppercase)
modified_content = content.upper()

# Ask the user for the new filename
new_filename = input("Enter the new filename to save the modified content: ")

# Try to write the modified content to the new file
try:
    with open(new_filename, 'w') as new_file:
        new_file.write(modified_content)
    print(f"Modified content has been written to {new_filename}")
except IOError:
    print(f"An error occurred while trying to write to {new_filename}.")