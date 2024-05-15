# Import pathlib
# Find the path to my Desktop
# List all the files on there
# Filter for screenshots only
# Create a new folder
# Move the screenshots in there
import pathlib

path = pathlib.Path.cwd()

for filepath in path.iterdir():
    print(filepath.name)
    
desktop_path = pathlib.Path("C:/Users/Blake/Desktop")


 
new_path = pathlib.Path('C:/Users/Blake/Pictures/Screenshots')
new_path.mkdir(exist_ok=True) 

for filepath in desktop_path.iterdir():
    if filepath.suffix == '.png':
        new_filepath = new_path.joinpath(filepath.name)
        filepath.replace(new_filepath)
    
