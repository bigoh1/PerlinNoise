# Number of cells in NxN grid
# Contributes to the size of the output image (image size ~ N * RESOLUTION)
N = 10

# width/length of those cells
STEP = 4

# number of pixels on the line [i * STEP; (i + 1) * STEP) for i=0,1,...,N-1
# note, that the total number of pixels inside a cell is `RESOLUTION` ^ 2
# the larger the value the bigger the output image size AND its quality
RESOLUTION = 30

# path to the file where the result is saved
OUTPUT_FILENAME = "out.png"

# turn on to see plasma effect
GREYSCALE = False
