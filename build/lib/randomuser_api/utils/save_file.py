from .create_dir import create_directory_for_file
import json


def save_json(payload: json, filepath: str):
    """
    Method to save the file to a json file.
    
    Args:
        payload (json): json object to be saved to the filepath.
        filepath (str): Filepath to save the json object.
    """
    create_directory_for_file(filepath)
    with open(filepath, 'w') as file:
        json.dump(payload, file, indent=4)
    print(f'Data saved to {filepath}')
