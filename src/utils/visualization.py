import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import Normalize

def plot_performance(metrics, title='Model Performance', xlabel='Epochs', ylabel='Accuracy'):
    plt.figure(figsize=(10, 5))
    plt.plot(metrics['epochs'], metrics['accuracy'], label='Accuracy', color='blue')
    plt.plot(metrics['epochs'], metrics['loss'], label='Loss', color='red')
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.legend()
    plt.grid()
    plt.show()

def plot_task_results(task_results, title='Task Results'):
    plt.figure(figsize=(10, 5))
    for task_name, results in task_results.items():
        plt.plot(results['x'], results['y'], label=task_name)
    plt.title(title)
    plt.xlabel('Input')
    plt.ylabel('Output')
    plt.legend()
    plt.grid()
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

def visualize_task(task, title="ARC Task Visualization", save=False):
    """
    Visualize an ARC task's input and output grids.

    Args:
        task: An ARCTask object containing train and test examples.
        title: Title for the visualization.
        save: Whether to save the visualization as an image file.
    """
    num_train = len(task.train_examples)
    num_test = len(task.test_examples)

    arc_cmap = get_arc_color_map()
    norm = Normalize(vmin=0, vmax=8)  # Normalize values to match the color map indices

    fig, axes = plt.subplots(
        nrows=num_train + num_test, ncols=2, figsize=(8, 4 * (num_train + num_test))
    )
    fig.suptitle(title, fontsize=16)

    for i, example in enumerate(task.train_examples):
        axes[i, 0].imshow(example["input"], cmap=arc_cmap, norm=norm, interpolation="nearest")
        axes[i, 0].set_title(f"Train Input {i+1}")
        axes[i, 1].imshow(example["output"], cmap=arc_cmap, norm=norm, interpolation="nearest")
        axes[i, 1].set_title(f"Train Output {i+1}")

    for i, example in enumerate(task.test_examples):
        axes[num_train + i, 0].imshow(example["input"], cmap=arc_cmap, norm=norm, interpolation="nearest")
        axes[num_train + i, 0].set_title(f"Test Input {i+1}")
        axes[num_train + i, 1].imshow(example["output"], cmap=arc_cmap, norm=norm, interpolation="nearest")
        axes[num_train + i, 1].set_title(f"Test Output {i+1}")

    for ax in axes.flat:
        ax.axis("off")

    plt.tight_layout(rect=[0, 0, 1, 0.96])

    if save:
        plt.savefig("task_visualization.png")
        print("Visualization saved as task_visualization.png")

    plt.show()