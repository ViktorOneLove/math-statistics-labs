from distribution_characteristics import DistributionCharacteristics as dist
import scipy.stats as stats
import math as math
import numpy as np



def generate_table_latex(boudaries, n, p, np, n_minus_np, chi):
    latex_table = f"\\begin{{tabular}}{{| c | c | c | c | c | c | c |}} \\hline $i$ & $\\Delta_{{i}}$ " \
                  f"& $n_i$ & $p_i$ & $np_i$ & $n_{{i}} - np_i$ & $\\frac{{n_{{i}} - np_i}}{{np_i}}$ \\\\ \\hline"

    for i in range(len(n)):
        latex_table += f" {i+1} & $({boudaries[i].__round__(2)}, {boudaries[i+1].__round__(2)}]$ & " \
                       f"{n[i]} & {p[i].__round__(4)} & {np[i].__round__(2)} & {n_minus_np[i].__round__(2)} &" \
                       f"{chi[i].__round__(2)} \\\\ \\hline"

    latex_table += f" $\\sum$ & $-$ & {sum(n)} & {sum(p).__round__(4)} & {sum(np).__round__(2)} & " \
                   f"{sum(n_minus_np).__round__(2)} & {sum(chi).__round__(2)} = $\\chi_{{B}}^2$ \\\\ \\hline"
    latex_table += f" \\end{{tabular}}"

    return latex_table


def calculate_agreement_criterion(hypothetical_function, distribution, size):
    sample = distribution(which='rvs', _capacity=size)

    mu = np.mean(sample)
    sigma = np.std(sample)
    print(f"mu = {mu.__round__(2)} sigma = {sigma.__round__(2)}")

    number_of_intervals = math.ceil(1.72 * (size ** (1/3)))
    print(f"k = {number_of_intervals}")

    a = []
    center = distribution(which='ppf', _x=0.5)
    h = 2 * stats.iqr(sample) / size ** (1/3)

    a.append(-np.inf)
    for i in range(0, number_of_intervals - 1):
        a.append(center + h * (i - ((number_of_intervals - 1) / 2)))
    a.append(np.inf)

    p_i = np.zeros(number_of_intervals)
    n_i = np.zeros(number_of_intervals)
    np_i = np.zeros(number_of_intervals)
    n_i_minus_np_i = np.zeros(number_of_intervals)
    chi = np.zeros(number_of_intervals)
    for i in range(0, number_of_intervals):
        p_i[i] = hypothetical_function(which='cdf', _x=a[i+1], _loc=mu, _scale=sigma) - \
               hypothetical_function(which='cdf', _x=a[i], _loc=mu, _scale=sigma)
        n_i[i] = len([val for val in sample if a[i] < val <= a[i+1]])
        np_i[i] = size * p_i[i]
        n_i_minus_np_i[i] = n_i[i] - np_i[i]
        chi[i] = (n_i_minus_np_i[i]) ** 2 / np_i[i]


    return generate_table_latex(a, n_i, p_i, np_i, n_i_minus_np_i, chi)

