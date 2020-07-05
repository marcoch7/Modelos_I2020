import numpy as np
import csv
import matplotlib.pyplot as plt
import matplotlib.mlab as mlab
from scipy.stats import norm
from scipy.optimize import curve_fit
import statistics 
from mpl_toolkits.mplot3d import Axes3D


# Problem 1

# X and Y values 
x_list = list(range(5, 16))
y_list = list(range(5, 26))

# arrays with X and Y probability values 
x_den = [0]*11
y_den = [0]*21

# Store probability values for X and Y
with open('xyp.csv') as csvfile:
    creader = csv.reader(csvfile, delimiter =',')
    for row in creader:
        for i in range(16):
            if row[0] == str(i):                   
                x_den[i-5] += float(row[2])
        for i in range(26):
            if row[1] == str(i):
                y_den[i-5] += float(row[2])        

# Plot X distribution
plt.bar(x_list, x_den)
plt.grid(linestyle='-', linewidth=0.5)
plt.title("X distribution")
plt.xlabel("X value")
plt.ylabel("Relative frequency of X")
plt.savefig('question1X.png')
plt.close()

# Plot Y distribution
plt.bar(y_list, y_den)
plt.grid(linestyle='-', linewidth=0.5)
plt.title("Y distribution")
plt.xlabel("Y value")
plt.ylabel("Relative frequency of Y")
plt.savefig('question1Y.png')
plt.close()


# Best fit curve 
# X
plt.bar(x_list, x_den)
plt.grid(linestyle='-', linewidth=0.5)
plt.title("X distribution")
plt.xlabel("X value")
plt.ylabel("Relative frequency of X")
def gau(e, r, i, c):
    # Gaussian distribution
    return r * np.exp(-(e-i)**2/(2*c**2))

def gaussiana(dom,mu,sigma):
    return 1/(np.sqrt(2*np.pi*sigma**2)) * np.exp(-(dom - mu)**2/(2*sigma**2))

popt, pcov = curve_fit(gau, x_list, x_den)
param, _ = curve_fit(gaussiana, x_list, x_den)
print("X parameters\nMu:", param[0], "Sigma: ", param[1])
e = np.linspace(4, 16, 50)
y = gau(e, *popt)
plt.plot(e , y, c='r')    
plt.savefig('BestfitX.png')
plt.close()


# Best fit curve  Y
plt.bar(y_list, y_den)
plt.grid(linestyle='-', linewidth=0.5)
plt.title("Y distribution")
plt.xlabel("Y value")
plt.ylabel("Relative frequency of Y")
popt, pcov = curve_fit(gau, y_list, y_den)

ee = np.linspace(4, 26, 50)
yy = gau(ee, *popt)
plt.plot(ee , yy, c='r')    
plt.savefig('BestfitY.png')
plt.close()

paramy, _ = curve_fit(gaussiana, y_list, y_den)
print("Y parameters\nMu: ", paramy[0], "Sigma: ", paramy[1])
pdf_y = norm.pdf(paramy[0], paramy[1])

meann = np.mean(x_den)
standard_d = statistics.stdev(x_den)
pdf_x = norm.pdf(x_den)

# Problem 2

# Matrix x,y range
X, Y = np.meshgrid(x_list, y_list)
# funcion densidad conjunta
f_dens = (1/(2*np.pi*3.29944287*6.02693775)) * np.exp(-(((X - 9.90484381)**2)/(2*3.29944287**2) + ((Y - 15.0794609)**2)/(2*6.02693775**2)))


# Problem 3

correlacion = 0
covarianza = 0

# Get correlacion and covarianza
with open('xyp.csv') as csvfile:
    creader = csv.reader(csvfile, delimiter =',')
    for row in creader:
        for i in range(16):
            if row[0] == str(i):                 
                correlacion = correlacion + i*float(row[1])*float(row[2])
                covarianza = covarianza + (i-param[0])*(float(row[1])-paramy[0])*float(row[2])

coef_correlacion = covarianza/(param[1]*paramy[1])                
print("Correlacion: ", correlacion)
print("Covarianza: ", covarianza)
print("Coeficiente de correlacion: ", coef_correlacion)

# Problem 4
plt.plot(y)
plt.title("X marginal density function")
plt.xlabel('fx(x)')
plt.ylabel('some numbers')
plt.savefig("Xmarginal")
plt.close()

plt.plot(yy)
plt.title("Y marginal density function")
plt.xlabel('fy(x)')
plt.ylabel('some numbers')
plt.savefig("Ymarginal")
plt.close()


threed = plt.axes(projection = '3d')
threed.plot_surface(X, Y, f_dens, cmap='viridis', edgecolor = 'none')
threed.set_title("Probabilidad conjunta")
plt.savefig("threed")
plt.close()