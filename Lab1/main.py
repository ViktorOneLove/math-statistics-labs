import matplotlib.pyplot as plt
import numpy as np
from distribution import Distribution
from density import Density


def plot_hist_with_density(func, size, density_smoothness=100, bins=20):
    fig_num = len(size)
    fig, ax = plt.subplots(1, fig_num, figsize=(12, 6))
    plt.subplots_adjust(wspace=0.4)

    distribution_name = func['distribution'].__name__

    plt.suptitle(distribution_name + " distribution")
    for i in range(fig_num):
        distribution = func['distribution'](size[i])
        density_x = np.linspace(min(distribution), max(distribution), density_smoothness)
        density_y = func['density'](density_x)

        ax[i].hist(distribution, density=True, histtype='stepfilled', facecolor='grey',
                   edgecolor='black', alpha=0.5, bins=bins)
        ax[i].plot(density_x, density_y, color='b', linewidth=1)
        ax[i].set_title(f'n = {size[i]}')
        ax[i].set_ylabel("density")
    plt.savefig(distribution_name + ".png")



if __name__ == '__main__':
    size = [10, 50, 1000]
    for func in [
        {'distribution': Distribution.normal, 'density': Density.normal},
        {'distribution': Distribution.cauchy, 'density': Density.cauchy},
        {'distribution': Distribution.laplace, 'density': Density.laplace},
        {'distribution': Distribution.poisson, 'density': Density.poisson},
        {'distribution': Distribution.uniform, 'density': Density.uniform}
    ]:
        plot_hist_with_density(func, size)

    plt.show()
