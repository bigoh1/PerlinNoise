import numpy as np

STEP = 4
N = 1

possible_gradients = np.array([
    [1, 1],
    [-1, 1],
    # [-1, -1],
    # [1, -1],
])

# possible_gradients = np.array([(np.cos(r), np.sin(r)) for r in np.linspace(0, 2*np.pi, 100)])

origins = np.array([
    [0, 4],
    [4, 4],
    [4, 0],
    [0, 0]
])