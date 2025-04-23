from file_ops.main import read_csv, write_csv

def main():
    data = read_csv("input.csv")
    print(data)
if __name__ == "__main__":
    main()

