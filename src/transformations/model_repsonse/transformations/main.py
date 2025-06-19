from typing import List
def map_column(data, column, func):
    return True

def sum_column(data, old_name, new_name):
    return True

def drop_column(data, columns_to_drop):
    return True

def add_column(data, column_name, func):
    return True

def normalize_numeric_strings(data: List[List[str]]) -> List[List[str]]:
    """
    Normalizes numerical strings in a 2D list to a format with max 2 decimal places.
    
    Args:
        data: List[List[str]] - A 2D list containing strings
        
    Returns:
        List[List[str]] - A 2D list with normalized numerical strings
        
    Examples:
        >>> normalize_numeric_strings([["1.234", "hello", "5"], ["3.4567", "world", "2.1"]])
        [["1.23", "hello", "5.00"], ["3.46", "world", "2.10"]]
    """
    def is_numeric_string(s: str) -> bool:
        try:
            float(s)
            return True
        except ValueError:
            return False
    
    # Create a new list to store the normalized data
    normalized_data = []
    
    for row in data:
        normalized_row = []
        for value in row:
            if is_numeric_string(value):
                # Convert to float and format with 2 decimal places
                normalized_value = "{:.2f}".format(float(value))
                normalized_row.append(normalized_value)
            else:
                # Keep non-numeric values as they are
                normalized_row.append(value)
        normalized_data.append(normalized_row)
    
    return normalized_data

# Test cases
if __name__ == "__main__":
    # Test case 1: Mixed numeric and non-numeric strings
    test1 = [["1.234", "hello", "5"], ["3.4567", "world", "2.1"]]
    print(normalize_numeric_strings(test1))
    # Expected: [["1.23", "hello", "5.00"], ["3.46", "world", "2.10"]]

    # Test case 2: Various numeric formats
    test2 = [["123.45678", "1", "0.1"], ["2.999", "10.5", "0"]]
    print(normalize_numeric_strings(test2))
    # Expected: [["123.46", "1.00", "0.10"], ["3.00", "10.50", "0.00"]]

    # Test case 3: Only non-numeric
    test3 = [["hello", "world"], ["test", "data"]]
    print(normalize_numeric_strings(test3))
    # Expected: [["hello", "world"], ["test", "data"]]