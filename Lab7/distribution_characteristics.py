import scipy.stats as stats
import math as math

class DistributionCharacteristics:

    @staticmethod
    def normal(which, _capacity=None, _x=None, _loc=0, _scale=1):
        if which == "rvs":
            return stats.norm.rvs(loc=_loc, scale=_scale, size=_capacity)
        if which == "cdf":
            return stats.norm.cdf(x=_x, loc=_loc, scale=_scale)
        if which == "pdf":
            return stats.norm.pdf(x=_x, loc=_loc, scale=_scale)
        if which == "ppf":
            return stats.norm.ppf(q=_x, loc=_loc, scale=_scale)


    @staticmethod
    def laplace(which, _capacity=None, _x=None, _loc=0, _scale=math.sqrt(2)):
        if which == "rvs":
            return stats.laplace.rvs(loc=_loc, scale=_scale, size=_capacity)
        if which == "cdf":
            return stats.laplace.cdf(x=_x, loc=_loc, scale=_scale)
        if which == "pdf":
            return stats.laplace.pdf(x=_x, loc=_loc, scale=_scale)
        if which == "ppf":
            return stats.laplace.ppf(q=_x, loc=_loc, scale=_scale)


    @staticmethod
    def uniform(which, _capacity=None, _x=None, _loc=-math.sqrt(3), _scale=math.sqrt(3)):
        if which == "rvs":
            return stats.uniform.rvs(loc=_loc, scale=_scale, size=_capacity)
        if which == "cdf":
            return stats.uniform.cdf(x=_x, loc=_loc, scale=_scale)
        if which == "pdf":
            return stats.uniform.ppf(x=_x, loc=_loc, scale=_scale)
        if which == "ppf":
            return stats.uniform.ppf(q=_x, loc=_loc, scale=_scale)
