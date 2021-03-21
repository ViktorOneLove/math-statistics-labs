from distribution_characteristics import DistributionCharacteristics as dist
from research import *

if __name__ == "__main__":

    sizes = [100, 20, 20]
    hypothetical_functions = [dist.normal]
    distributions = [dist.normal, dist.laplace, dist.uniform]

    for hypothetical_function in hypothetical_functions:
        for dist, size in zip(distributions, sizes):
            latex_table = calculate_agreement_criterion(hypothetical_function, dist, size)
            print(latex_table)




