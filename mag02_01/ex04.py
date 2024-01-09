import numpy as np
import matplotlib.pyplot as plt


def mandelbrot_recursive(c, max_iter, current_iter=0, z=0):
    if current_iter == max_iter or abs(z) > 2:
        return current_iter

    z = z * z + c
    return mandelbrot_recursive(c, max_iter, current_iter + 1, z)


def mandelbrot_set_recursive(xmin, xmax, ymin, ymax, width, height, max_iter):
    x = np.linspace(xmin, xmax, width)
    y = np.linspace(ymin, ymax, height)
    img = np.empty((width, height))

    for i in range(width):
        for j in range(height):
            c = complex(x[i], y[j])
            img[i, j] = mandelbrot_recursive(c, max_iter)

    return img


xmin, xmax = -2.0, 1.0
ymin, ymax = -1.5, 1.5
width, height = 800, 800
max_iter = 256

img = mandelbrot_set_recursive(xmin, xmax, ymin, ymax, width, height, max_iter)

plt.imshow(img, extent=(xmin, xmax, ymin, ymax), cmap="jet")
plt.colorbar()
plt.title("Множина Мандельброта (рекурсивна побудова)")
plt.show()
