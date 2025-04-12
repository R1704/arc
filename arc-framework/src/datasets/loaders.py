import json
import numpy as np
from pathlib import Path
from typing import Dict, List, Iterator, Tuple, Any

class ARCTask:
    """Represents a single ARC task with train and test examples."""
    
    def __init__(self, task_id: str, task_data: Dict[str, List[Dict[str, Any]]]):
        self.task_id = task_id
        self.train_examples = task_data.get("train", [])
        self.test_examples = task_data.get("test", [])
    
    def __str__(self) -> str:
        return f"ARCTask(id={self.task_id}, train_examples={len(self.train_examples)}, test_examples={len(self.test_examples)})"

class ARCDataset:
    """Base loader for ARC datasets."""
    
    def __init__(self, dataset_dir: str, split: str = "training"):
        """
        Initialize the dataset loader.
        
        Args:
            dataset_dir: Path to the dataset directory (e.g., data/arc_original)
            split: Either 'training' or 'evaluation'
        """
        self.dataset_path = Path(dataset_dir)
        self.split = split
        
        # Validate the dataset structure
        self.split_path = self.dataset_path / split
        if not self.split_path.exists() or not self.split_path.is_dir():
            raise ValueError(f"Split '{split}' not found at {self.split_path}")
        
        # Load task IDs
        self.task_ids = [f.stem for f in self.split_path.glob("*.json")]
    
    def __len__(self) -> int:
        return len(self.task_ids)
    
    def __iter__(self) -> Iterator[ARCTask]:
        """Iterate through all tasks in the dataset."""
        for task_id in self.task_ids:
            yield self.get_task(task_id)
            
    def get_task(self, task_id: str) -> ARCTask:
        """Load a specific task by ID."""
        task_path = self.split_path / f"{task_id}.json"
        
        if not task_path.exists():
            raise ValueError(f"Task {task_id} not found in {self.split} split")
            
        with open(task_path, 'r') as f:
            task_data = json.load(f)
            
        return ARCTask(task_id, task_data)

class ARCAGIDataset(ARCDataset):
    """Loader for the ARC-AGI dataset."""
    def __init__(self, data_dir: str = "./data/arc_agi", split: str = "training"):
        super().__init__(dataset_dir=data_dir, split=split)

class ARCAGI2Dataset(ARCDataset):
    """Loader for the ARC-AGI-2 dataset."""
    def __init__(self, data_dir: str = "./data/arc_agi2", split: str = "training"):
        super().__init__(dataset_dir=data_dir, split=split)