import numpy as np
import matplotlib.pyplot as plt


def mandelbrot(c, max_iter):
    z = c
    for n in range(max_iter):
        if abs(z) > 2:
            return n
        z = z * z + c
    return max_iter


def mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            img[i, j] = mandelbrot(complex(x[i], y[j]), max_iter)

    return img


xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
width, height = 800, 800
max_iter = 256

img = mandelbrot_set(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.imshow(img, extent=(xmin, xmax, ymin, ymax), cmap="jet")
plt.colorbar()
plt.title("Множина Мандельброта")
plt.show()
