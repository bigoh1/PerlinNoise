import numpy as np
import colorsys


def scale(x, x0, x1, y0, y1):
    return (y0 * (x1 - x) + y1 * (x - x0)) / (x1 - x0)


# TODO: optimize
def cos_interpolate(x, x0, x1, y0, y1):
    return -0.5 * (np.cos((x - x0) * np.pi / (x1 - x0)) - 1) * (y1 - y0) + y0


def get_cell_pos(point: np.array, n, step):
    x_num = min(np.floor(point[0] / step), max(n - 1, 0))
    y_num = min(np.floor(point[1] / step), max(n - 1, 0))

    return int(x_num), int(y_num)


def get_origins(n, step):
    result = []
    for j in range(n + 1):
        result.append([])
        for i in range(n + 1):
            result[-1].append((step * i, step * j))
    return np.array(result)


def get_gradients(n):
    possible_gradients = np.array([
        [1, 1],
        [-1, 1],
        [-1, -1],
        [1, -1],
    ])

    rand_ind = np.random.randint(possible_gradients.shape[0], size=((n + 1) ** 2))
    gradients = possible_gradients[rand_ind, :].reshape((n + 1, n + 1, 2))
    return gradients


def near_vectors(point: np.array, source: np.array, n: int, step: int):
    """
    :param point: 2d point (x, y), such that 0 <= x,y < n*step
    :param source: either `origins` or `gradients` vector
    :param n: size of the nxn grid.
    :param step: width/height of a cell in the grid
    :return: positions of origin vectors which are the vertices of a cell the point is in if `source` is `origins`;
     otherwise the values of the vectors.
    """
    x_num, y_num = get_cell_pos(point, n, step)

    result = np.array([source[y_num + 1, x_num],
                       source[y_num + 1, x_num + 1],
                       source[y_num, x_num + 1],
                       source[y_num, x_num],
                       ])

    return result


def plasma(colors: np.array):
    # Assume that 0 <= colors[i][j] <= 1 for all possible i and j
    rgb_colors = np.zeros((colors.shape[0], colors.shape[1], 3))

    grey_to_rgb = lambda r: colorsys.hsv_to_rgb(r, 1, 1)

    for i in range(colors.shape[0]):
        for j in range(colors.shape[1]):
            rgb_colors[i, j, :] = grey_to_rgb(colors[i, j])

    return rgb_colors
