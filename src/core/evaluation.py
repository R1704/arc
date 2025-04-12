class EvaluationMetrics:
    def __init__(self):
        self.metrics = {}

    def add_metric(self, name, value):
        self.metrics[name] = value

    def get_metric(self, name):
        return self.metrics.get(name, None)

    def report(self):
        for name, value in self.metrics.items():
            print(f"{name}: {value}")


class Evaluator:
    def __init__(self, model, task):
        self.model = model
        self.task = task
        self.metrics = EvaluationMetrics()

    def evaluate(self):
        # Placeholder for evaluation logic
        predictions = self.model.predict(self.task.input_data)
        self.metrics.add_metric("accuracy", self.calculate_accuracy(predictions, self.task.expected_output))
        self.metrics.add_metric("loss", self.calculate_loss(predictions, self.task.expected_output))
        return self.metrics

    def calculate_accuracy(self, predictions, expected):
        correct = sum(p == e for p, e in zip(predictions, expected))
        return correct / len(expected)

    def calculate_loss(self, predictions, expected):
        return sum((p - e) ** 2 for p, e in zip(predictions, expected)) / len(expected)