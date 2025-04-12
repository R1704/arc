from datasets.downloader import download_dataset
from datasets.registry import DatasetRegistry
from utils.visualization import visualize_task

def main():
    # Download the ARC-AGI-2 dataset if not present
    download_dataset("arc_agi2")
    
    # Load the training set using DatasetRegistry
    training_dataset = DatasetRegistry.get_dataset("arc-agi", data_dir="data/arc_agi2", split="training")
    print(f"Loaded {len(training_dataset)} training tasks")
    
    # Get a specific task
    task = training_dataset.get_task(training_dataset.task_ids[0])
    print(f"First task: {task}")
    
    # Visualize the first task
    visualize_task(task, title=f"Task {task.task_id} Visualization", save=True)
    
    # Iterate through all tasks
    for i, task in enumerate(training_dataset):
        if i < 3:  # Just show the first few
            print(f"Task {task.task_id}: {len(task.train_examples)} train examples, {len(task.test_examples)} test examples")

if __name__ == "__main__":
    main()