import os
import yaml
def get_save_file_path(filename):
    # Get the absolute path of the current file (file_handler.py)
    current_dir = os.path.dirname(os.path.abspath(__file__))

    # Go up one directory to the project root
    project_root = os.path.dirname(current_dir)

    # Construct the full path to the saves directory
    saves_dir = os.path.join(project_root, 'saves')

    # Ensure the saves directory exists
    if not os.path.exists(saves_dir):
        os.makedirs(saves_dir)

    # Construct the full path to the file to open
    return os.path.join(saves_dir, filename)

def open_save_file(filename):
    file_path = get_save_file_path(filename)
    content = None
    with open(file_path, 'r') as file:
        content = yaml.safe_load(file)
    return content

def write_save_file(filename, content):
    file_path = get_save_file_path(filename)
    
    with open(file_path, 'w') as file:
        file.write(content)
        print(f"Content written to {filename}.")



