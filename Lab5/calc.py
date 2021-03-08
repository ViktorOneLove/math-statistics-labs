import numpy as np
import scipy.stats as stats
import statistics
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
from sample_correlation_coefficients  import SampleCorrelationCoefficients as scc



def bivariate_normal_distribution(capacities):
    correlation_coefficients = [0.0, 0.5, 0.9]
    repetitions = 1000

    for capacity in capacities:

        tabel_in_latex = f"\\begin{{tabular}}{{| c | c | c | c |}} \hline"

        for cor_cov in correlation_coefficients:
            tabel_in_latex += f" p = {cor_cov} & $r$ & $r_{{S}}$ & $r_{{Q}}$ \\\\ \\hline"

            data = []
            for _ in range(repetitions):
                sample = stats.multivariate_normal.rvs([0, 0], [[1, cor_cov], [cor_cov, 1]], capacity)
                data += [[c_cor(sample) for c_cor in [scc.pearson, scc.spearman, scc.quadrant]]]
            data = np.array(data).T
            res = [list(map(lambda x: x.__round__(3), [
                np.mean(data[i]),
                np.mean(list(map(lambda x: x ** 2, data[i]))),
                statistics.variance(data[i])])) for i in range(3)]

            for cor_coeff_characteristics in range(len(res[0])):
                if cor_coeff_characteristics == 0:
                    tabel_in_latex += f" $E(z)$"
                elif cor_coeff_characteristics == 1:
                    tabel_in_latex += f" $E(z^2)$"
                elif cor_coeff_characteristics == 2:
                    tabel_in_latex += f" $D(z)$"

                for cor_coeff in res:
                    tabel_in_latex += f" & {cor_coeff[cor_coeff_characteristics]}"

                tabel_in_latex += f" \\\\ \\hline"

        tabel_in_latex += f" \\end{{tabular}}"
        print(tabel_in_latex)


def mixture_of_normal_distributions(capacities):
    repetitions = 1000

    tabel_in_latex = f"\\begin{{tabular}}{{| c | c | c | c |}} \hline"

    for capacity in capacities:
        data = []
        for _ in range(repetitions):
            sample = 0.9 * stats.multivariate_normal.rvs([0, 0], [[1, 0.9], [0.9, 1]], capacity) + \
                     0.1 * stats.multivariate_normal.rvs([0, 0], [[10, -0.9], [-0.9, 10]], capacity)
            data += [[c_cor(sample) for c_cor in [scc.pearson, scc.spearman, scc.quadrant]]]
        data = np.array(data)
        res = [list(map(lambda x: x.__round__(3), [
            np.mean(data[i]),
            np.mean(list(map(lambda x: x ** 2, data[i]))),
            statistics.variance(data[i])])) for i in range(3)]

        tabel_in_latex += f" n = {capacity} & $r$ & $r_{{S}}$ & $r_{{Q}}$ \\\\ \\hline"

        for cor_coeff_characteristics in range(len(res[0])):
            if cor_coeff_characteristics == 0:
                tabel_in_latex += f" $E(z)$"
            elif cor_coeff_characteristics == 1:
                tabel_in_latex += f" $E(z^2)$"
            elif cor_coeff_characteristics == 2:
                tabel_in_latex += f" $D(z)$"

            for cor_coeff in res:
                tabel_in_latex += f" & {cor_coeff[cor_coeff_characteristics]}"

            tabel_in_latex += f" \\\\ \\hline"

    tabel_in_latex += f" \\end{{tabular}}"

    print(tabel_in_latex)


def equiprobability_ellipse(capacities):
    for capacity in capacities:
        _, sp = plt.subplots(1, 3, figsize=(16, 6))
        for cor_cov, subplot in zip([0, 0.5, 0.9], sp):
            sample = stats.multivariate_normal.rvs([0, 0], [[1, cor_cov], [cor_cov, 1]], capacity)
            x = sample[:, 0]
            y = sample[:, 1]
            vx = statistics.variance(x)
            vy = statistics.variance(y)
            angle = np.arctan(2 * np.sqrt(vx) * np.sqrt(vy) * cor_cov / (vx - vy)) / 2
            w = 5 * np.sqrt(vx * (np.cos(angle)) ** 2 + cor_cov * np.sqrt(vx) * np.sqrt(vy) * np.sin(2 * angle) + vy * (
                np.sin(angle)) ** 2)
            h = 5 * np.sqrt(vx * (np.sin(angle)) ** 2 - cor_cov * np.sqrt(vx) * np.sqrt(vy) * np.sin(2 * angle) + vy * (
                np.cos(angle)) ** 2)
            ell = Ellipse(xy=(np.mean(x), np.mean(y)), width=w, height=h,
                          angle=np.rad2deg(angle), fill=False)

            subplot.scatter(x, y)
            subplot.add_patch(ell)

            title = f"n = {capacity} rho = {cor_cov}"

            subplot.set_title(title)
            subplot.set_xlabel("X")
            subplot.set_ylabel("Y")

        plt.savefig(f"{capacity}" + f".png")

