import argparse
from randomuser_api.RandomUserAPI import RandomUserAPI

# main allows the user to utilize the api from the terminal by passing args directly.
# For example:
# python main.py --result_count=5000 --seed='example' --multi=True  --output_filepath='outputs/custom_output.json'


def main():
    parser = argparse.ArgumentParser(description="RandomUserAPI Data Fetcher")

    parser.add_argument('--result_count', type=int, default=100, help="Number of results (default: 100)")
    parser.add_argument('--multi', type=bool, default=True, help="Use multi-processing (default: True)")
    parser.add_argument('--seed', type=str, default='pura', help="Seed for data generation (default: 'pura')")
    parser.add_argument('--output_filepath', type=str, default=None, help="Filepath to save output (default: None)")
    parser.add_argument('--results_per_page', type=int, default=100, help="Number of results per page (default: 100)")

    args = parser.parse_args()

    rapi = RandomUserAPI()
    rapi.result_count=args.result_count
    rapi.seed=args.seed
    rapi.multi=args.multi
    rapi.output_filepath=args.output_filepath
    rapi.output_filepath=args.output_filepath
    rapi.results_per_page=args.results_per_page


    _ = rapi.fetch_all_data()


if __name__ == '__main__':
    main()