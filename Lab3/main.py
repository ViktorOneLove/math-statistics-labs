from distribution import Distribution
import matplotlib.pyplot as plt
import numpy as np

def draw_boxplot(distribution, size):
    fig, ax = plt.subplots()
    ax.boxplot(list(map(lambda x: distribution(x), size)), vert=False)
    ax.set_title(distribution.__name__)
    ax.set_yticklabels(list(map(str, size)))
    plt.savefig(distribution.__name__)


def emissions_proportion(distribution, size, averaging):
    res = []
    koeff = 1.5
    for each_size in size:
        data = []
        for i in range(averaging):
            sample = np.array(distribution(each_size))
            x1 = np.quantile(sample, 0.25) - koeff * ((np.quantile(sample, 0.75)) - (np.quantile(sample, 0.25)))
            x2 = np.quantile(sample, 0.75) + koeff * ((np.quantile(sample, 0.75)) - (np.quantile(sample, 0.25)))
            data.append(len(list(filter(lambda x: x < x1 or x > x2, sample))) / each_size)
        res.append((sum(data) / len(data)).__round__(2))
    return res


def print_emissions(distribution_name, size, emissions):
    latex_code = ""
    for i in range(len(size)):
        latex_code += f" {distribution_name} n = {size[i]} & {emissions[i]} \\\\ \\hline"
    return latex_code


if __name__ == "__main__":

    size = [20, 100]

    share_of_emissions_table_latex = f"\\begin{{tabular}}{{| c | c |}} \hline Sample & Share of emissions \\\\ \\hline"

    for dist in [
        Distribution.normal,
        Distribution.cauchy,
        Distribution.laplace,
        Distribution.poisson,
        Distribution.uniform
    ]:
        draw_boxplot(dist, size)
        emissions = emissions_proportion(dist, size, 1000)
        share_of_emissions_table_latex += print_emissions(dist.__name__, size, emissions)

    share_of_emissions_table_latex += f" \\end{{tabular}}"
    print(share_of_emissions_table_latex)
    plt.show()
