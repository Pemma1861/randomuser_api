from concurrent import futures
import json
import re
import time
from urllib.error import HTTPError, URLError
import urllib.request
import warnings


from .utils.checks import check_type, check_positive, check_valid_filepath
from .utils.data_processing import process_user
from .utils.page_count import get_page_count
from .utils.save_file import save_json
from .utils.url_utils import build_url


class RandomUserAPI:
    """
    Helper class to facilitate a modular approach to using the RandomUser API.

    Attributes:
        result_count (int): Number of results desired.
            Defaults to 1000.
        seed (str): Seed to be used for data generation. Defaults to 'pura'.
        multi (bool): Whether multi-processing should be used. Defaults to True.
        output_filepath (str): Filepath to save output if desired.
            A value of None will not attempt to save outputs. Defaults to None.
            Providing a value save the results to a file instead of returning them.
    """

    def __init__(
        self, result_count: int=1000, seed: str='pura', multi: bool=True, output_filepath: str=None
    ):

        # Type checks for initialization
        check_type('result_count', result_count, int)
        check_positive('result_count', result_count)
        check_type('seed', seed, str)
        check_type('multi', multi, bool)
        if output_filepath is not None:
            check_type('output_filepath', output_filepath, str)
            check_valid_filepath(output_filepath)

        # Set attributes if all types are correct
        self.multi = multi
        self.seed = seed
        self.result_count = result_count
        self.output_filepath = output_filepath

        # Setting results per page
        results_per_page=100
        self.results_per_page = results_per_page

        # Generate initial URL
        self._url = build_url(self.seed, self.results_per_page)


    def fetch_data(self, page: int=1) -> json:
        """
        Method to pull data and return the response in JSON format.
            Will not save the data to a file.
            If an invalid page number is supplied, the server-side API will default to page 1.

        Args:
            page (int): Page number of results. Defaults to 1.

        Returns:
            JSON object containing results.
        """
        url = self.url + f'&page={page}'

        while True:
            try:
                response = urllib.request.urlopen(url)
                if response.getcode() == 200:
                    return json.loads(response.read())
            except HTTPError as e:
                if e.code == 429:
                    retry_after = int(e.headers.get('Retry-After', 1))
                    print(
                        f'HTTP 429: Rate limit exceeded. Retrying after {retry_after} seconds...'
                    )
                    time.sleep(retry_after)
                else:
                    raise e
            except URLError as e:
                print(f'Failed to fetch data due to network error: {e.reason}')
                raise e


    def fetch_all_data(self, result_count: int=None):
        """
        Method to fetch all data using either multi-processing or single-processing
        based on the 'multi' attribute. Processes each user through process_user.
        Saves file to output_filepath if attribute is not None.
        
        Args:
            result_count (int): Optional result count desired. Defaults to None.
                A value of None will instead use self.result_count
        Returns:
            JSON object containing results if output_filepath is not set. Otherwise None.
        """

        if result_count:
            check_type('result_count', result_count, int)
            check_positive('result_count', result_count)

        if not result_count:
            result_count = self.result_count 

        page_count = get_page_count(result_count, self.results_per_page)
        page_numbers = list(range(1, page_count + 1))
        processes = min(page_count, 10)  # Restrict process count to page numbers if less than 10

        if self.multi:
            with futures.ThreadPoolExecutor(processes) as executor:
                results = executor.map(self.fetch_and_process_page, page_numbers)
        else:
            results = [self.fetch_and_process_page(page) for page in page_numbers]

        # Flatten the list of lists
        all_users = [user for result in results for user in result]

        # Limit the number of records to result_count
        if len(all_users) > result_count:
            all_users = all_users[:result_count]

        # Save to file if output_filepath is provided otherwise return payload
        if self.output_filepath:
            save_json(all_users, self.output_filepath)
            return
        else:
            return all_users


    def fetch_and_process_page(self, page: int):
        """
        Method to fetch and process data for a single page.

        Args:
            page (int): Page number of results.

        Returns:
            list: List of processed user data for the page.
        """
        result = self.fetch_data(page)
        return [process_user(user) for user in result['results']]


    @property
    def result_count(self):
        return self._result_count

    @property
    def multi(self):
        return self._multi

    @property
    def results_per_page(self):
        return self._results_per_page

    @property
    def seed(self):
        return self._seed

    @property
    def output_filepath(self):
        return self._output_filepath

    @property
    def url(self):
        return self._url


    @result_count.setter
    def result_count(self, value):
        check_type('result_count', value, int)
        check_positive('result_count', value)
        self._result_count = value


    @multi.setter
    def multi(self, value):
        check_type('multi', value, bool)
        self._multi = value


    @results_per_page.setter
    def results_per_page(self, value):
        check_type('results_per_page', value, int)
        check_positive('results_per_page', value)
        self._results_per_page = value
        self._url = build_url(self.seed, self.results_per_page)


    @seed.setter
    def seed(self, value):
        check_type('seed', value, str)

        # Check for non-alphanumeric characters to prevent code injection
        if re.search(r'\W', value):
            # Remove non-alphanumeric characters
            new_value = re.sub(r'\W', '', value)
            warnings.warn(
                f'Non-alphanumeric characters found in seed. Modified "{value}" to "{new_value}".'
            )
            value = new_value

        self._seed = value


    @output_filepath.setter
    def output_filepath(self, value):
        if value is not None:
            check_type('output_filepath', value, str)
            check_valid_filepath(value)
        self._output_filepath = value


    @url.setter
    def url(self, value):
        warnings.warn('URL modification is not allowed. Reverting to generated URL.')
        self._url = build_url(self.seed, self.results_per_page)

