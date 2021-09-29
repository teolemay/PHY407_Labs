"""
PHY 407 lab 1: question 1 C) and D)

Teophile Lemay and Charlie Hughes

This script calculates the x and y position as well as x and y velocity of the Planet Mercury around the sun
The calculation is first performed assuming a Newtonian orbit, then repeated while accounting for general relativity.

all calculations done with units of years, AU, Msun for time, distance, mass respectively.
"""

import scipy.constants as spc
import numpy as np
import matplotlib.pyplot as plt

#define constants
G = 39.5 #Au^3 / (M_sun * year^2)
Msun = 1 #2.0 * 10**30 kg
deltaT = 0.0001 #years

def r(x, y):
    """
    calculate radius of orbit using pythagoras's thm
  
    :param x: x distance 
    :param y: y distance
  
    :return: radius
    """
    return np.sqrt(x**2 + y**2)

#QUESTION 1 C)
#define initial conditions and empty arrays to fill with calculated values
time =  np.arange(0, 1, deltaT)
x = np.zeros_like(time)
x[0] = 0.47 #initial conditions are added manually when not 0
y = np.zeros_like(time)
vx = np.zeros_like(time)
vy = np.zeros_like(time)
vy[0] = 8.17

#iterate through time using the Euler-Cromer method
for i in range(0, len(time)-1):
    vx[i+1] = vx[i] - G*Msun*x[i]*deltaT / (r(x[i], y[i])**3)
    vy[i+1] = vy[i] - G*Msun*y[i]*deltaT / (r(x[i], y[i])**3)
    x[i+1] = x[i] + vx[i+1] * deltaT
    y[i+1] = y[i] + vy[i+1] * deltaT  
  
# plot positions vs time, velocities vs time, orbit trace.
plt.figure()
plt.plot(time, x)
plt.title('X Position vs. Time')
plt.xlabel('Time (years)')
plt.ylabel('X Position (AU)')
plt.figure()
plt.plot(time, y)
plt.title('Y Position vs. Time')
plt.xlabel('Time (years)')
plt.ylabel('Y Position (AU)')
plt.figure()
plt.plot(time, vx)
plt.title('X Velocity vs. Time')
plt.xlabel('Time (years)')
plt.ylabel('X Velocity (AU/year)')
plt.figure()
plt.plot(time, vy)
plt.title('Y Velocity vs. Time')
plt.xlabel('Time (years)')
plt.ylabel('Y Velocity (AU/year)')
plt.figure()
plt.plot(x, y)
plt.title("Mercury's (Newtonian) Orbit")
plt.xlabel('X Position (AU)')
plt.ylabel('Y Position (AU)')
plt.show()


#QUESTION 1 D)

#define additional constants
alpha = 0.01 #AU^2

#define initial conditions and empty arrays to fill with calculated values
time =  np.arange(0, 4, deltaT) #evaluate over 4 earth years for extra effect
x = np.zeros_like(time)
x[0] = 0.47 #initial conditions are added manually when not 0
y = np.zeros_like(time)
vx = np.zeros_like(time)
vy = np.zeros_like(time)
vy[0] = 8.17

#iterate through time using the Euler-Cromer method
for i in range(0, len(time)-1):
    #the equation for velocity has been updated to include the correctional term (1 + alpha/r^2)
    vx[i+1] = vx[i] - G*Msun*x[i] * (1 + alpha/(r(x[i], y[i])**2)) * deltaT / (r(x[i], y[i])**3)
    vy[i+1] = vy[i] - G*Msun*y[i] * (1 + alpha/(r(x[i], y[i])**2)) * deltaT / (r(x[i], y[i])**3)
    x[i+1] = x[i] + vx[i+1] * deltaT
    y[i+1] = y[i] + vy[i+1] * deltaT  

plt.figure()
plt.plot(x, y)
plt.title("Mercury's (exaggerated relativistic) Orbit")
plt.xlabel('X Position (AU)')
plt.ylabel('Y Position (AU)')
plt.show()