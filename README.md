Here is the updated README in markdown format:

```markdown
# RandomUserAPI

This project aims to provide a solution for retrieving data from the [RandomUser API](https://randomuser.me).

## Usage

This project can be used either with Docker or as a standalone project.

### Using Docker

1. **Build the image:**
   ```sh
   docker build -t randomuser_api .
   ```

2. **Run the container:**
   ```sh
   docker run -v "$(pwd)/outputs:/home/outputs" randomuser_api:latest
   ```

   **Expected output:** Three files will be created in the `outputs/` directory with the output of the three example files in `examples/`:
   - example1.json
   - example2.json
   - example3.json

### Using the Project

#### Running Examples from the Terminal

To run the examples from the terminal, use the `-m` argument to ensure correct localized imports:
```sh
python -m examples.example1
```

#### Utilizing the API from the Terminal

You can use `main.py` to query the API and save the results in a specified location. The following arguments are allowed:
- `--result_count` (int) default: 100
- `--multi` (bool) default: True
- `--seed` (str) default: 'pura'
- `--output_filepath` (str) default: None
- `--results_per_page` (int) default: 100

**Examples:**
```sh
python main.py --output_filepath='./outputs/custom_output.json'
python main.py --result_count=5000 --output_filepath='./outputs/custom_output.json'
python main.py --result_count=5000 --seed='example' --multi=False --output_filepath='./outputs/custom_output.json'
```

#### Using the API as an Import

1. **Simple usage to pull 100 records saving the results to `./outputs/example1.json` (as seen in example1):**
   ```python
   from randomuser_api.RandomUserAPI import RandomUserAPI

   rapi = RandomUserAPI()
   rapi.output_filepath = './outputs/example1.json'
   rapi.fetch_all_data()
   ```

2. **Usage to retrieve 100 records without multi-processing, saving the results to `./outputs/example2.json` (as seen in example2):**
   ```python
   from randomuser_api.RandomUserAPI import RandomUserAPI

   rapi = RandomUserAPI(
       max_result_count=100,
       seed='pura',
       multi=False,
       output_filepath='./outputs/example2.json'
   )

   rapi.fetch_all_data()
   ```

3. **Example of pulling 10,000 records with multi-processing and using 1,000 results per page, saving the results to `./outputs/example3.json` (as seen in example3):**
   ```python
   from randomuser_api.RandomUserAPI import RandomUserAPI

   rapi = RandomUserAPI(
       max_result_count=10000,
       seed='pura',
       multi=True,
       output_filepath='./outputs/example3.json',
       results_per_page=1000
   )

   rapi.fetch_all_data()
   ```

### Limitations and Known Issues

1. **Limited Capabilities:** There are some limitations to the capabilities of the project restricting what the user can do.

2. **Number of Processes:** The user cannot specify how many processes to spin up while multiprocessing.
   - This is both out of scope and a natural restriction due to the requests per second allowed by the RandomUser API.
   - The API will instead always use the lesser of 10 processes or the number of pages required to pull the `result_count` requested by the user.

3. **Proxies and IP Spoofing:** The user cannot set proxies, nor does the API spoof IPs for faster requests.

4. **Internet Connectivity:** The API does not test for internet connectivity prior to attempting requests.

5. **Selectable Columns:** The user cannot pick which columns to return.
   - This was deemed out of scope.
   - The API will always return these columns: First name, Last name, Gender, Email address, Date of birth, Phone number, Nationality.

6. **Return Type:** The user cannot specify the return type.
   - This was deemed out of scope.
   - The API will always return a JSON object of the response payload if an output filepath is not specified.
