from typing import List, Callable

def map_column(data, column, func):
    return True

def sum_column(data, old_name, new_name):
    return True

def drop_column(data: List[List[str]], columns_to_drop: List[str]) -> List[List[str]]:
    """
    Removes specified columns from a 2D list representing CSV data, including handling duplicate column names.
    
    Args:
        data: List[List[str]] - A 2D list containing strings (CSV data)
        columns_to_drop: List[str] - A list of column names to remove
        
    Returns:
        List[List[str]] - A 2D list with the specified columns removed
    """

    if not data:
        return data

    # Collect all indices of columns to drop
    indices_to_drop = []
    for column in columns_to_drop:
        indices = [i for i, col_name in enumerate(data[0]) if col_name == column]
        if not indices:
            print(f"Column {column} not found in data")
        else:
            indices_to_drop.extend(indices)

    # Sort indices in reverse order to avoid shifting issues when popping
    indices_to_drop = sorted(set(indices_to_drop), reverse=True)

    # Remove the columns from the header row and each data row
    for index in indices_to_drop:
        data[0].pop(index)
        for row in data[1:]:
            row.pop(index)

    return data

def add_column(data: List[List[str]], column_name: str, func: Callable) -> List[List[str]]:
    """
    Adds a new column to the CSV data using a function to compute column values.
    
    Args:
        data: List[List[str]] - A 2D list containing strings (CSV data)
        column_name: str - The name of the new column to add
        func: callable - A function that takes a row (List[str]) and returns a string value
        
    Returns:
        List[List[str]] - A 2D list with the new column added
        
    Examples:
        >>> data = [["John", "25"], ["Jane", "30"]]
        >>> def get_status(row): return "Adult" if int(row[1]) >= 18 else "Minor"
        >>> add_column(data, "status", get_status)
        [["John", "25", "Adult"], ["Jane", "30", "Adult"]]
        
        >>> def get_name_length(row): return str(len(row[0]))
        >>> add_column(data, "name_length", get_name_length)
        [["John", "25", "4"], ["Jane", "30", "4"]]
    """
    if not data:
        return data
    
    # Add the column name to the header row (first row)
    if data:
        data[0].append(column_name)
    
    # Add computed values to each data row
    for i in range(1, len(data)):
        row = data[i]
        new_value = func(row)
        row.append(str(new_value))
    
    return data

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

