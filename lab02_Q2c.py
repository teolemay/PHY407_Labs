"""
PHY407 lab 2 question 2 (c)

teophile lemay

this script makes a 3d surface plot of the solution to the wave equation on a circular membrane

N.B. since we are plotting at t=0, we can ignore the las cos(c*z_mn *t / a) because cos(0) = 1
"""

import numpy as np
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
    this function defines the integrand of an nth order Bessel function of the first kind
    ***this version of the function is modified to include z_3,2 = 11.620 in the argument for x***

    :param n: int, order of the bessel function of the first kind
    :param x: float, x value for bessel function 
    :param phi: float, value of phi (restricted to [0, pi])

    :return: calculated value of the integrand of the bessel function at given x, and phi
    """
    return np.cos(n*phi - 11.620*x*np.sin(phi))

def polar_to_xy(r, theta):
    """
    this function converts 2d polar coordinates to x, y coordinates. it is helpful for plotting

    :param r: radius (float)
    :param theta: angle in radians (float)
    """
    x = r*np.cos(theta)
    y = r*np.sin(theta)
    return x, y

#define some constants
n=2
N=1000 #N=1000 was as good as scipy.special.jv, so it should work here.

#create the area
x_vals = np.linspace(-1.2, 1.2, 1000) #work in units of r/R
y_vals = np.linspace(-1.2, 1.2, 1000)
x, y = np.meshgrid(x_vals, y_vals)
R = np.sqrt(x**2 + y**2)
theta = np.arctan(y/x)

print('\nfinished preparing, calculating u\n')

u_vals = (int_simpson_for_bessel(0, np.pi, bessel_integrand, N, n, R) / np.pi) * np.cos(n*theta)
u_vals[R > 1] = 0

print('\nfinished calculating u, plotting now\n')

#need 2d array to describe variations in both r/R and theta
# u_vals = np.zeros(x.shape, y.shape.shape)

# for i, x in enumerate(x):
#     for j, y  in enumerate(y):
#         R = np.sqrt(x**2 + y**2)
#         u_vals[i, j] = (int_simpson_for_bessel(0, np.pi, bessel_integrand, N, n, r) / np.pi) * np.cos(n*theta)


fig = plt.figure()
ax = fig.add_subplot(projection='3d')
surface = ax.plot_surface(x, y, u_vals, cmap='coolwarm')
fig.colorbar(surface, shrink=0.75)
plt.show()
print('finished plotting')