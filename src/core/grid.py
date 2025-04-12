class Grid:
    def __init__(self):
        self.tasks = []
        self.parameters = {}

    def add_task(self, task):
        self.tasks.append(task)

    def set_parameters(self, params):
        self.parameters.update(params)

    def get_configuration(self):
        return {
            "tasks": self.tasks,
            "parameters": self.parameters
        }

    def clear(self):
        self.tasks = []
        self.parameters = {}