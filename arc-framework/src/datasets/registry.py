from pathlib import Path
from typing import Dict, Type, Optional
from .loaders import ARCDataset, ARCAGIDataset, ARCAGI2Dataset

# Registry of dataset types
DATASET_REGISTRY = {
    "arc-agi": ARCAGIDataset,
    "arc-agi2": ARCAGI2Dataset,
    # Add other dataset types here
}

class DatasetRegistry:
    """Central registry for managing ARC datasets."""
    
    @staticmethod
    def get_dataset(dataset_type: str, data_dir: Optional[str] = None, split: str = "training") -> ARCDataset:
        """
        Get a dataset by type.
        
        Args:
            dataset_type: Type of dataset (e.g., 'original', 'agi')
            data_dir: Optional custom data directory
            split: 'training' or 'evaluation'
            
        Returns:
            Initialized dataset instance
        """
        if dataset_type not in DATASET_REGISTRY:
            raise ValueError(f"Unknown dataset type: {dataset_type}. Available: {list(DATASET_REGISTRY.keys())}")
        
        dataset_class = DATASET_REGISTRY[dataset_type]
        
        if data_dir:
            return dataset_class(data_dir=data_dir, split=split)
        return dataset_class(split=split)
    
    @staticmethod
    def register_dataset(name: str, dataset_class: Type[ARCDataset]):
        """Register a new dataset type."""
        DATASET_REGISTRY[name] = dataset_class