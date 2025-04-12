"""
ARC API - Main entry point for external projects to use the ARC library.
This module provides a clean, standardized interface to the ARC dataset and tools.
"""
from typing import Optional, List, Dict, Any, Tuple, Union

from .datasets.registry import DatasetRegistry
from .datasets.downloader import download_dataset
from .core.task import Task
from .core.evaluation import Evaluator, EvaluationMetrics
from .models.base_model import BaseModel
from .utils.visualization import visualize_task
from .datasets.loaders import ARCTask, ARCDataset


def load_dataset(dataset_name: str = "arc-agi", split: str = "training", 
                data_dir: Optional[str] = None) -> ARCDataset:
    """
    Load a specific ARC dataset.
    
    Args:
        dataset_name: Name of the dataset (e.g., "arc-agi", "arc-agi2")
        split: Either "training" or "evaluation"
        data_dir: Optional custom directory for the dataset
        
    Returns:
        An ARCDataset instance for the requested dataset
    """
    # The registry uses hyphen format (arc-agi)
    registry_name = dataset_name if "-" in dataset_name else dataset_name.replace("_", "-")
    return DatasetRegistry.get_dataset(registry_name, data_dir=data_dir, split=split)


def get_task(dataset_name: str, task_id: str, split: str = "training", 
             data_dir: Optional[str] = None) -> ARCTask:
    """
    Get a specific task by ID from a dataset.
    
    Args:
        dataset_name: Name of the dataset (e.g., "arc-agi", "arc-agi2")
        task_id: The ID of the task to load
        split: Either "training" or "evaluation"
        data_dir: Optional custom directory for the dataset
        
    Returns:
        An ARCTask for the requested task_id
    """
    dataset = load_dataset(dataset_name, split, data_dir)
    return dataset.get_task(task_id)


def visualize(task: ARCTask, title: Optional[str] = None, 
              save: bool = False, save_path: Optional[str] = None) -> None:
    """
    Visualize an ARC task.
    
    Args:
        task: The ARCTask to visualize
        title: Optional title for the visualization
        save: Whether to save the visualization to a file
        save_path: Path where to save the visualization (if save=True)
    """
    if title is None:
        title = f"Task {task.task_id} Visualization"
    visualize_task(task, title=title, save=save, save_path=save_path)


def evaluate_model(model: BaseModel, task: ARCTask) -> EvaluationMetrics:
    """
    Evaluate a model on a specific task.
    
    Args:
        model: The model to evaluate
        task: The task to evaluate on
        
    Returns:
        EvaluationMetrics containing the evaluation results
    """
    evaluator = Evaluator(model, task)
    return evaluator.evaluate()


def download_arc_dataset(dataset_name: str = "arc-agi") -> str:
    """
    Download a specific ARC dataset if not present.
    
    Args:
        dataset_name: Name of the dataset to download (e.g., "arc-agi", "arc-agi2")
        
    Returns:
        Path to the downloaded dataset
    """
    # The downloader uses underscore format (arc_agi) 
    downloader_name = dataset_name.replace("-", "_")
    return download_dataset(downloader_name)