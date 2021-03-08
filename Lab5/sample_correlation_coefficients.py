import scipy.stats as stats
import numpy as np


class SampleCorrelationCoefficients:


    @staticmethod
    def pearson(sample):
        x = sample[:, 0]
        y = sample[:, 1]
        return stats.pearsonr(x, y)[0]


    @staticmethod
    def spearman(sample):
        x = sample[:, 0]
        y = sample[:, 1]
        return stats.spearmanr(x, y)[0]


    @staticmethod
    def quadrant(sample):
        x = sample[:, 0]
        y = sample[:, 1]

        size = len(x)

        x_new = x - np.median(x)
        y_new = y - np.median(y)

        n = [0, 0, 0, 0]
        for i in range(size):
            if x_new[i] > 0 and y_new[i] >= 0:
                n[0] += 1
            if x_new[i] <= 0 and y_new[i] > 0:
                n[1] += 1
            if x_new[i] < 0 and y_new[i] <= 0:
                n[2] += 1
            if x_new[i] >= 0 and y_new[i] < 0:
                n[3] += 1
        return ((n[0] + n[2]) - (n[1] + n[3])) / size
