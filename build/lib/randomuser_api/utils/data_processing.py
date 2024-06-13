
def process_user(user):
    """
    Function to process a single user data from https://randomuser.me/ API response.

    Args:
        user (dict): A dictionary containing user information.

    Returns:
        dict: A dictionary containing processed user information.
    """
    return {
        'First name': user['name']['first'],
        'Last name': user['name']['last'],
        'Gender': user['gender'],
        'Email address': user['email'],
        'Date of birth': user['dob']['date'],
        'Phone number': user['phone'],
        'Nationality': user['nat']
    }
