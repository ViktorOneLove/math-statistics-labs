import numpy as np
import scipy.stats as stats
import math
from scipy.special import factorial

class Distribution:

    @staticmethod
    def normal(which, capacity=None, x=None):
        if which == "rvs":
            return stats.norm(0, 1).rvs(capacity)
        if which == "cdf":
            return stats.norm(0, 1).cdf(x)
        if which == "pdf":
            return stats.norm(0, 1).pdf(x)

    @staticmethod
    def cauchy(which, capacity=None, x=None):
        if which == "rvs":
            return stats.cauchy(loc=0, scale=1).rvs(capacity)
        if which == "cdf":
            return stats.cauchy(loc=0, scale=1).cdf(x)
        if which == "pdf":
            return stats.cauchy(loc=0, scale=1).pdf(x)

    @staticmethod
    def laplace(which, capacity=None, x=None):
        if which == "rvs":
            return stats.laplace(loc=0, scale=1 / math.sqrt(2)).rvs(capacity)
        if which == "cdf":
            return stats.laplace(loc=0, scale=1 / math.sqrt(2)).cdf(x)
        if which == "pdf":
            return stats.laplace(loc=0, scale=1 / math.sqrt(2)).pdf(x)

    @staticmethod
    def poisson(which, capacity=None, x=None):
        if which == "rvs":
            return stats.poisson(10).rvs(capacity)
        if which == "cdf":
            return stats.poisson(10).cdf(x)
        if which == "pdf":
            return np.power(10, x) / factorial(x) * np.exp(-10)

    @staticmethod
    def uniform(which, capacity=None, x=None):
        if which == "rvs":
            return stats.uniform(-math.sqrt(3), 2 * math.sqrt(3)).rvs(capacity)
        if which == "cdf":
            return stats.uniform(-math.sqrt(3), 2 * math.sqrt(3)).cdf(x)
        if which == "pdf":
            return stats.uniform(-math.sqrt(3), 2 * math.sqrt(3)).pdf(x)
