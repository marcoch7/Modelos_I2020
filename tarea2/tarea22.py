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

resultS = []
for numero in resy:                   
        resultS.append(np.sqrt(numero))
a, bins, c = plt.hist(resultS, 100, density = 1, facecolor='m', alpha=0.5)
plt.xlabel('Magnitud')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.title(r'Histograma de mediciones de la raiz de una variable fisica')
plt.savefig('resfinal.png')

(mu, sigma) = stats.norm.fit(resultS)
print("mu: ", mu)
print("sigma: ", sigma)
normalfit = stats.norm.pdf(bins, mu, sigma)
plt.plot(bins, normalfit)
plt.savefig('res72.png')