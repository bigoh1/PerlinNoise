import numpy as np


def scale(x, x0, x1, y0, y1):
    return (y0 * (x1 - x) + y1 * (x - x0)) / (x1 - x0)


def get_cell_pos(point: np.array, N, STEP):
    xnum = min(np.floor(point[0] / STEP), max(N - 1, 0))
    ynum = min(np.floor(point[1] / STEP), max(N - 1, 0))

    return int(xnum), int(ynum)


def get_origins(point: np.array, origins: np.array, N, STEP):
    xnum, ynum = get_cell_pos(point, N, STEP)

    # TODO think a though: if we access origins[x, y] or ...[y, x] is it any different?
    result = np.array([origins[ynum + 1, xnum],
                       origins[ynum + 1, xnum + 1],
                       origins[ynum, xnum + 1],
                       origins[ynum, xnum],
                       ])

    return result


# TODO: REFACTOR (see get_origins)
def get_gradients(point, gradients, N, STEP):
    xnum, ynum = get_cell_pos(point, N, STEP)

    result = np.array([gradients[ynum + 1, xnum],
                       gradients[ynum + 1, xnum + 1],
                       gradients[ynum, xnum + 1],
                       gradients[ynum, xnum]
                       ])
    return result