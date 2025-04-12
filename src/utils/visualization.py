import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize
import os

def plot_performance(metrics, title='Model Performance', xlabel='Epochs', ylabel='Accuracy', save_path=None):
    plt.figure(figsize=(10, 5))
    plt.plot(metrics['epochs'], metrics['accuracy'], label='Accuracy', color='blue')
    plt.plot(metrics['epochs'], metrics['loss'], label='Loss', color='red')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    
    if save_path:
        plt.savefig(save_path)
    
    plt.show()

def plot_task_results(task_results, title='Task Results', save_path=None):
    plt.figure(figsize=(10, 5))
    for task_name, results in task_results.items():
        plt.plot(results['x'], results['y'], label=task_name)
    plt.title(title)
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.legend()
    plt.grid()
    
    if save_path:
        plt.savefig(save_path)
    
    plt.show()

def save_plot(figure, filename):
    figure.savefig(filename)
    plt.close(figure)

def get_arc_color_map():
    """Returns a consistent color map for ARC tasks."""
    from matplotlib.colors import ListedColormap

    # Define the ARC AGI color scheme
    arc_colors = [
        "#000000",  # Black
        "#0074D9",  # Blue
        "#FF4136",  # Red
        "#2ECC40",  # Green
        "#FFDC00",  # Yellow
        "#AAAAAA",  # Gray
        "#F012BE",  # Magenta
        "#7FDBFF",  # Light Blue
        "#870C25"   # Dark Red
    ]
    return ListedColormap(arc_colors)

def visualize_task(task, title=None, save=False, save_path=None, show=True):
    """
    Visualize an ARC task's input and output grids.

    Args:
        task: An ARCTask object containing train and test examples.
        title: Title for the visualization. If None, uses task ID.
        save: Whether to save the visualization as an image file.
        save_path: Path where to save the visualization. If None, uses 'task_{task.task_id}.png'.
        show: Whether to display the plot (True) or just return the figure (False).
        
    Returns:
        The matplotlib figure object for further customization if needed.
    """
    num_train = len(task.train_examples)
    num_test = len(task.test_examples)
    
    if title is None:
        title = f"Task {task.task_id} Visualization"
    
    if save and save_path is None:
        save_path = f"task_{task.task_id}.png"

    arc_cmap = get_arc_color_map()
    norm = Normalize(vmin=0, vmax=8)  # Normalize values to match the color map indices

    fig, axes = plt.subplots(
        nrows=num_train + num_test, ncols=2, figsize=(8, 4 * (num_train + num_test))
    )
    
    # Handle the case of a single row
    if num_train + num_test == 1:
        axes = np.array([axes])
        
    fig.suptitle(title, fontsize=16)

    for i, example in enumerate(task.train_examples):
        axes[i, 0].imshow(example["input"], cmap=arc_cmap, norm=norm, interpolation="nearest")
        axes[i, 0].set_title(f"Train Input {i+1}")
        axes[i, 1].imshow(example["output"], cmap=arc_cmap, norm=norm, interpolation="nearest")
        axes[i, 1].set_title(f"Train Output {i+1}")

    for i, example in enumerate(task.test_examples):
        idx = num_train + i
        if idx < len(axes):
            axes[idx, 0].imshow(example["input"], cmap=arc_cmap, norm=norm, interpolation="nearest")
            axes[idx, 0].set_title(f"Test Input {i+1}")
            if "output" in example:  # Show output if available
                axes[idx, 1].imshow(example["output"], cmap=arc_cmap, norm=norm, interpolation="nearest")
                axes[idx, 1].set_title(f"Test Output {i+1}")
            else:
                axes[idx, 1].text(0.5, 0.5, "Output not available", 
                                 horizontalalignment='center', verticalalignment='center')

    for ax in axes.flat:
        ax.axis("off")

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    if save:
        # Create directory if it doesn't exist
        save_dir = os.path.dirname(save_path)
        if save_dir and not os.path.exists(save_dir):
            os.makedirs(save_dir)
            
        plt.savefig(save_path)
        print(f"Visualization saved as {save_path}")

    if show:
        plt.show()
    else:
        plt.close(fig)
        
    return fig

def visualize_prediction(task, prediction, title=None, save=False, save_path=None):
    """
    Visualize a model's prediction for an ARC task.
    
    Args:
        task: The ARCTask object
        prediction: The model's prediction (output grid)
        title: Title for the visualization
        save: Whether to save the visualization
        save_path: Where to save the visualization
    """
    num_train = len(task.train_examples)
    num_test = len(task.test_examples)
    
    if title is None:
        title = f"Task {task.task_id} with Prediction"
        
    arc_cmap = get_arc_color_map()
    norm = Normalize(vmin=0, vmax=8)

    # Create a figure with 3 columns: Input, Expected Output, Prediction
    fig, axes = plt.subplots(
        nrows=num_test, ncols=3, figsize=(12, 4 * num_test)
    )
    
    # Handle the case of a single row
    if num_test == 1:
        axes = np.array([axes])
        
    fig.suptitle(title, fontsize=16)
    
    for i, example in enumerate(task.test_examples):
        # Input
        axes[i, 0].imshow(example["input"], cmap=arc_cmap, norm=norm, interpolation="nearest")
        axes[i, 0].set_title(f"Test Input {i+1}")
        
        # Expected Output (if available)
        if "output" in example:
            axes[i, 1].imshow(example["output"], cmap=arc_cmap, norm=norm, interpolation="nearest")
            axes[i, 1].set_title(f"Expected Output {i+1}")
        else:
            axes[i, 1].text(0.5, 0.5, "Expected output not available", 
                         horizontalalignment='center', verticalalignment='center')
        
        # Prediction
        if i < len(prediction):
            axes[i, 2].imshow(prediction[i], cmap=arc_cmap, norm=norm, interpolation="nearest")
            axes[i, 2].set_title(f"Model Prediction {i+1}")
        else:
            axes[i, 2].text(0.5, 0.5, "No prediction available", 
                        horizontalalignment='center', verticalalignment='center')
    
    for ax in axes.flat:
        ax.axis("off")
        
    plt.tight_layout(rect=[0, 0, 1, 0.96])
    
    if save:
        # Create directory if it doesn't exist
        save_dir = os.path.dirname(save_path) if save_path else ""
        if save_dir and not os.path.exists(save_dir):
            os.makedirs(save_dir)
            
        save_path = save_path or f"task_{task.task_id}_prediction.png"
        plt.savefig(save_path)
        print(f"Prediction visualization saved as {save_path}")
        
    plt.show()
    return fig