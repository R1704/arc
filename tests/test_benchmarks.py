import unittest
from src.benchmarks.arc_agi import ARCAGI
from src.benchmarks.arc_agi2 import ARCAGI2
from src.benchmarks.arc_1d import ARC1D
from src.benchmarks.custom_benchmark import CustomBenchmark

class TestBenchmarks(unittest.TestCase):

    def setUp(self):
        self.arc_agi = ARCAGI()
        self.arc_agi2 = ARCAGI2()
        self.arc_1d = ARC1D()
        self.custom_benchmark = CustomBenchmark()

    def test_arc_agi_initialization(self):
        self.assertIsNotNone(self.arc_agi)
        self.assertTrue(hasattr(self.arc_agi, 'tasks'))

    def test_arc_agi2_initialization(self):
        self.assertIsNotNone(self.arc_agi2)
        self.assertTrue(hasattr(self.arc_agi2, 'tasks'))

    def test_arc_1d_initialization(self):
        self.assertIsNotNone(self.arc_1d)
        self.assertTrue(hasattr(self.arc_1d, 'tasks'))

    def test_custom_benchmark_initialization(self):
        self.assertIsNotNone(self.custom_benchmark)
        self.assertTrue(hasattr(self.custom_benchmark, 'tasks'))

    def test_arc_agi_evaluation(self):
        results = self.arc_agi.evaluate()
        self.assertIsInstance(results, dict)

    def test_arc_agi2_evaluation(self):
        results = self.arc_agi2.evaluate()
        self.assertIsInstance(results, dict)

    def test_arc_1d_evaluation(self):
        results = self.arc_1d.evaluate()
        self.assertIsInstance(results, dict)

    def test_custom_benchmark_evaluation(self):
        results = self.custom_benchmark.evaluate()
        self.assertIsInstance(results, dict)

if __name__ == '__main__':
    unittest.main()