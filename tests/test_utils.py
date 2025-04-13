import unittest
from arc.utils import data_loader, visualization

class TestUtils(unittest.TestCase):

    def test_data_loader(self):
        # Test data loading functionality
        data = data_loader.load_data('path/to/data')
        self.assertIsNotNone(data)
        self.assertGreater(len(data), 0)

    def test_visualization(self):
        # Test visualization functionality
        result = visualization.plot_results([1, 2, 3], [1, 4, 9])
        self.assertIsNone(result)  # Assuming plot_results returns None after plotting

if __name__ == '__main__':
    unittest.main()