import ast
import os
from pathlib import Path

# Runs through all the files in the project and find classes that inherit from Pet clas
# Then these values are used for user menu render

#print("Current working dir: ", os.getcwd())
#print("Script dir:", Path(__file__).resolve().parent)

script_dir = Path(__file__).resolve().parent

def find_inherited_classes(base_class = "Pet", path = script_dir):
    inherited_classes = []
    # Go through file structure. Get files for each dir
    for root, _, files in os.walk(path):
        #print(f"root: {root}, line: {_}, files: {files}")
        for file in files:
            if file.endswith(".py"):
                file_path = os.path.join(root, file)
                with open(file_path, "r", encoding="utf-8") as f:
                    # what is it
                    tree = ast.parse(f.read(), filename=file_path)
                    for node in ast.walk(tree):
                        if isinstance(node, ast.ClassDef):
                            for base in node.bases:
                                if isinstance(base, ast.Name) and base.id == base_class:
                                    # Add as tuple?
                                    inherited_classes.append((node.name, file_path))
    return inherited_classes

# def clear_screen():
#     os.system('cls' if os.name == 'nt' else 'clear')
#
# clear_screen()
# classes = find_inherited_classes()
# for path, class_name in classes:
#     print(f"Path: {path} : {class_name}")