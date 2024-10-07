# preprocess.py
# This script loads an image, resizes it to a specified target size, normalizes the pixel values,
# and returns the preprocessed image in a format suitable for model input.
# It uses the PIL library for image manipulation and NumPy for array handling.
import os
import numpy as np
from PIL import Image

def preprocess_image(image_path, target_size=(224, 224)):
    image = Image.open(image_path)
    image = image.resize(target_size)
    image = np.array(image) / 255.0  # Normalize
    return image

if __name__ == '__main__':
    image_path = "data/test/pizza/8917.jpg"
    preprocessed_image = preprocess_image(image_path)
    print("Image Preprocessed:", preprocessed_image.shape)