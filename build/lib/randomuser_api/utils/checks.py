import os


def check_positive(name, value):
    """
    Checks if a value is positive.

    Args:
        name (str): The name of the variable.
        value (int or float): The value to check.

    Raises:
        ValueError: If the value is not positive.
    """
    if value <= 0:
        raise ValueError(f'Expected "{name}" to be greater than 0, but got {value}')


def check_type(name, value, expected_type):
    """
    Checks if a value is of a specified type.

    Args:
        name (str): The name of the variable.
        value: The value to check.
        expected_type: The expected type of the value.

    Raises:
        TypeError: If the value is not of the expected type.
    """
    if not isinstance(value, expected_type):
        raise TypeError(
            f'Expected "{name}" to be of type {expected_type.__name__}, but got {type(value).__name__}'
        )


def check_valid_filepath(filepath):
    """
    Checks if a filepath is valid.

    Args:
        filepath (str): The filepath to check.

    Raises:
        ValueError: If the filepath is not valid.
    """
    if not os.path.basename(filepath):
        raise ValueError(
            f'Invalid file path: "{filepath}" does not contain a file name.'
        )

