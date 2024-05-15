# Write a script that walks through a nested folder structure 
# and prints out all the Python files it can find.
# Run it in your labs folder and add formatting for nicer viewing.
from pathlib import Path

desktop = Path('C:/Users/Blake/Desktop')

for filepath in desktop.iterdir():
    if filepath.suffix == '.py':
        print(filepath.name)
    