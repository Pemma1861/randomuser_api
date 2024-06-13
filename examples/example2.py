import os, sys
from randomuser_api.RandomUserAPI import RandomUserAPI


sys.path.append(os.path.join(os.path.dirname(__file__), "lib"))



'''
    Example of pulling 100 records without multi-processing
    Saves output to outputs/example2.json

    To run from terminal use:
    python -m examples.example2
'''

def main():
    rapi = RandomUserAPI(
                        result_count=100,
                        seed='pura',
                        multi=False,
                        output_filepath='/home/outputs/example2.json'
                    )

    rapi.fetch_all_data()


if __name__=='__main__':
    main()
