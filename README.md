# ARC Framework

A framework for working with the Abstract Reasoning Corpus (ARC) challenge by François Chollet.

## Overview

The ARC Framework provides tools for loading, visualizing, and evaluating ARC tasks. It supports multiple versions of the ARC dataset, including ARC-AGI and ARC-AGI2.

## Project Structure

The project is organized into several key directories and files:

- **src/**: Contains the core functionality of the framework.
  - **core/**: Implements the main components of the framework, including task management and evaluation.
  - **benchmarks/**: Contains implementations of various ARC benchmarks, such as ARC-AGI, ARC-AGI2, and ARC-1D.
  - **utils/**: Provides utility functions for data loading and visualization.
  - **models/**: Defines model architectures that can be used to tackle the ARC challenges.

- **tests/**: Contains unit tests for the core functionalities, benchmarks, and utilities to ensure the reliability of the framework.

- **examples/**: Provides example implementations of different models using the framework, demonstrating how to utilize the provided functionalities.

- **data/**: Contains information about the datasets used in the benchmarks.

- **setup.py**: The setup script for the package, defining metadata and dependencies.

- **pyproject.toml**: Configuration file for the project, including build system requirements.

- **requirements.txt**: Lists the dependencies required for the project.

## Installation

### Option 1: Install from GitHub

```bash
pip install git+https://github.com/yourusername/arc.git
```

### Option 2: Local Installation

Clone the repository and install it locally:

```bash
git clone https://github.com/yourusername/arc.git
cd arc
pip install -e .
```

## Quick Start

Here's a simple example of using the ARC Framework:

```python
from arc import load_dataset, get_task, visualize, download_arc_dataset

# Download dataset if not present
download_arc_dataset("arc-agi")

# Load a dataset
dataset = load_dataset("arc-agi", split="training")
print(f"Loaded dataset with {len(dataset)} tasks")

# Get a specific task
task_id = dataset.task_ids[0]
task = get_task("arc-agi", task_id)

# Visualize the task
visualize(task, save=True)
```

## Using ARC Framework in External Projects

The ARC Framework is designed to be easily used in external projects. Here's how you can integrate it:

### 1. Loading Datasets

```python
from arc import load_dataset

# Load the training set of ARC-AGI
training_dataset = load_dataset("arc-agi", split="training")

# Load the evaluation set of ARC-AGI2
eval_dataset = load_dataset("arc-agi2", split="evaluation")
```

### 2. Working with Tasks

```python
from arc import get_task

# Get a specific task by ID
task = get_task("arc-agi", "08573cc6", split="training")

# Iterate through all tasks in a dataset
dataset = load_dataset("arc-agi", split="training")
for task_id in dataset.task_ids:
    task = dataset.get_task(task_id)
    print(f"Task {task_id}: {len(task.train_examples)} train examples, {len(task.test_examples)} test examples")
```

### 3. Visualizing Tasks

```python
from arc import visualize

# Visualize a task
visualize(task, title="My Task Visualization")

# Save the visualization
visualize(task, save=True, save_path="path/to/save/visualization.png")
```

### 4. Implementing and Evaluating Models

```python
from arc import BaseModel, evaluate_model

# Implement a model by subclassing BaseModel
class MyModel(BaseModel):
    def predict(self, input_data):
        # Implement prediction logic
        return processed_output
        
    def train(self, train_examples):
        # Implement training logic
        pass

# Create your model
model = MyModel()

# Train your model
model.train(task.train_examples)

# Evaluate your model on a task
metrics = evaluate_model(model, task)
metrics.report()  # Print metrics
```

## Advanced Usage

For more advanced usage, see the examples in the `examples/` directory:

- `basic_usage.py`: Simple example of loading and visualizing tasks
- `external_usage.py`: Example of using the framework in an external project

## Available Datasets

- `arc-agi`: The original ARC-AGI dataset
- `arc-agi2`: The updated ARC-AGI2 dataset

## Running Benchmarks

```python
from arc.benchmarks.arc_agi import ARCAGIBenchmark
from arc.models.simple_model import SimpleModel

# Initialize the benchmark
benchmark = ARCAGIBenchmark()

# Create your model
model = SimpleModel()

# Run the benchmark
results = benchmark.evaluate(model)
benchmark.report(results)
```

## Contributing

Contributions to the ARC Framework are welcome! Please feel free to submit issues or pull requests to improve the framework or add new benchmarks and models.

## License

[Your License]