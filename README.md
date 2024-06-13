# RandomUserAPI
===============
This project aims to provide a solution for retrieving data from the https://randomuser.me api


## Usage
--------
Can be used either with docker or as a standalone project.

### Using the docker

1. Build the image
`docker build -t randomuser_api .`

2. Run the container
`docker run -v "$(pwd)/outputs:/home/outputs" randomuser_api:latest`

Expected output:
Three files will be created in `outputs/` with the output of the three example files in `examples/`
- example1.json
- example2.json
- example3.json



### Using the project
---------------------
#### Running examples from the terminal

Running the examples from the terminal requires the `-m` argument to ensure correct localized imports
- `python -m examples.example1`

#### Utilizing the api from the terminal
- It is possible to use main.py to query the api and save the results in a specified location all from the terminal. These are the args allowed:
    - `--result_count` (int) default: 100
    - `--multi` (bool) default: True
    - `--seed` (str) default: 'pura'
    - `--output_filepath` default: None
    - `--results_per_page`default: 100

- Examples of utlizing the api from the terminal
    - `python main.py --output_filepath='./outputs/custom_output.json'`
    - `python main.py --result_count=5000 --output_filepath='./outputs/custom_output.json'`
    - `python main.py --result_count=5000 --seed='example' --multi=False  --output_filepath='./outputs/custom_output.json'`

#### Using the api as an import
Simple usage to pull 100 records as seen in example1
```
from randomuser_api.RandomUserAPI import RandomUserAPI

rapi = RandomUserAPI()
rapi.output_filepath = './outputs/example1.json'
rapi.fetch_all_data(100)
```

Usage to retrieve 100 records without multi-processing saving the results to `outputs/example2.json` as seen in example2
```
from randomuser_api.RandomUserAPI import RandomUserAPI

rapi = RandomUserAPI(
                    result_count=100,
                    seed='pura',
                    multi=False,
                    output_filepath='./outputs/example2.json'
                )

rapi.fetch_all_data()
```

Example of pulling 10000 records with multi-processing and using 1000 results per page saving the results to `outputs/example3.json` as seen in example3
```
from randomuser_api.RandomUserAPI import RandomUserAPI

rapi = RandomUserAPI()

rapi.result_count = 10000
rapi.seed = 'pura'
rapi.multi = True
rapi.output_filepath = './outputs/example3.json'
rapi.results_per_page = 1000

rapi.fetch_all_data()
```


### Limitations and known issues
--------
1. There are some limitations to the capabilities of the project restricting what the user is able to do.


2. The user cannot specify how many processes to spin up while multiprocessing.
   - Both out of scope and a natural restriction to requests per second allowed by https://randomuser.me/
   - The api will instead always use the lesser of 10 processes, or the number of pages required to pull the record_count requested by the user

3. The user cannot set proxies, nor does the api spoof IPs for faster requests.
4. The api does not test for internet connectivity prior to attempting request.

5. The user cannot pick which columns to return.
   - Deemed out of scope
   - The api will instead always return these columns:
      - First name, Last name, Gender, Email address, Date of birth, Phone number, Nationality

6. Cannot specify return type.
   - Deemed out of scope
   - The api will always return a JSON object of the response payload if an output filepath is not specified.



