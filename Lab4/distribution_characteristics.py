import numpy as np
import scipy.stats as stats
import math
from scipy.special import factorial

class DistributionCharacteristics:

    @staticmethod
    def normal(which, capacity=None, x=None):
        if which == "rvs":
            return np.random.normal(0, 1, capacity)
        if which == "cdf":
            return stats.norm(0, 1).cdf(x)
        if which == "pdf":
            return 1 / np.sqrt(2 * np.pi) * np.exp(-x ** 2 / 2)

    @staticmethod
    def cauchy(which, capacity=None, x=None):
        if which == "rvs":
            return np.random.standard_cauchy(capacity)
        if which == "cdf":
            return stats.cauchy(loc=0, scale=1).cdf(x)
        if which == "pdf":
            return 1 / np.pi * 1 / (x ** 2 + 1)

    @staticmethod
    def laplace(which, capacity=None, x=None):
        if which == "rvs":
            return np.random.laplace(0, np.sqrt(2), capacity)
        if which == "cdf":
            return stats.laplace(loc=0, scale=1 / math.sqrt(2)).cdf(x)
        if which == "pdf":
            return 1 / np.sqrt(2) * np.exp(-np.sqrt(2) * np.abs(x))

    @staticmethod
    def poisson(which, capacity=None, x=None):
        if which == "rvs":
            return np.random.poisson(10, capacity)
        if which == "cdf":
            return stats.poisson(10).cdf(x)
        if which == "pdf":
            return np.power(10, x) / factorial(x) * np.exp(-10)

    @staticmethod
    def uniform(which, capacity=None, x=None):
        if which == "rvs":
            return np.random.uniform(-np.sqrt(3), np.sqrt(3), capacity)
        if which == "cdf":
            return stats.uniform(-math.sqrt(3), 2 * math.sqrt(3)).cdf(x)
        if which == "pdf":
            pdf = []
            for each_x in x:
                if math.fabs(each_x) <= math.sqrt(3):
                    pdf.append(1 / (2 * math.sqrt(3)))
                else:
                    pdf.append(0)
            return pdf
