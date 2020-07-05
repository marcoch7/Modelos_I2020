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

res = []
resy = []
with open('datos.csv') as csvfile:
    for line in csvfile:            
        line = line.strip()        
        if line != '':
            try:
                res.append(float(line))
                resy.append(float(line))
            except ValueError:
                pass    

print(res)

# Crear histograma de Y. RESPUESTA 4
a, bins, c = plt.hist(res, 200, density = 1, facecolor='blue', alpha=0.5)
plt.xlabel('Magnitud')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.title(r'Histograma de mediciones de una variable fisica')
plt.savefig('res4.png')


# RESPUESTA 5
(mu, sigma) = stats.rayleigh.fit(res)
print("mu: ", mu)
print("sigma: ", sigma)
rayleigh = stats.rayleigh(mu, sigma)
print("rayleigh: ", rayleigh)
y = stats.rayleigh.pdf(bins, mu, sigma)
plt.plot(bins, y)
cdf = stats.rayleigh.cdf(bins, mu, sigma)
plt.savefig('res5.png')

# Respuesta 6. Probabilidad en el intervalo [18, 68]

print("La probabilidad en el intervalo [18, 68] es: ", rayleigh.cdf(68) - rayleigh.cdf(18))
contrast = 0
for i in range(0, len(res)):
    if res[i] <= 68 and res[i] >= 18:
        contrast += 1

contraste = float(contrast)/len(res)

print("La probabilidad relativa de este intervalo es: ", contraste)   

# Respuesta 7. Calcular los cuatro primeros momentos y comentar sobre el “significado” de cada uno y la correspondencia con la grafica observada y los valores teoricos.

mean, var = rayleigh.stats(moments='mv')
skew = stats.skew(res)
kurt = stats.kurtosis(res)
dev = np.sqrt(skew)
print("Los primeros cuatro momentos:")
print("     Mean: ", float(mean))
print("     Var: ", float(var))
print("     Dev: ", float(dev))
print("     Skew: ", float(skew))
print("     Kurt: ", float(kurt))

# Respuesta 8. Y = sqrt(X), graficar el histograma de Y
resultS = []
for numero in resy:                   
        resultS.append(np.sqrt(numero))
a, bins, c = plt.hist(resultS, 200, facecolor='yellow', alpha=0.5)
plt.xlabel('Magnitud')
plt.ylabel('Frecuencia')
plt.grid(True)
plt.title(r'Histograma de mediciones de la raiz de una variable fisica')
plt.savefig('resy.png')