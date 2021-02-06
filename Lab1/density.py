import math
import numpy as np
from scipy.special import factorial


class Density:

    @staticmethod
    def normal(x):
        return 1 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2)

    @staticmethod
    def cauchy(x):
        return 1 / np.pi * 1 / (x ** 2 + 1)

    @staticmethod
    def laplace(x):
        return 1 / np.sqrt(2) * np.exp(-np.sqrt(2) * np.abs(x))

    @staticmethod
    def poisson(x):
        return np.power(10, x) / factorial(x) * np.exp(-10)

    @staticmethod
    def uniform(x):
        pdf = []
        for each_x in x:
            if math.fabs(each_x) <= math.sqrt(3):
                pdf.append(1 / (2 * math.sqrt(3)))
            else:
                pdf.append(0)
        return pdf
