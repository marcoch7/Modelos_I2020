# coding=utf-8
# Simulación de Montecarlo

import csv
import numpy as np
from scipy import stats
from scipy.stats import norm
from scipy.stats import rayleigh
from scipy.stats import moment
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab

resy = []
with open('datos.csv') as csvfile:
    for line in csvfile:            
        line = line.strip()        
        if line != '':
            try:
                resy.append(float(line))
            except ValueError:
                pass    

mu = 5.9063850448899702
sigma = 1.6267631301145551

x = []
i = 0
while i<=15:
    x.append(i)
    i += 0.1
print(x)    

