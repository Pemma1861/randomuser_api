import os, sys
from randomuser_api.RandomUserAPI import RandomUserAPI


sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))

'''
    Example of pulling 100 records with simple usage
    response returns the results as json

    To run from terminal use:
    python -m examples.example1
'''

def main():
    
    # Change the output path depending on if the code is being ran through docker
    outpath = os.getenv("DOCKER_OUTPUT_PATH", "./outputs") + "/example1.json"

    rapi = RandomUserAPI()

    rapi.output_filepath = outpath
    rapi.fetch_all_data(100)

if __name__=='__main__':
    main()
