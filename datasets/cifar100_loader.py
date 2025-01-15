import torchvision
import torch
from torchvision import transforms, datasets
from torch.utils.data import DataLoader

def get_cifar100_loaders(batch_size):
    """
    Prepare DataLoaders for the CIFAR-100 dataset with transformations.

    Args:
        batch_size (int): Number of samples per batch for the DataLoader.

    Returns:
        trainloader (torch.utils.data.DataLoader): DataLoader for the CIFAR-100 training dataset.
        testloader (torch.utils.data.DataLoader): DataLoader for the CIFAR-100 test dataset.
        classes (list): List of class names for the CIFAR-100 dataset.
    """
    # ---------------------------------------------------
    # Define Transformations
    # ---------------------------------------------------
    # Data augmentation and normalization for training and test datasets.
    # Training: Adds random cropping and horizontal flipping for data augmentation.
    # Test: Only normalization, no data augmentation.
    transform = transforms.Compose([
        transforms.RandomCrop(32, padding=4),  # Randomly crop with padding for better generalization
        transforms.RandomHorizontalFlip(),    # Random horizontal flipping for data augmentation
        transforms.ToTensor(),                # Convert PIL images to PyTorch tensors
        transforms.Normalize((0.5, 0.5, 0.5), (0.5, 0.5, 0.5))  # Normalize to range [-1, 1]
    ])

    # ---------------------------------------------------
    # Load CIFAR-100 Dataset
    # ---------------------------------------------------
    # Training Dataset
    trainset = datasets.CIFAR100(
        root='./data', train=True, download=True, transform=transform
    )
    trainloader = DataLoader(
        trainset, batch_size=batch_size, shuffle=True, num_workers=2
    )

    # Test Dataset
    testset = datasets.CIFAR100(
        root='./data', train=False, download=True, transform=transform
    )
    testloader = DataLoader(
        testset, batch_size=batch_size, shuffle=False, num_workers=2
    )

    # ---------------------------------------------------
    # Retrieve Class Labels
    # ---------------------------------------------------
    # CIFAR-100 contains 100 classes, which can be retrieved as a list of strings.
    classes = trainset.classes

    # ---------------------------------------------------
    # Return the DataLoaders and Class Labels
    # ---------------------------------------------------
    return trainloader, testloader, classes