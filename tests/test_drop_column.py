import unittest
from src.transformations.main import drop_column

class TestDropColumn(unittest.TestCase):

    def test_drop_single_column(self):
        """Test dropping a single column"""
        data = [["name", "age", "city"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        result = drop_column(data, ["age"])
        expected = [["name", "city"], ["John", "NYC"], ["Jane", "LA"]]
        self.assertEqual(result, expected)

    def test_drop_multiple_columns(self):
        """Test dropping multiple columns"""
        data = [["name", "age", "city", "country"], ["John", "25", "NYC", "USA"], ["Jane", "30", "LA", "USA"]]
        result = drop_column(data, ["age", "country"])
        expected = [["name", "city"], ["John", "NYC"], ["Jane", "LA"]]
        self.assertEqual(result, expected)

    def test_drop_first_column(self):
        """Test dropping the first column"""
        data = [["name", "age", "city"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        result = drop_column(data, ["name"])
        expected = [["age", "city"], ["25", "NYC"], ["30", "LA"]]
        self.assertEqual(result, expected)

    def test_drop_last_column(self):
        """Test dropping the last column"""
        data = [["name", "age", "city"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        result = drop_column(data, ["city"])
        expected = [["name", "age"], ["John", "25"], ["Jane", "30"]]
        self.assertEqual(result, expected)

    def test_drop_duplicate_columns(self):
        """Test dropping duplicate column names"""
        data = [["name", "age", "name", "city"], ["John", "25", "John", "NYC"], ["Jane", "30", "Jane", "LA"]]
        result = drop_column(data, ["name"])
        expected = [["age", "city"], ["25", "NYC"], ["30", "LA"]]
        self.assertEqual(result, expected)

    def test_drop_nonexistent_column(self):
        """Test dropping a column that doesn't exist"""
        data = [["name", "age", "city"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        result = drop_column(data, ["nonexistent"])
        expected = [["name", "age", "city"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        self.assertEqual(result, expected)

    def test_drop_mixed_existent_nonexistent_columns(self):
        """Test dropping a mix of existing and non-existing columns"""
        data = [["name", "age", "city"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        result = drop_column(data, ["age", "nonexistent", "city"])
        expected = [["name"], ["John"], ["Jane"]]
        self.assertEqual(result, expected)

    def test_empty_data(self):
        """Test with empty data"""
        data = []
        result = drop_column(data, ["name"])
        self.assertEqual(result, [])

    def test_header_only(self):
        """Test with only header row"""
        data = [["name", "age", "city"]]
        result = drop_column(data, ["age"])
        expected = [["name", "city"]]
        self.assertEqual(result, expected)

    def test_single_data_row(self):
        """Test with single data row"""
        data = [["name", "age", "city"], ["John", "25", "NYC"]]
        result = drop_column(data, ["age"])
        expected = [["name", "city"], ["John", "NYC"]]
        self.assertEqual(result, expected)

    def test_drop_all_columns(self):
        """Test dropping all columns"""
        data = [["name", "age", "city"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        result = drop_column(data, ["name", "age", "city"])
        expected = [[], [], []]
        self.assertEqual(result, expected)

    def test_drop_empty_column_list(self):
        """Test dropping no columns"""
        data = [["name", "age", "city"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        result = drop_column(data, [])
        expected = [["name", "age", "city"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        self.assertEqual(result, expected)

    def test_case_sensitive_column_names(self):
        """Test that column names are case sensitive"""
        data = [["Name", "Age", "City"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        result = drop_column(data, ["name"])  # lowercase
        expected = [["Name", "Age", "City"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        self.assertEqual(result, expected)

    def test_drop_columns_with_special_characters(self):
        """Test dropping columns with special characters in names"""
        data = [["first_name", "last-name", "email@domain"], ["John", "Doe", "john@example.com"]]
        result = drop_column(data, ["last-name", "email@domain"])
        expected = [["first_name"], ["John"]]
        self.assertEqual(result, expected)

    def test_drop_columns_with_spaces(self):
        """Test dropping columns with spaces in names"""
        data = [["first name", "last name", "email"], ["John", "Doe", "john@example.com"]]
        result = drop_column(data, ["first name"])
        expected = [["last name", "email"], ["Doe", "john@example.com"]]
        self.assertEqual(result, expected)

    def test_preserve_data_integrity(self):
        """Test that data integrity is preserved when dropping columns"""
        data = [["id", "name", "age", "city"], ["1", "John", "25", "NYC"], ["2", "Jane", "30", "LA"]]
        result = drop_column(data, ["age"])
        expected = [["id", "name", "city"], ["1", "John", "NYC"], ["2", "Jane", "LA"]]
        self.assertEqual(result, expected)
        
        # Verify that the original data structure is maintained
        self.assertEqual(len(result), 3)  # header + 2 data rows
        self.assertEqual(len(result[0]), 3)  # 3 columns in header
        self.assertEqual(len(result[1]), 3)  # 3 columns in first data row
        self.assertEqual(len(result[2]), 3)  # 3 columns in second data row

if __name__ == "__main__":
    unittest.main() 