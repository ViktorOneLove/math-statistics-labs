from calculation import *
import matplotlib.pyplot as plt


if __name__ == "__main__":

    begin = -1.8
    end = 2.0
    num = 20
    x = np.linspace(start=begin, stop=end, num=num, endpoint=True)
    y_ideal = ideal_model(x)
    for fun in [model, model_with_disturbance]:
        y_target = fun(x)
        b_0_lsm, b_1_lsm, y_founded_lsm = least_square_method(x, y_target)
        b_0_lmm, b_1_lmm, y_founded_lmm = least_modulus_method(x, y_target)
        print(f"b_0_lsm = {b_0_lsm} b_1_lsm = {b_1_lsm} b_0_lmm = {b_0_lmm} b_1_lmm = {b_1_lmm}")
        plt.plot(x, y_target, 'ko', mfc='none')
        plt.plot(x, y_ideal, 'r')
        plt.plot(x, y_founded_lsm, 'b')
        plt.plot(x, y_founded_lmm, 'g')
        plt.legend(('Выборка', 'Модель', 'МНК', 'МНМ'))
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.savefig(f"{fun.__name__}" + f".png")
        plt.show()

