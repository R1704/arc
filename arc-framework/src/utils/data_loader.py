import os
import json

def load_data(file_path):
    if not os.path.exists(file_path):
        raise FileNotFoundError(f"The file {file_path} does not exist.")
    
    with open(file_path, 'r') as file:
        data = json.load(file)
    
    return data

def preprocess_data(data):
    # Implement any preprocessing steps needed for the data
    processed_data = data  # Placeholder for actual preprocessing logic
    return processed_data

def load_benchmark_data(benchmark_name):
    benchmark_data_path = os.path.join('data', f'{benchmark_name}.json')
    raw_data = load_data(benchmark_data_path)
    return preprocess_data(raw_data)