import pandas as pd

def read_csv(file_path):
    """
    Read CSV file using pandas and return data as a list of lists.
    
    Args:
        file_path (str): Path to the input CSV file
        
    Returns:
        list: List of lists containing CSV data
    """
    df = pd.read_csv(file_path)
    data = df.values.tolist()
    return data

def write_csv(file_path, data):
    """
    Write data to CSV file using pandas.
    
    Args:
        file_path (str): Path to save the CSV file
        data (list): List of lists containing data to write
    """
    df = pd.DataFrame(data)
    df.to_csv(file_path, index=False)
