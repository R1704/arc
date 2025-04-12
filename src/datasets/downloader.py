import os
import requests
import json
import zipfile
import subprocess
from pathlib import Path
from .registry import DATASET_REGISTRY

ARC_DATASETS = {
    "arc_agi": {
        "type": "github_zip",
        "url": "https://github.com/fchollet/ARC-AGI/archive/refs/heads/master.zip",
        "extract_dir": "ARC-AGI-master/data",
        "target_dir": "arc_agi"
    },
    "arc_agi2": {
        "type": "git",
        "url": "https://github.com/arcprize/ARC-AGI-2",
        "data_dir": "data",
        "target_dir": "arc_agi2"
    },
    # Add other datasets with their sources
}

def download_dataset(dataset_name, data_dir="./data"):
    """Download and extract a specific ARC dataset."""
    if dataset_name in DATASET_REGISTRY:
        print(f"Dataset {dataset_name} is already registered. Skipping download.")
        return Path(data_dir) / ARC_DATASETS[dataset_name]["target_dir"]

    if dataset_name not in ARC_DATASETS:
        raise ValueError(f"Unknown dataset: {dataset_name}. Available: {list(ARC_DATASETS.keys())}")
    
    dataset_info = ARC_DATASETS[dataset_name]
    data_path = Path(data_dir) / dataset_info["target_dir"]
    
    if data_path.exists():
        print(f"Dataset {dataset_name} already exists at {data_path}")
        return data_path
    
    # Create the data directory if it doesn't exist
    Path(data_dir).mkdir(parents=True, exist_ok=True)
    
    if dataset_info["type"] == "github_zip":
        download_github_zip(dataset_info, data_dir, data_path)
    elif dataset_info["type"] == "git":
        clone_git_repo(dataset_info, data_dir, data_path)
    else:
        raise ValueError(f"Unknown dataset type: {dataset_info['type']}")
    
    print(f"Dataset {dataset_name} ready at {data_path}")
    return data_path

def download_github_zip(dataset_info, data_dir, data_path):
    """Download and extract a dataset from a GitHub ZIP archive."""
    print(f"Downloading dataset from {dataset_info['url']}...")
    zip_path = Path(data_dir) / f"{Path(dataset_info['url']).name}"
    
    # Download the zip file
    response = requests.get(dataset_info['url'], stream=True)
    with open(zip_path, 'wb') as f:
        for chunk in response.iter_content(chunk_size=8192):
            f.write(chunk)
    
    # Validate the downloaded file
    if not zipfile.is_zipfile(zip_path):
        raise zipfile.BadZipFile(f"Downloaded file is not a valid ZIP file: {zip_path}")
    
    print(f"Extracting dataset...")
    with zipfile.ZipFile(zip_path, 'r') as zip_ref:
        zip_ref.extractall(data_dir)
    
    # Move files to the correct location
    extract_path = Path(data_dir) / dataset_info["extract_dir"]
    data_path.mkdir(parents=True, exist_ok=True)
    
    if not extract_path.exists():
        raise FileNotFoundError(f"Expected path {extract_path} not found in downloaded archive")
        
    # Ensure the training and evaluation directories are moved correctly
    if extract_path.exists() and extract_path.is_dir():
        for subdir in ['training', 'evaluation']:
            src_dir = extract_path / subdir
            dst_dir = data_path / subdir
            if src_dir.exists() and src_dir.is_dir():
                import shutil
                shutil.move(str(src_dir), str(dst_dir))
            else:
                print(f"Warning: {subdir} directory not found in {extract_path}")
    
    # Clean up
    repo_root = Path(data_dir) / Path(dataset_info["extract_dir"]).parts[0]
    if repo_root.exists():
        shutil.rmtree(repo_root)
    zip_path.unlink()

def clone_git_repo(dataset_info, data_dir, data_path):
    """Clone a Git repository and extract its data."""
    print(f"Cloning repository from {dataset_info['url']}...")
    temp_dir = Path(data_dir) / "temp_repo"
    
    # Clone the repo
    subprocess.run(["git", "clone", dataset_info['url'], str(temp_dir)], check=True)
    
    # Copy the data directory
    src_data_dir = temp_dir / dataset_info["data_dir"]
    data_path.mkdir(parents=True, exist_ok=True)
    
    import shutil
    if src_data_dir.is_dir():
        # Copy the training and evaluation directories
        for subdir in src_data_dir.iterdir():
            if subdir.is_dir():
                dst_subdir = data_path / subdir.name
                if not dst_subdir.exists():
                    shutil.copytree(subdir, dst_subdir)
    
    # Clean up
    shutil.rmtree(temp_dir)