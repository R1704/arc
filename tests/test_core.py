import unittest
from arc.core.task import Task
from arc.core.grid import Grid
from arc.core.evaluation import evaluate_model
from arc.benchmarks.arc_agi import ARCAGI
from arc.benchmarks.arc_agi2 import ARCAGI2
from arc.benchmarks.arc_1d import ARC1D
from arc.models.base_model import BaseModel

class TestCore(unittest.TestCase):

    def setUp(self):
        self.task = Task()
        self.grid = Grid()
        self.model = BaseModel()

    def test_task_initialization(self):
        self.assertIsNotNone(self.task)

    def test_grid_configuration(self):
        self.grid.configure(self.task)
        self.assertTrue(self.grid.is_configured())

    def test_evaluate_model(self):
        result = evaluate_model(self.model, self.task)
        self.assertIsInstance(result, dict)

    def test_arc_agi_benchmark(self):
        arc_agi = ARCAGI()
        tasks = arc_agi.get_tasks()
        self.assertGreater(len(tasks), 0)

    def test_arc_agi2_benchmark(self):
        arc_agi2 = ARCAGI2()
        tasks = arc_agi2.get_tasks()
        self.assertGreater(len(tasks), 0)

    def test_arc_1d_benchmark(self):
        arc_1d = ARC1D()
        tasks = arc_1d.get_tasks()
        self.assertGreater(len(tasks), 0)

if __name__ == '__main__':
    unittest.main()