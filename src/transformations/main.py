from typing import List, Callable, Any
import copy


def map_column(data, column, func):
    return True

def sum_column(data, old_name, new_name):
    return True

def drop_column(data: List[List[str]], columns_to_drop: List[str]) -> List[List[str]]:
    """
    Removes specified columns from a 2D list representing CSV data.
    
    Args:
        data: List[List[str]] - A 2D list containing strings (CSV data)
        columns_to_drop: List[str] - A list of column names to remove
        
    Returns:
        List[List[str]] - A 2D list with the specified columns removed
        
    Edge Cases:
        - Empty data or no headers: Returns original data
        - Non-existent columns: Silently skipped
        - Duplicate columns: All instances removed
    """
    if not data or not data[0]:
        return data
    
    new_data = copy.deepcopy(data)  # Preserve original data
    headers = new_data[0]
    
    # Find indices to keep (handles duplicates automatically)
    indices_to_keep = [i for i, header in enumerate(headers) if header not in columns_to_drop]
    
    # Update headers
    new_data[0] = [headers[i] for i in indices_to_keep]
    
    # Update each data row, handling varying row lengths
    for i in range(1, len(new_data)):
        new_data[i] = [new_data[i][j] for j in indices_to_keep if j < len(new_data[i])]
    
    return new_data

def add_column(data: List[List[str]], column_name: str, func: Callable[[List[str]], Any]) -> List[List[str]]:
    """
    Adds a new column to the CSV data using a function to compute column values.
    
    Args:
        data: List[List[str]] - A 2D list containing strings (CSV data)
        column_name: str - The name of the new column to add
        func: Callable[[List[str]], Any] - A function that takes a row and returns a value
        
    Returns:
        List[List[str]] - A 2D list with the new column added
        
    Raises:
        ValueError: If the column_name already exists in the headers
    """
    if not data:
        return data  # Return original empty data, not empty list
    
    new_data = copy.deepcopy(data)  # Preserve original data
    headers = new_data[0]
    
    if column_name in headers:
        raise ValueError(f"Column '{column_name}' already exists")
    
    # Add the column name to the header row
    headers.append(column_name)
    
    # Add computed values to each data row
    for i in range(1, len(new_data)):
        row = new_data[i]
        try:
            new_value = func(row)
            row.append(str(new_value))
        except Exception:
            row.append("")  # Default on error
    
    return new_data

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
    def clean_numeric_string(s: str) -> str:
        s = s.strip()
        negative = False

        if s.startswith('-$') or s.startswith('$-'):
            negative = True
            s = s.replace('-', '').replace('$', '')
        elif s.startswith('$'):
            s = s[1:]
        elif s.startswith('-'):
            negative = True
            s = s[1:]

        s = s.replace(',', '')

        if negative:
            s = '-' + s

        return s

    def is_numeric_string(s: str) -> bool:
        try:
            float(clean_numeric_string(s))
            return True
        except ValueError:
            return False

    normalized_data = []
    for row in data:
        normalized_row = []
        for value in row:
            cleaned = clean_numeric_string(value)
            if is_numeric_string(value):
                normalized_row.append("{:.2f}".format(float(cleaned)))
            else:
                normalized_row.append(value)
        normalized_data.append(normalized_row)

    return normalized_data

