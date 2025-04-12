# ARC Framework Data Documentation

## Overview

This directory contains data resources used for the various benchmarks in the ARC framework. The data is essential for evaluating different models against the ARC challenges proposed by François Chollet.

## Data Structure

The data used in the benchmarks is organized into specific formats that correspond to the tasks defined in the benchmarks. Each benchmark may have its own unique data requirements, and users should refer to the respective benchmark documentation for details on the data format and structure.

## Benchmarks

The following benchmarks utilize the data in this directory:

- **ARC-AGI**: This benchmark focuses on tasks that assess general intelligence in artificial agents. Data for this benchmark includes a variety of task types and configurations.
  
- **ARC-AGI2**: An extension of the ARC-AGI benchmark, featuring additional tasks and evaluation criteria. The data structure is similar to ARC-AGI but may include new task types.
  
- **ARC-1D**: This benchmark is designed for one-dimensional tasks. The data is structured to facilitate the evaluation of models on these specific challenges.

- **Custom Benchmark**: Users can define their own benchmarks and data requirements. The framework allows for flexibility in data formats to accommodate various task designs.

## Usage

To utilize the data in your benchmarks, ensure that the data files are correctly formatted and placed in this directory. You can then load the data using the utilities provided in the `src/utils/data_loader.py` module.

## Contribution

If you wish to contribute additional data or benchmarks, please follow the guidelines outlined in the main project README and ensure that your data adheres to the established formats.

## License

This project is licensed under the MIT License. Please see the LICENSE file for more details.