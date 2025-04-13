"""
ARC - Abstract Reasoning Corpus tools and utilities.
This package provides tools for loading, visualizing, and evaluating ARC tasks.
"""

# Import and expose the main API functions
from .api import (
    load_dataset,
    get_task,
    visualize,
    evaluate_model,
    download_arc_dataset
)

# Expose key classes for direct import
from .datasets.loaders import ARCTask, ARCDataset
from .core.evaluation import Evaluator, EvaluationMetrics
from .models.base_model import BaseModel

# Version information
__version__ = "0.1.0"