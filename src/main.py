from file_ops.main import read_csv

def main():
    print("---CSV Data Operations Program---")
    csv_filename = input("Enter a csv filename:" )
    csv_data = read_csv(csv_filename)
    print("- csv loaded")
    
if __name__ == "__main__":
    main()
