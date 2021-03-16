from distribution import Distribution as dist
import numpy as np


def ideal_model(x):
    return 2 + 2 * x


def model(x):
    return 2 + 2 * x + dist.normal(20)


def model_with_disturbance(x):
    y = 2 + 2 * x + dist.normal(20)
    y[0] += 10
    y[19] -= 10
    return y


def least_square_method(x, y):
    x_mean = np.mean(x)
    x_square_mean = np.mean(list(map(lambda t: t ** 2, x)))
    xy_mean = np.mean(x * y)
    y_mean = np.mean(y)

    b_1 = (xy_mean - x_mean * y_mean) / (x_square_mean - x_mean ** 2)
    b_0 = y_mean - x_mean * b_1

    return b_0, b_1, b_0 + b_1 * x


def least_modulus_method(x, y):
    n = len(x)

    r_Q = np.mean(np.sign(x - np.median(x)) * np.sign(y - np.median(y)))

    l_index = n // 4 + 1 if n % 4 != 0 else n // 4
    j_index = n - l_index + 1

    q_y = (y[j_index] - y[l_index])
    q_x = (x[j_index] - x[l_index])

    k_Q = x[j_index] - x[l_index]

    b_1 = r_Q * q_y / q_x
    b_0 = np.median(y) - b_1 * np.median(x)

    return b_0, b_1, b_0 + b_1 * x