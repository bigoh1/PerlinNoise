import numpy as np
import matplotlib.pyplot as plt
import png


from draw_plot import draw
from constants import *
from utility import *

STEP = 4
N = 10
RESOLUTION = 30

# possible_gradients = np.array([
#     [1, 1],
#     [-1, 1],
#     [-1, -1],
#     [1, -1],
# ])

possible_gradients = np.array([(np.cos(r), np.sin(r)) for r in np.linspace(0, 2*np.pi, 100)])

origins = np.array([[(STEP * i, STEP * j) for i in range(N+1)] for j in range(N+1)])

rand_ind = np.random.randint(possible_gradients.shape[0], size=((N+1) ** 2))
gradients = possible_gradients[rand_ind, :].reshape((N+1, N+1, 2))


fix, ax = draw(N, STEP)


f = open('out.png', 'wb')               # binary mode is important
w = png.Writer(RESOLUTION * N, RESOLUTION * N, greyscale=True)

colors = np.zeros((RESOLUTION * N , RESOLUTION * N))

# gradient_ind = 0
# for i in range(0, N * STEP, STEP):
#     for j in range(0, N * STEP, STEP):
#         for xi, x in enumerate(np.linspace(i, i+STEP, RESOLUTION)):
#             for yi, y in enumerate(np.linspace(j, j+STEP, RESOLUTION)):
for xi, x in enumerate(np.linspace(0, N*STEP, RESOLUTION * N)):
    for yi, y in enumerate(np.linspace(0, N*STEP, RESOLUTION * N)):
            point = np.array([x, y])

            # calculate differences btw origins and the point (point -> origin)
            curr_origins = get_origins(point, origins, N, STEP)
            diffs = curr_origins - point

            dot = np.zeros(shape=(4, ))
            curr_gradients = get_gradients(point, gradients, N, STEP)
            for k in range(4):
                dot[k] = np.dot(curr_gradients[k], diffs[k])

            # calculate top interpolation
            point_x = point[0]
            top_y0, top_y1 = dot[0:2]
            # top_yrange = top_y1 - top_y0

            top_x0, top_x1 = curr_origins[0:2, 0]
            # top_int = (top_y0 * (top_x1 - (point_x - top_x0)) + top_y1 * ((point_x - top_x0) - top_x0)) / (top_x1 - top_x0)
            # top_int = (top_y0 * (top_x1 - point_x) + top_y1 * (point_x - top_x0)) / (
            #             top_x1 - top_x0)
            top_int = cos_interpolate(point_x, top_x0, top_x1, top_y0, top_y1)


            # calculate bottom interpolation
            bottom_y0, bottom_y1 = dot[2:]

            # bottom_yrange = bottom_y1 - bottom_y0

            bottom_x0, bottom_x1 = curr_origins[2:, 0]
            # bottom_int = (bottom_y0 * (bottom_x1 - (point_x-bottom_x0)) + bottom_y1 * ((point_x - bottom_x0) - bottom_x0)) / (bottom_x1 - bottom_x0)
            # bottom_int = (bottom_y0 * (bottom_x1 - point_x) + bottom_y1 * (
            #             point_x - bottom_x0)) / (bottom_x1 - bottom_x0)
            bottom_int = cos_interpolate(point_x, bottom_x0, bottom_x1, bottom_y0, bottom_y1)

            # calculate the third interpolation
            point_y = point[1]
            y0, y1 = top_int, bottom_int
            # final_range = y1 - y0

            x0, x1 = curr_origins[0, 1], curr_origins[2, 1]
            # final_int = (y0 * (x1 - (point_y-x1)) + y1 * ((point_y-x1) - x0)) / (x1 - x0)
            # final_int = (y0 * (x1 - point_y) + y1 * (point_y - x0)) / (x1 - x0)
            final_int = cos_interpolate(point_y, x0, x1, y0, y1)

            # TODO: try swapping i and j
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

print(colors_scaled.shape)
w.write(f, colors_scaled)
f.close()


plt.show()
