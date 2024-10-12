import argparse
from csv_reader import read_csv
from csv_writer import write_csv
from csv_processor import process_csv

def main():
    parser = argparse.ArgumentParser(description="CSV Manipulator Program")
    parser.add_argument("input_file", help="Path to the input CSV file")
    parser.add_argument("output_file", help="Path to save the manipulated CSV file")
    args = parser.parse_args()

    data = read_csv(args.input_file)
    processed_data = process_csv(data)
    write_csv(args.output_file, processed_data)

if __name__ == "__main__":
    main()

