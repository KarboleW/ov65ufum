import numpy as np
from ipywidgets import interact, fixed
from PIL import Image
import matplotlib.pyplot as plt

def imshow(X, resize=None):
    """Plots an image of resized size if argument is given.

    Parameters
    ----------
    X : numpy.array
        Image as numpy array..
    resize : tuple, optional
        Resize size (width, height).
        
    Returns
    -------
    PIL.Image
        Resized image as Pillow Image object.
    """
    
    X = Image.fromarray(np.uint8(X))
    if resize != None:
        X = X.resize(resize)
    
    plt.figure(), plt.imshow(X), plt.show()
    
    return X
