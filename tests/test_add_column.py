import unittest
from src.transformations.main import add_column

class TestAddColumn(unittest.TestCase):

    def test_add_simple_column(self):
        """Test adding a simple constant column"""
        data = [["name", "age"], ["John", "25"], ["Jane", "30"]]
        
        def add_constant(row):
            return "Active"
        
        result = add_column(data, "status", add_constant)
        expected = [["name", "age", "status"], ["John", "25", "Active"], ["Jane", "30", "Active"]]
        self.assertEqual(result, expected)

    def test_add_computed_column(self):
        """Test adding a column based on existing data"""
        data = [["name", "age"], ["John", "25"], ["Jane", "30"]]
        
        def get_status(row):
            age = int(row[1])  # age is in column 1
            return "Adult" if age >= 18 else "Minor"
        
        result = add_column(data, "status", get_status)
        expected = [["name", "age", "status"], ["John", "25", "Adult"], ["Jane", "30", "Adult"]]
        self.assertEqual(result, expected)

    def test_add_name_length_column(self):
        """Test adding a column that computes name length"""
        data = [["name", "age"], ["John", "25"], ["Jane", "30"]]
        
        def get_name_length(row):
            return str(len(row[0]))  # name is in column 0
        
        result = add_column(data, "name_length", get_name_length)
        expected = [["name", "age", "name_length"], ["John", "25", "4"], ["Jane", "30", "4"]]
        self.assertEqual(result, expected)

    def test_add_calculated_column(self):
        """Test adding a column with mathematical calculations"""
        data = [["price", "quantity"], ["10.50", "2"], ["25.00", "3"]]
        
        def calculate_total(row):
            price = float(row[0])
            quantity = int(row[1])
            return str(price * quantity)
        
        result = add_column(data, "total", calculate_total)
        expected = [["price", "quantity", "total"], ["10.50", "2", "21.0"], ["25.00", "3", "75.0"]]
        self.assertEqual(result, expected)

    def test_add_conditional_column(self):
        """Test adding a column with conditional logic"""
        data = [["name", "age", "city"], ["John", "25", "NYC"], ["Jane", "30", "LA"]]
        
        def get_region(row):
            city = row[2]
            if city == "NYC":
                return "East"
            elif city == "LA":
                return "West"
            else:
                return "Other"
        
        result = add_column(data, "region", get_region)
        expected = [["name", "age", "city", "region"], ["John", "25", "NYC", "East"], ["Jane", "30", "LA", "West"]]
        self.assertEqual(result, expected)

    def test_empty_data(self):
        """Test with empty data"""
        data = []
        result = add_column(data, "test", lambda row: "value")
        self.assertEqual(result, [])

    def test_single_header_row(self):
        """Test with only header row"""
        data = [["name", "age"]]
        result = add_column(data, "status", lambda row: "Active")
        expected = [["name", "age", "status"]]
        self.assertEqual(result, expected)

if __name__ == "__main__":
    unittest.main() 