import numpy as np
import scipy.integrate as integrate

from view import func, a, b, y_min, y_max


def monte_carlo_integrate(func, a, b, y_min, y_max, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(y_min, y_max, num_points)
    under_curve = np.sum(y < func(x))
    print(under_curve)
    area = (b - a) * (y_max - y_min) * (under_curve / num_points)
    return area


if __name__ == "__main__":
    result, err = integrate.quad(func, a, b)  # noqa
    mc_result = monte_carlo_integrate(func, a, b, y_min, y_max, 1_000_000)
    print(result, mc_result)
