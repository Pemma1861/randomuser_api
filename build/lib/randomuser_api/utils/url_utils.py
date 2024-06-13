

def build_url(seed: str, results_per_page: int) -> str:
    """
    Method to build the URL for query calls to https://randomuser.me/
    It is possible to make this modular; however,
    currently outside the scope.

    Args:
        seed (str): Seed to be used for data generation.
        results_per_page (int): Number of results per page.

    Returns:
        str: The constructed URL.
    """
    base_url = 'https://randomuser.me/api/?'
    include_cols = 'name,gender,email,dob,phone,nat'
    url = (
        f"{base_url}results={results_per_page}&seed={seed}&inc={include_cols}"
    )
    return url

