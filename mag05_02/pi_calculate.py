import os
from concurrent.futures import ProcessPoolExecutor, ThreadPoolExecutor

import matplotlib.pyplot as plt
import numpy as np

nums = 10_000


def estimate_pi(n, view_=False):

    x = np.random.uniform(-1, 1, n)
    y = np.random.uniform(-1, 1, n)
    inside_circle = x ** 2 + y ** 2 <= 1
    pi_estimate = 4 * np.sum(inside_circle) / n
    if view_:
        plt.figure(figsize=(8, 8))
        plt.scatter(x[inside_circle], y[inside_circle], color="blue", s=1)
        plt.scatter(x[~inside_circle], y[~inside_circle], color="red", s=1)
        plt.axis("equal")
        plt.show()
    return pi_estimate


def main():
    num_for_process = 1_000_000
    with ProcessPoolExecutor() as executor:
        futures = [executor.submit(estimate_pi, num_for_process) for _ in range(1000)]  # noqa
        pi_estimates = [future.result() for future in futures]
        pi = np.mean(pi_estimates)
        print(pi)


if __name__ == "__main__":
    # pi = estimate_pi(nums, True)
    # print(pi)
    print(os.cpu_count())
    main()

