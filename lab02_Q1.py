"""
PHY407 lab 2 question 1

Charlie Hughes and Teophile Lemay

This script compares standard deviations calculated using a double pass method (lab 2 exercise sheet, eq. 1) and a single pass method (lab 2 exercise sheet, eq. 2)
"""

import numpy as np

def mean(input):  #Calculate mean of 1d array using for loop
    avg = 0
    for i in input:
        avg += i
    return avg/np.size(input)

def std_dev_1(input, mean): #Calculate std using formula 1 from report. Input 1d array and mean
    std = 0
    for i in input:
        std += (i - mean)**2
    return np.sqrt((1/(np.size(input)-1))*std)

def std_dev_2(input): #Calculate std using formula 2 from report
    sum = 0
    mean = 0
    n = np.size(input)
    for i in input: #Note only 1 loop is passed through
        sum += i**2
        mean += i
    mean = mean / n
    return np.sqrt((1/(n-1))*(sum-n*(mean**2)))


### QUESTION 1(B) ###
print("Question 1B")

array = np.loadtxt("cdata.txt") #load data given
std_true = np.std(array, ddof=1) #Calculate true standard deviation using numpy

std1 = std_dev_1(array, mean(array)) #Two passes
std2 = std_dev_2(array) #One pass

print((std1 - std_true)/std_true) #Check relative error for each
print((std2 - std_true)/std_true)


### QUESTION 1(C) ###
print("Question 1C")

sequence1 = np.random.normal(0., 1., 2000) #Two sequences of given parameters created
sequence2 = np.random.normal(1.e7, 1., 2000)

# Sequence 1
std_true_seq1 = np.std(sequence1, ddof=1) #True std using numpy
std_seq1_method1 = std_dev_1(sequence1, mean(sequence1)) #Two passes
std_seq1_method2 = std_dev_2(sequence1) #One pass
print("Sequence 1 relative error for formulae 1 & 2")
print((std_seq1_method1 - std_true_seq1)/std_true_seq1) #Relative error
print((std_seq1_method2 - std_true_seq1)/std_true_seq1)

# Sequence 2
std_true_seq2 = np.std(sequence2, ddof=1)
std_seq2_method1 = std_dev_1(sequence2, mean(sequence2)) #Two passes
std_seq2_method2 = std_dev_2(sequence2)
print("Sequence 2 relative error for formulae 1 & 2")
print((std_seq2_method1 - std_true_seq2)/std_true_seq2)
print((std_seq2_method2 - std_true_seq2)/std_true_seq2)