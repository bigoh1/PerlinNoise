def scale(x, x0, x1, y0, y1):
    return (y0 * (x1 - x) + y1 * (x - x0)) / (x1 - x0)
