import os


def create_directory_for_file(filepath):
    """
    Method to create the directory for the given file path if it doesn't already exist.

    Args:
        filepath (str): Filepath to check and create directory for.
    """
    directory = os.path.dirname(filepath)

    if not os.path.exists(directory):
        os.makedirs(directory)
        print(f"Directory '{directory}' created.")
    else:
        return

