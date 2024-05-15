# Write a script that searches a folder you specify (as well as its subfolders, up
# to two levels deep) and compiles a list of all `.jpg` files contained in there.
# The list should include the complete path of each `.jpg` file.
# 
# You should train:
# 
# - Using `for` loops
# - Using conditional statements
# - Working with `pathlib`
# - Thinking about nested loops
# 
# If you are feeling bold, create a list containing each type of file extension
# you find in the folder.
# Start with a small folder to make it easy to check whether your program is
# working correctly. Then search a bigger folder.
# This program should work for any specified folder on your computer.
from pathlib import Path

desktop = Path('C:/Users/Blake/Desktop')

from pathlib import Path

def search_jpg_files(directory):
    base_path = Path(directory)
    jpg_files = []
    all_extensions = set()

    # Loop through the base directory and up to two levels of subdirectories
    for path in base_path.rglob('*.*'):  # This will get all files regardless of how deep they are
        # Check if the file is two levels deep or less
        if len(Path(path).parts) <= len(base_path.parts) + 3:
            all_extensions.add(path.suffix)  # Add file extension to the set

            # Check if the file has a .jpg extension
            if path.suffix.lower() == '.jpg':
                jpg_files.append(str(path))

    return jpg_files, all_extensions

# Specify the directory to search
directory = input("Enter the directory path to search: ")

# Run the function
jpg_files, extensions = search_jpg_files(directory)

# Output the results
print("Found .jpg files:")
for file in jpg_files:
    print(file)

print("\nAll file extensions found:")
for ext in extensions:
    print(ext)