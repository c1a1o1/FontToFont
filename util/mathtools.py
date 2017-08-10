import numpy as np


def mse(x, y):
    return np.linalg.norm(x - y)