"""
Phy 407 Lab 2 question 3

Charlie Hughes and Teophile Lemay

This code calculates V(r, z) using Simpson's rule integration and compares it to the known analytical solution
"""

import numpy as np
import scipy.integrate as integrate
import matplotlib.pyplot as plt
from scipy.special import k0 #Bessel's fnc

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


#Parameters
Q = 10**-13 #C
l = 1 #mm
E = 8.8541878176 * 10**-12 / 1000 #F/mm
r = 0.25 #mm
z = 0 #mm
n = 50 #Number of slices (8 by default, 50 gets to ~1 in 1 million offset)

def electro_pot(u): #function to be integrated (lab 2 exercise sheet, eq. 8)
    return (Q * np.exp(-(np.tan(u))**2)) / (4*np.pi*E*(np.cos(u)**2)*np.sqrt((z-l*np.tan(u))**2+r**2))

def electro_pot_true(): #analytical solution (lab 2 exercise sheet, eq. 9)
    return (Q/(4*np.pi*E*l))*(np.exp((r**2)/(2*l**2)))*k0((r**2)/(2*l**2))


result = []
result_analytical = []
for i in np.linspace(0.25,5,10): #Reasonable range of r values
    r = i
    #run calculation with both methods (simpson's and analytical)
    result.append(int_simpson(-np.pi/2, np.pi/2, electro_pot, n)) #Use my simpson function
    result_analytical.append(electro_pot_true())

#First plot of numerical integration vs analytical functions across r values
plt.plot(np.linspace(0.25,5,10), result, label='Integration')
plt.plot(np.linspace(0.25,5,10), result_analytical, label='Analytical')
plt.legend()
plt.xlabel("Radius / mm")
plt.ylabel("Potiential Difference / V")
plt.title("Electrostatic Potential for a Line of Charge")
plt.show()

#Second plot comparing difference between two functions
plt.stem(np.linspace(0.25,5,10), abs(np.array(result_analytical) - np.array(result)), label="Numerical/Analytical Deviation")
plt.plot([0.25, 5], [1/1000000, 1/1000000], linewidth=1.0, color='orange', label="Goal: 1 in 1 million")
plt.legend()
plt.xlabel("Radius / mm")
plt.ylabel("Δ Potiential Difference / V $10^-6$")
plt.title("Deviation between Analytical and Numerical (N = {}) Electrostatic Potential".format(n))
plt.show()



### QUESTION 3(B) ###

resolution = 50  #Resolution of r,z in each axis (i.e. colormap is 50x50 pixels)
result = np.zeros(resolution**2)
result = result.reshape(resolution,resolution)
z_array = np.linspace(-5,5,resolution) #Range of z values (mm)
r_array = np.linspace(0.25,5,resolution) #Range of r values (mm)

for j in np.arange(resolution):
    z = z_array[j]
    for i in np.arange(resolution):
        r = r_array[i]
        result[j,i] = int_simpson(-np.pi/2, np.pi/2, electro_pot, n) #Calculate using simpson itnegral fnc

import matplotlib.colors as colors
plt.pcolormesh(r_array, z_array, result, shading='auto', cmap='PiYG') #Create 50x50 colormap using PiYg color scheme
plt.title("Density Map of Electrostatic Potential in r & z directions")
plt.xlabel("r / mm")
plt.ylabel("z / mm")
cbar = plt.colorbar(orientation="horizontal", pad=0.2) #Add colorbar for clairty
cbar.ax.set_xlabel("Potential Difference V")
CS = plt.contour(r_array, z_array, result, levels=10) #Add contours for clarity
plt.clabel(CS, fontsize=12, fmt='%1.1f')
plt.show()