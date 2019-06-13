"""
Calculate indices and other features from multi-channel point cloud data

Inputs are assumed to be n x 6 arrays with each row being x, y, z, r, g, b
"""

import numpy as np

from scipy.misc import bytescale
from skimage.color import rgb2lab


def calculate_ngrdvi(data):
    """ Calculates red-green difference index (NGRDVI) from color data

    Args:
        data: An n x d array of input data. Rows are [x, y, z, r, g, b, ...]

    Returns:
        An n x 1 array of NGRDVI values
    """

    red = data[:, 3]
    green = data[:, 4]

    return (green - red) / (green + red)


def calculate_vdvi(data):
    """ Calculates visual difference vegetation index (VDVI) from color data

    Args:
        data: An n x d array of input data. Rows are [x, y, z, r, g, b, ...]

    Returns:
        An n x 1 array of VDVI values
    """

    red = data[:, 3]
    green = data[:, 4]
    blue = data[:, 5]

    return (2 * green - red - blue) / (2 * green + red + blue)


def calculate_color_features(data):
    """ Calculates color features related to the greenness of each point.

    The default features are [a, b, NGRDVI] where a and b are the green-red and
    blue-yellow coordinates of the CIE-Lab color space.

    Args:
        data: An n x d array of input data. Rows are [x, y, z, r, g, b, ...]

    Returns:
        An n x 3 array of features for each point.
    """

    rgb = bytescale(data[:, 3:6]).astype(np.int16)
    lab = rgb2lab(np.array([rgb]))[0].reshape(-1,3)
    ngrdvi = calculate_ngrdvi(data).reshape(-1,1)
    return np.hstack([lab[:, 1:3], ngrdvi])
