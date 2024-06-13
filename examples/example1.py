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
    rapi = RandomUserAPI()
    rapi.output_filepath = '/home/outputs/example1.json'
    rapi.fetch_all_data(100)

if __name__=='__main__':
    main()
