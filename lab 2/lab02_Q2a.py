"""
PHY407 teophile lemay and Charlie Hughes
Lab 2, question 2 a, part iii and part iv

this script contains an inneficient way of determining how many slices you need to get an error
of around 10^-9 while doing integrals using the trapezoidal rule and simpson's rule

timing of the integration functions was done in the python interface using timeit.timeit
e.g.
    timeit.timeit('int_simpson(0, 1, my_func, 2**4)', setup='from lab2_Q02a import int_simpson, my_func',  number=10000)/10000 
"""

import numpy as np

#define all the functions we will need
def my_func(x):
    """
    function to integrate: 4/(1 + x^2)
    """
    return 4 / (1 + x**2)

def int_trapezoidal(a, b, func, N):
    """
    function to calculate integrals of a given function over a given interval using the trapezoidal rule.
    
    :param a: start of interval of integration (float)
    :param b: end of interval of integration (should be larger than a) (float)
    :param func: function to integrate
    :param N: integer, number of slices of the interval to use.

    :return: calculated integral approximation
    """
    h = (b - a)/N
    sum = 0
    for k in range(1, N):
        sum += func(a + (k * h))
    return h * (func(a)/2 + func(b)/2 + sum)

def int_simpson(a, b, func, N):
    """
    this function calculates the integral of a given function over a given interval using simpson's rule

    :param a: start of interval of integration (float)
    :param b: end of interval of integration (should be larger than a) (float)
    :param func: function to integrate
    :param N: integer, number of slices of the interval to use (N must be even).

    :return: calculated integral approximation
    """
    h = (b - a)/N
    sum_Odd = 0
    sum_Even = 0
    for k in range(1, N, 2):
        sum_Odd += func(a + (k * h))
    for j in range(2, N, 2):
        sum_Even += func(a + (j * h))
    return (h/3) * (func(a) + func(b) + 4*sum_Odd + 2*sum_Even)


def err(x, y):
    """
    this function calculates the relative error between x (given value) and y (true value)
    """
    return (x-y)



if __name__ == '__main__':
    #lines below can be uncommented to run the script on it's own and calculate integrals
    #these lines do the work necessary for Q2 (a) part iii
    # trap = int_trapezoidal(0, 1, my_func, 2**12)
    # print('trapezoidal:')
    # print('value:')
    # print(trap)
    # print('error:')
    # print(err(trap, np.pi))
    # print()
    # print('simpson')
    # simp = int_simpson(0, 1, my_func, 2**4)
    # print('value:')
    # print(simp)
    # print('error:')
    # print(err(simp, np.pi))

    #the lines below do the work for Q2 (a) part iv
    I1 = int_trapezoidal(0, 1, my_func, 16)
    I2 = int_trapezoidal(0, 1, my_func, 32)
    approx_err = (I2 - I1)/3
    print(approx_err)
