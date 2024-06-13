import math

def get_page_count(result_count: int, results_per_page: int = 100) -> int:
    """
    Method to calculate the number of pages needed for the
    requested result count

    Args:
        result_count (int): number of total results requested.
        results_per_page (int): Number of results per page. (Default: 100)
    Returns:
        int: the number of pages needed.
    """

    return int(math.ceil(result_count / results_per_page))

