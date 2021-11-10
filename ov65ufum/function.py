import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt

def imshow(X, resize=None):
    """
    You should create a way to resize an image from an array X.
    The use of widgets is optional but you can take a look to interact.
    We should be able to install this package in Google Colab from your Git
    repo.
    """
    
    image = Image.fromarray(X)
    image = image.resize(resize)
    
    plt.figure()
    plt.imshow(image)
    plt.show()
    
    return image
