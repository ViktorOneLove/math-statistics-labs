import numpy as np
import math as math


class PositionCharacteristics:

    @staticmethod
    def sample_mean(arr):
        return sum(arr) / len(arr)

    @staticmethod
    def sample_median(arr):
        return arr[len(arr) // 2] if len(arr) % 2 == 1 else (arr[len(arr) // 2 - 1] + arr[len(arr) // 2]) /2

    @staticmethod
    def half_sum(arr):
        return (arr[0] + arr[-1]) / 2

    @staticmethod
    def quartile_half_sum(arr):
        return (np.quantile(arr, 1 / 4) + np.quantile(arr, 3 / 4)) / 2

    @staticmethod
    def truncated_mean(arr):
        n = len(arr)
        r = n // 4
        return sum(arr[r : n - r - 1]) / (n - 2 * r)

    @staticmethod
    def dispersion(arr):
        mean = PositionCharacteristics.sample_mean(arr)
        return sum(list(map(lambda x: (x-mean)**2, arr))) / len(arr)

    @staticmethod
    def correct_digits(vrnc: float):
        return max(0, round(-math.log10(abs(vrnc))))

    @staticmethod
    def variance(values):
        values = np.array(values)
        mean = PositionCharacteristics.sample_mean(values)
        return PositionCharacteristics.sample_mean(values * values) - mean * mean