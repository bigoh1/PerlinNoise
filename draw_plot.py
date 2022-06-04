import matplotlib.pyplot as plt
import numpy as np


def draw(N, STEP):
    LIM = [-1, N * STEP+1]

    fig = plt.figure()
    ax = fig.add_subplot(1, 1, 1)

    # Major ticks every 20, minor ticks every 5
    major_ticks = np.arange(LIM[0], LIM[1], STEP)
    minor_ticks = np.arange(LIM[0], LIM[1], 1)

    ax.set_xticks(major_ticks)
    ax.set_xticks(minor_ticks, minor=True)
    ax.set_yticks(major_ticks)
    ax.set_yticks(minor_ticks, minor=True)

    ax.grid(which='both')

    # Or if you want different settings for the grids:
    ax.grid(which='minor', alpha=0.2)
    ax.grid(which='major', alpha=0.5)
    plt.xlim(LIM)
    plt.ylim(LIM)

    return fig, ax
