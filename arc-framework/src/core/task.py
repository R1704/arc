class Task:
    def __init__(self, task_id, description, parameters):
        self.task_id = task_id
        self.description = description
        self.parameters = parameters

    def setup(self):
        # Code to set up the task based on parameters
        pass

    def execute(self, model):
        # Code to execute the task using the provided model
        pass

    def evaluate(self, results):
        # Code to evaluate the results of the task execution
        pass

    def __str__(self):
        return f"Task {self.task_id}: {self.description}"