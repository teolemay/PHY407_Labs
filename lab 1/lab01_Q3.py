''' This code contains 1) The custom histogram function created
 2) A for loop to test each sample size across the two functions 
 (as well as another for loop to average out these values over multiple tests) 
 ***NOTE: plt.show() is currently commented out for both histograms so they don't
 appear every loop. They have been compared and are identical. ***   '''

import numpy as np
import matplotlib.pyplot as plt
from time import time

def hist_manual(input, bins, plot = False):
    '''input is a 1D array; bins is an integer. Works by creating linspace array of bin size
    and checks how many values fall within the range of each bin. Produces histogram pyplot
    '''
    min = np.min(input)
    max = np.max(input)
    x = np.linspace(min,max,bins+1)
    y = np.zeros(bins+1) 
    #Bins+1 used so the histogram can start at zero at the edges
    y[0] = 0
    for i in range(np.size(x)-1):
        y[i+1] = np.size(np.where((input >= x[i]) & (input < x[i+1])))
    # By using >= and < for each, ensures no overlap in one value 
    # being sorted into two bins/double counted
    y[bins] = np.size(np.where(input > x[bins-1])) #capturing final bin
    
    if plot == True:
        plt.step(x, y, color="red", label='Custom')
        plt.fill_between(x,y, step="pre", alpha=0.4, color='red')
        plt.legend()
        plt.title("Histogram")
        plt.xlabel("Data Values")
        plt.ylabel("Number of Occurrences")
        ###!plt.show()
        plt.clf()
    

N = np.array([10,100,1000,10000,100000,1000000])  #Sample sizes
M = 1000    #Bin Size
time_arr_custom = np.zeros(np.size(N))
time_arr_numpy = np.zeros(np.size(N))


for j in np.arange(3):  ## Average 3 times for better results
    for i in np.arange(np.size(N)):
        data = np.random.randn(N[i])  
   
        ### Numpy function
        start = time() 
        counts, bins = np.histogram(data, M)
        plt.step(bins[:-1], counts)
        ###!plt.show()
        plt.clf() #Clear pyplot cache
        end = time()
        time_arr_numpy[i] += end-start
        
        ### Manual function
        start = time() 
        hist_manual(data, M, plot=True)
        end = time()
        time_arr_custom[i] += end-start
    

print("Custom function ", time_arr_custom/3) #Divide by 3 because that will return mean result
print("Numpy function ", time_arr_numpy/3)

### Plot time comparison between each histogram function

plt.plot(N, time_arr_custom/3, label="Custom Hist Function")
plt.plot(N, time_arr_numpy/3, label="NumPy Hist Function")
plt.xscale('log')
plt.legend()
plt.xlabel("Number of Samples")
plt.ylabel("Time to Execute Code (s)")
plt.title("Custom & NumPy Histogram Function: Number of Samples vs Runtime")
plt.show()