from distribution import Distribution
from data_position_characteristics import PositionCharacteristics


if __name__ == '__main__':

    for dist in [
        Distribution.normal,
        Distribution.cauchy,
        Distribution.laplace,
        Distribution.poisson,
        Distribution.uniform
    ]:
        latex_table_code = f"\\begin{{tabular}}{{|c | c | c | c | c | c|}} \hline \multicolumn{{6}}{{|c|}}{{{dist.__name__}}} \\\\"
        latex_table_code += f" \\hline & $\\bar{{x}}$ & $medx$ & $z_R$ & $z_Q$ & $z_{{tr}}$ "
        for size in [10, 100, 1000]:
            latex_table_code += f" \\\\ \\hline $n={size}$ & & & & & \\\\"
            mean = []
            dispersion = []
            for data_pos in [
                PositionCharacteristics.sample_mean,
                PositionCharacteristics.sample_median,
                PositionCharacteristics.half_sum,
                PositionCharacteristics.quartile_half_sum,
                PositionCharacteristics.truncated_mean
            ]:
                data = [data_pos(sorted(dist(size))) for i in range(1000)]
                mean.append(round(PositionCharacteristics.sample_mean(data),
                                  PositionCharacteristics.correct_digits(PositionCharacteristics.variance(data))))
                # mean.append(PositionCharacteristics.sample_mean(data))
                dispersion.append(PositionCharacteristics.dispersion(data))

            latex_table_code += f" \\hline $E(z)$"
            for elem in mean:
                latex_table_code += f" &{round(elem, 6)}"
            latex_table_code += f" \\\\"
            latex_table_code += f" \\hline $D(z)$"
            for elem in dispersion:
                latex_table_code += f" &{elem.__round__(6)}"
        latex_table_code += f" \\\\ \\hline \end{{tabular}}"
        print(latex_table_code)

