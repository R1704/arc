from core.task import Task
from core.evaluation import evaluate_model

class ARCAGI:
    def __init__(self):
        self.tasks = self.load_tasks()

    def load_tasks(self):
        # Load and return the specific tasks for ARC-AGI
        return [
            Task(name="Task 1", description="Description of Task 1"),
            Task(name="Task 2", description="Description of Task 2"),
            # Add more tasks as needed
        ]

    def run(self, model):
        results = []
        for task in self.tasks:
            task_result = self.execute_task(task, model)
            results.append(task_result)
        return results

    def execute_task(self, task, model):
        # Execute the task using the provided model and return the result
        model_output = model.predict(task.input_data)
        evaluation_result = evaluate_model(model_output, task.expected_output)
        return evaluation_result

    def evaluate(self, model):
        results = self.run(model)
        # Process and return evaluation results
        return results