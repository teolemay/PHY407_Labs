"""
PHY407 Lab 2 question 2 (b)
Teophile Lemay and Charlie Hughes

This script calculates integrals of bessel functions of the first kind (J_n (x))
"""
import numpy as np
from scipy.special import jv
import matplotlib.pyplot as plt

def int_simpson_for_bessel(a, b, func, N, func_n, func_x):
    """
    this function calculates the integral of a given function over a given interval using simpson's rule
    the function has been adapted to accomodate multiparameter functions, in particular a bessel function of
    the first kind. since the integration variable is phi, we also add the n (order) and x terms.

    :param a: start of interval of integration (float)
    :param b: end of interval of integration (should be larger than a) (float)
    :param func: function to integrate
    :param N: integer, number of slices of the interval to use.
    :param func_x: float, x value for  bessel integrand
    :param func_n: int, order of bessel function of first kind.

    :return: calculated integral approximation
    """
    h = (b - a)/N
    sum_Odd = 0
    sum_Even = 0
    for k in range(1, N, 2):
        sum_Odd += func((a + (k * h)), func_n, func_x)
    for j in range(2, N, 2):
        sum_Even += func((a + (j * h)), func_n, func_x)
    return (h/3) * (func(a, func_n, func_x) + func(b, func_n, func_x) + 4*sum_Odd + 2*sum_Even)

def bessel_integrand(phi, n, x):
    """
    this function defines the integrand of an nth order Bessel function of the first kind at x

    :param n: int, order of the bessel function of the first kind
    :param x: float, x value for bessel function 
    :param phi: float, value of phi (restricted to [0, pi])

    :return: calculated value of the integrand of the bessel function at given x, and phi
    """
    return np.cos(n*phi - x*np.sin(phi))

x_vals = np.arange(0, 20, 0.1)
N=1000

#calculate values for n=0 first kind of bessel function
n=0
y_vals0 = np.zeros_like((x_vals))
for i, x in enumerate(x_vals):
    y_vals0[i] = int_simpson_for_bessel(0, np.pi, bessel_integrand, N, n, x) / np.pi

#calculate values for n=3 first kind of bessel function
n=3
y_vals3 = np.zeros_like((x_vals))
for i, x in enumerate(x_vals):
    y_vals3[i] = int_simpson_for_bessel(0, np.pi, bessel_integrand, N, n, x) / np.pi

#calculate values for n=5 first kind of bessel function
n=5
y_vals5 = np.zeros_like((x_vals))
for i, x in enumerate(x_vals):
    y_vals5[i] = int_simpson_for_bessel(0, np.pi, bessel_integrand, N, n, x) / np.pi

#calculate bessel functions using scipy.special.jv
scipy_vals0 = np.zeros_like(x_vals)
for i, x in enumerate(x_vals):
    scipy_vals0[i] = jv(0, x)

scipy_vals3 = np.zeros_like(x_vals)
for i, x in enumerate(x_vals):
    scipy_vals3[i] = jv(3, x)

scipy_vals5 = np.zeros_like(x_vals)
for i, x in enumerate(x_vals):
    scipy_vals5[i] = jv(5, x)

#plot everything together
plt.figure()
plt.plot(x_vals, y_vals0, label='Simpson (n=0)')
plt.plot(x_vals, y_vals3, label='Simpson (n=3)')
plt.plot(x_vals, y_vals5, label='Simpson (n=5)')
#the three plot commands below would be commented out in order to plot only the simpson's rule results
plt.plot(x_vals, scipy_vals0, label='scipy (n=0)')
plt.plot(x_vals, scipy_vals3, label='scipy (n=3)')
plt.plot(x_vals, scipy_vals5, label='scipy (n=5)')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')
plt.title('Bessel functions of the first kind for different orders n')

plt.show()

#calculate differences between my approximations and scipy.special.jv
difference0 = np.max(np.abs(y_vals0 - scipy_vals0))
difference3 = np.max(np.abs(y_vals3 - scipy_vals3))
difference5 = np.max(np.abs(y_vals5 - scipy_vals5))
print('0:', difference0)
print('3:', difference3)
print('5:', difference5)

