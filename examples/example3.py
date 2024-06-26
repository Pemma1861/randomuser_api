import os, sys
from randomuser_api.RandomUserAPI import RandomUserAPI


sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))


'''
    Example of pulling 10000 records with multi-processing and using 1000 results per page
    Saves output to outputs/example3.json

    To run from terminal use:
    python -m examples.example3
'''

def main():

    # Change the output path depending on if the code is being ran through docker
    outpath = os.getenv("DOCKER_OUTPUT_PATH", "./outputs") + "/example3.json"

    rapi = RandomUserAPI()

    rapi.result_count = 10000
    rapi.seed = 'pura'
    rapi.multi = True
    rapi.output_filepath = outpath
    rapi.results_per_page = 1000
    
    rapi.fetch_all_data()


if __name__=='__main__':
    main()
