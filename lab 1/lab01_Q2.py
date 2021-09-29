"""
PHY 407 lab 1: question 2 A)

Teophile Lemay and Charlie Hughes

This script calculates the orbit of the Jupiter around the sun, as well as the earth's orbit while taking 
into account the gravitational effect of Jupiter on the earth.
Purely Newtonian orbit are assumed.

For parts B and C of question 2, constants and initial conditions wouldbe changed in order to investigate the 
effect of Jupiter having a greatly increased mass, or Jupiter's effect on the orbit of an asteroid orbiting 
further from the sun than the earth.

all calculations done with units of years, AU, and Msun for time, distance, mass respectively.
"""

import numpy as np 
import matplotlib.pyplot as plt 

#define constants
deltaT = 0.0001 #years
Msun = 1 #1.989 * 10**30 kg  https://nssdc.gsfc.nasa.gov/planetary/factsheet/sunfact.html
Mjup = 0.000954 #(1.898 × 10^27 kg) / (1.989 × 10^30 kg) https://ssd.jpl.nasa.gov/?planet_phys_par
G = 39.5 #Au^3 / (M_sun * year^2)

def r(x, y):
    """
    calculate radius of orbit using pythagoras's thm
  
    :param x: x distance 
    :param y: y distance
  
    :return: radius
    """
    return np.sqrt(x**2 + y**2)

#create arrays and set initial conditions
time = np.arange(0, 10, deltaT)
#arrays for Jupiter
xJ = np.zeros_like(time)
xJ[0] = 5.2 #AU
yJ = np.zeros_like(time)
vxJ = np.zeros_like(time)
vyJ = np.zeros_like(time)
vyJ[0] = 2.63 #AU/year
#arrays for earth
xE = np.zeros_like(time)
xE[0] = 1
yE = np.zeros_like(time)
vxE = np.zeros_like(time)
vyE = np.zeros_like(time)
vyE[0] = 6.18

#calculate Jupiter's orbit
for i in range(0, len(time)-1):
    vxJ[i+1] = vxJ[i] - G*Msun*xJ[i] * deltaT / (r(xJ[i], yJ[i])**3)
    vyJ[i+1] = vyJ[i] - G*Msun*yJ[i] * deltaT / (r(xJ[i], yJ[i])**3)
    xJ[i+1] = xJ[i] + vxJ[i+1] * deltaT
    yJ[i+1] = yJ[i] + vyJ[i+1] * deltaT

# calculate earth's orbit:
for i in range(0, len(time)-1):
    vxE[i+1] = vxE[i] - ( G*Msun*xE[i]/(r(xE[i], yE[i])**3) + G*Mjup*(xE[i] - xJ[i])/(r( xE[i]-xJ[i], yE[i]-yJ[i] )**3)  ) * deltaT
    vyE[i+1] = vyE[i] - ( G*Msun*yE[i]/(r(xE[i], yE[i])**3) + G*Mjup*(yE[i] - yJ[i])/(r( xE[i]-xJ[i], yE[i]-yJ[i] )**3)  ) * deltaT
    xE[i+1] = xE[i] + vxE[i+1] * deltaT
    yE[i+1] = yE[i] + vyE[i+1] * deltaT


#plot orbits
plt.figure()
plt.plot(xJ, yJ, label='Jupiter')
plt.plot(xE, yE, label='Earth')
plt.legend()
plt.title('Orbits of Jupiter and Earth over 10 years')
plt.xlabel('X position (AU)')
plt.ylabel('Y position (AU)')

plt.show()

