# ARC Framework

The ARC Framework is designed to facilitate experimentation and evaluation of various models against the ARC challenges proposed by François Chollet. This framework provides a structured approach to implement, test, and evaluate different benchmarks, making it easier for researchers and developers to work with these challenges.

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

To install the ARC Framework, clone the repository and install the required dependencies:

```bash
git clone <repository-url>
cd arc-framework
pip install -r requirements.txt
```

## Usage

To use the ARC Framework, you can import the necessary modules in your Python scripts. For example, to work with the ARC-AGI benchmark:

```python
from src.benchmarks.arc_agi import ARCAGI
from src.models.base_model import BaseModel

# Initialize the benchmark and model
benchmark = ARCAGI()
model = BaseModel()

# Run the evaluation
results = benchmark.evaluate(model)
print(results)
```

## Contributing

Contributions to the ARC Framework are welcome! Please feel free to submit issues or pull requests to improve the framework or add new benchmarks and models.

## License

This project is licensed under the MIT License. See the LICENSE file for more details.