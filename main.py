import numpy as np
import matplotlib.pyplot as plt
import png


from draw_plot import draw
from constants import *
from utility import *

fix, ax = draw(N, STEP)

rand_ind = np.random.randint(possible_gradients.shape[0], size=4)

# [top-left, top-right, bottom-right, bottom-left]
gradients = possible_gradients[rand_ind, :]

RESOLUTION = 100
f = open('out.png', 'wb')               # binary mode is important
w = png.Writer(RESOLUTION, RESOLUTION, greyscale=True)

colors = np.zeros((RESOLUTION, RESOLUTION))

for xi, x in enumerate(np.linspace(0, 4, RESOLUTION)):
    for yi, y in enumerate(np.linspace(0, 4, RESOLUTION)):
        point = np.array([x, y])

        # calculate differences btw origins and the point (point -> origin)
        diffs = origins - point

        dot = np.zeros((gradients.shape[0], 1))
        for i in range(gradients.shape[0]):
            dot[i] = np.dot(gradients[i], diffs[i])

        # calculate top interpolation
        point_x = point[0]
        top_y0, top_y1 = dot[0:2]
        # top_yrange = top_y1 - top_y0

        top_x0, top_x1 = origins[0:2, 0]
        top_int = (top_y0 * (top_x1 - point_x) + top_y1 * (point_x - top_x0)) / (top_x1 - top_x0)

        # calculate bottom interpolation
        bottom_y0, bottom_y1 = dot[2:]
        # bottom_yrange = bottom_y1 - bottom_y0

        bottom_x0, bottom_x1 = origins[2:, 0]
        bottom_int = (bottom_y0 * (bottom_x1 - point_x) + bottom_y1 * (point_x - bottom_x0)) / (bottom_x1 - bottom_x0)

        # calculate the third interpolation
        point_y = point[1]
        y0, y1 = top_int, bottom_int
        # final_range = y1 - y0

        x0, x1 = origins[0, 1], origins[2, 1]
        final_int = (y0 * (x1 - point_y) + y1 * (point_y - x0)) / (x1 - x0)

        colors[xi, yi] = final_int


min_colors, max_colors = np.amin(colors), np.amax(colors)
greyscale_min, greyscale_max = 0.0, 1.0
colors_scaled = np.uint8(scale(colors, min_colors, max_colors, greyscale_min, greyscale_max) * 255)

print(gradients)

# for xi, x in enumerate(np.linspace(0, 4, RESOLUTION)):
#     for yi, y in enumerate(np.linspace(0, 4, RESOLUTION)):
#         plt.scatter(x, y, color=str(colors_scaled[xi, yi]))
#         print(x, y)

plt.quiver(origins[:, 0], origins[:, 1], gradients[:, 0], gradients[:, 1], color=['r','b','g'], angles='xy', scale_units='xy', scale=1)

print(colors_scaled.flatten())
w.write(f, colors_scaled)
f.close()


plt.show()
