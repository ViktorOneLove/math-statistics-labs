from distribution import Distribution
import matplotlib.pyplot as plt
from statsmodels.distributions.empirical_distribution import ECDF
import numpy as np
from scipy import stats


def draw_cdf(fun, capacity, plot_):
    plot_.set_title(fun['distribution'].__name__ + ' n=' + str(capacity))
    sample = fun['distribution'](which="rvs", capacity=capacity)
    ecdf = ECDF(sample)
    x = np.linspace(fun['a'], fun['b'])
    y_ecdf = ecdf(x)
    y_cdf = fun['distribution'](which="cdf", x=x)
    plot_.step(x, y_ecdf)
    plot_.plot(x, y_cdf)
    plt.savefig("cdf " + fun['distribution'].__name__ )


def draw_kde(fun, capacity, axs):
    def kde(samples, param):
        k = stats.gaussian_kde(samples, bw_method="silverman")
        k.set_bandwidth(k.factor*param)
        return k

    bandwidths = [0.5, 1.0, 2.0]
    for bandwidth, plot_ in zip(bandwidths, axs):
        plot_.set_title(fun['distribution'].__name__ + ' n=' + str(capacity))
        plot_.set_xlabel(f"h = h_n*{bandwidth}")
        sample = fun['distribution'](which="rvs", capacity=capacity)
        x = np.linspace(fun['a'], fun['b'])
        y = fun['distribution'](which="pdf", x=x)
        plot_.plot(x, y)

        kde_ = kde(samples=sample, param=bandwidth)
        y_kde = kde_.evaluate(x)
        plot_.plot(x, y_kde)
        plot_.set_ylim([0, 1])
        plot_.grid()

    plt.savefig("kde n = " + str(capacity) + " " + fun['distribution'].__name__)

if __name__ == '__main__':
    capacities = [20, 60, 100]
    for func in [
        {'distribution': Distribution.normal, 'a': -4, 'b': 4},
        {'distribution': Distribution.cauchy, 'a': -4, 'b': 4},
        {'distribution': Distribution.laplace, 'a': -4, 'b': 4},
        {'distribution': Distribution.poisson, 'a': 6, 'b': 14},
        {'distribution': Distribution.uniform, 'a': -4, 'b': 4}
    ]:
        fig, axs = plt.subplots(1, 3, figsize=(16, 6))
        for capacity, plot in zip(capacities, axs):
            draw_cdf(func, capacity, plot)

        for capacity in capacities:
            fig, axs = plt.subplots(1, 3, figsize=(16, 6))
            draw_kde(func, capacity, axs)

        # plt.show()
