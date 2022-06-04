import numpy as np
import png
from utility import *
from params import N, STEP, RESOLUTION, OUTPUT_FILENAME

origins = get_origins(N, STEP)
gradients = get_gradients(N)

f = open(OUTPUT_FILENAME, 'wb')
w = png.Writer(RESOLUTION * N, RESOLUTION * N, greyscale=True)

colors = np.zeros((RESOLUTION * N, RESOLUTION * N))

for xi, x in enumerate(np.linspace(0, N*STEP, RESOLUTION * N)):
    for yi, y in enumerate(np.linspace(0, N*STEP, RESOLUTION * N)):
        point = np.array([x, y])

        # calculate differences btw origins and the point (point -> origin)
        curr_origins = near_vectors(point, origins, N, STEP)
        diffs = curr_origins - point

        dot = np.zeros(shape=(4, ))
        curr_gradients = near_vectors(point, gradients, N, STEP)
        for k in range(4):
            dot[k] = np.dot(curr_gradients[k], diffs[k])

        # calculate top interpolation
        point_x = point[0]
        top_y0, top_y1 = dot[0:2]
        top_x0, top_x1 = curr_origins[0:2, 0]
        top_int = cos_interpolate(point_x, top_x0, top_x1, top_y0, top_y1)


        # calculate bottom interpolation
        bottom_y0, bottom_y1 = dot[2:]
        bottom_x0, bottom_x1 = curr_origins[2:, 0]
        bottom_int = cos_interpolate(point_x, bottom_x0, bottom_x1, bottom_y0, bottom_y1)

        # calculate the third interpolation
        point_y = point[1]
        y0, y1 = top_int, bottom_int
        x0, x1 = curr_origins[0, 1], curr_origins[2, 1]
        final_int = cos_interpolate(point_y, x0, x1, y0, y1)

        # TODO: try swapping i and j
        colors[xi, yi] = final_int


# TODO: find a way to scaling the values to [0; 1] range inside the loop
min_colors, max_colors = np.amin(colors), np.amax(colors)
greyscale_min, greyscale_max = 0.0, 1.0
colors_scaled = np.uint8(scale(colors, min_colors, max_colors, greyscale_min, greyscale_max) * 255)

w.write(f, colors_scaled)
f.close()
