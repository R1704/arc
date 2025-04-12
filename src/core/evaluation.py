class EvaluationMetrics:
    def __init__(self):
        self.metrics = {}

    def add_metric(self, name, value):
        self.metrics[name] = value

    def get_metric(self, name):
        return self.metrics.get(name, None)

    def get_all_metrics(self):
        """Returns all metrics as a dictionary"""
        return self.metrics.copy()
        
    def report(self, print_output=True):
        """
        Report all metrics, optionally printing them
        
        Args:
            print_output: Whether to print the metrics to stdout
            
        Returns:
            Dictionary of metrics
        """
        if print_output:
            for name, value in self.metrics.items():
                print(f"{name}: {value}")
        
        return self.get_all_metrics()


class Evaluator:
    def __init__(self, model, task):
        self.model = model
        self.task = task
        self.metrics = EvaluationMetrics()

    def evaluate(self):
        """
        Evaluate the model on the task
        
        Returns:
            EvaluationMetrics object with evaluation results
        """
        # ARCTask has test_examples attribute with input and output
        test_inputs = [example["input"] for example in self.task.test_examples]
        test_outputs = [example["output"] for example in self.task.test_examples if "output" in example]
        
        # Get predictions from model
        predictions = self.model.predict(test_inputs)
        
        # Calculate basic metrics
        if test_outputs:  # Only calculate if we have expected outputs
            self.metrics.add_metric("accuracy", self.calculate_accuracy(predictions, test_outputs))
            self.metrics.add_metric("loss", self.calculate_loss(predictions, test_outputs))
            
            # Add any task-specific metrics
            self._add_task_specific_metrics(predictions, test_outputs)
        else:
            self.metrics.add_metric("note", "No expected outputs available for evaluation")
        
        return self.metrics
        
    def _add_task_specific_metrics(self, predictions, expected):
        """
        Add any metrics specific to the task type
        
        This can be overridden in subclasses to provide task-specific metrics
        """
        pass

    def calculate_accuracy(self, predictions, expected):
        """Calculate the accuracy of predictions"""
        # Handle case where predictions or expected is a list of grids
        if isinstance(predictions, list) and isinstance(expected, list):
            if all(hasattr(p, 'tolist') and hasattr(e, 'tolist') for p, e in zip(predictions, expected)):
                # Convert numpy arrays to lists for comparison
                matches = [np.array_equal(p, e) for p, e in zip(predictions, expected)]
                return sum(matches) / len(matches) if matches else 0
            
            # Special case for list of lists (2D grids as nested lists)
            if all(isinstance(p, list) and isinstance(e, list) for p, e in zip(predictions, expected)):
                try:
                    import numpy as np
                    # Convert to numpy arrays for comparison
                    matches = [np.array_equal(np.array(p), np.array(e)) for p, e in zip(predictions, expected)]
                    return sum(matches) / len(matches) if matches else 0
                except:
                    # Fallback: string comparison of the lists
                    matches = [str(p) == str(e) for p, e in zip(predictions, expected)]
                    return sum(matches) / len(matches) if matches else 0
        
        # Fall back to simple equality check
        correct = sum(p == e for p, e in zip(predictions, expected))
        return correct / len(expected) if expected else 0

    def calculate_loss(self, predictions, expected):
        """Calculate the MSE loss between predictions and expected output"""
        import numpy as np
        
        # Ensure predictions and expected are of the same length
        if len(predictions) != len(expected):
            return float('inf')  # Return worst possible loss
            
        total_mse = 0
        count = 0
        
        for p, e in zip(predictions, expected):
            # Handle numpy arrays
            if hasattr(p, 'flatten') and hasattr(e, 'flatten'):
                p_flat = p.flatten()
                e_flat = e.flatten()
                mse = ((p_flat - e_flat) ** 2).mean()
                total_mse += mse
                count += 1
            
            # Handle nested lists (2D grids)
            elif isinstance(p, list) and isinstance(e, list):
                try:
                    # Convert to numpy arrays
                    p_array = np.array(p)
                    e_array = np.array(e)
                    
                    if p_array.shape != e_array.shape:
                        # Different shapes, count as maximum error
                        total_mse += 1.0  # Normalized max error
                    else:
                        # Same shape, calculate MSE
                        p_flat = p_array.flatten()
                        e_flat = e_array.flatten()
                        mse = ((p_flat - e_flat) ** 2).mean()
                        total_mse += mse
                    count += 1
                except:
                    # If conversion fails, use string comparison
                    total_mse += 1.0 if str(p) != str(e) else 0.0
                    count += 1
            
            # Handle scalar values
            elif isinstance(p, (int, float)) and isinstance(e, (int, float)):
                mse = (p - e) ** 2
                total_mse += mse
                count += 1
            
            else:
                # If types are incompatible, count as error
                total_mse += 1.0
                count += 1
        
        # Return average MSE
        return total_mse / count if count > 0 else 0