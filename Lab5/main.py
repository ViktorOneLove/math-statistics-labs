import calc

if __name__ == "__main__":

    capacity = [20, 60, 100]
    correlation_coefficients = [0.0, 0.5, 0.9]
    repetitions = 1000

    for exp in [
        calc.bivariate_normal_distribution,
        calc.mixture_of_normal_distributions,
        calc.equiprobability_ellipse
    ]:
        exp(capacity)
