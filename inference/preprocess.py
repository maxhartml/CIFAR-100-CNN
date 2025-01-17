import torchvision.transforms as transforms
from PIL import Image
from configuration.config_1 import *

def preprocess_image(image_path):
    """
    Preprocess an image for inference, including resizing, normalization, and tensor conversion.

    Args:
        image_path (str): Path to the input image.

    Returns:
        torch.Tensor: Preprocessed image tensor with a batch dimension.
    """
    # Define the transformations: resize, convert to tensor, and normalize
    transform = transforms.Compose([
        transforms.Resize(IMAGE_SIZE),  # Resize image to 32x32 pixels
        transforms.ToTensor(),       # Convert image to PyTorch tensor
        transforms.Normalize(mean=MEAN, std=STD)  # Normalize to CIFAR-like range
    ])

    # Open the image, ensure it's RGB, and apply transformations
    img = Image.open(image_path).convert('RGB')
    img = transform(img).unsqueeze(0)  # Add batch dimension

    return img