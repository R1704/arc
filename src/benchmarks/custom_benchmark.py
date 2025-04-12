from src.core.task import Task
from src.core.evaluation import evaluate_model

class CustomBenchmark:
    def __init__(self, tasks):
        self.tasks = tasks

    def run(self, model):
        results = {}
        for task in self.tasks:
            task_instance = Task(task)
            task_instance.setup()
            predictions = model.predict(task_instance.data)
            results[task.name] = evaluate_model(predictions, task_instance.labels)
        return results

    def add_task(self, task):
        self.tasks.append(task)