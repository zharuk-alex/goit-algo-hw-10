import numpy as np
import scipy.integrate as integrate

from task_2_view import f, a, b


def monte_carlo_integrate(func, a, b, num_points):
    x = np.random.uniform(a, b, num_points)
    y = np.random.uniform(0, func(b), num_points)
    under_curve = y < func(x)
    area = under_curve.sum() / num_points * (b - a) * func(b)
    return area


if __name__ == "__main__":
    quad_result, err = integrate.quad(f, a, b)
    mc_result = monte_carlo_integrate(f, a, b, 100_000_000)
    print(quad_result, mc_result)
