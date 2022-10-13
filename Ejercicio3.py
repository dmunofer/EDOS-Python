import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import *


def ej3(y,x):
    dydx = 2*(x-2)**2+ (y/(x-2))
    return dydx

y=1
t= np.linspace(0,5)

def resuelta3():
    resuelta= odeint(ej3,y,t)
    plt.plot(resuelta,t)
    plt.xlabel('tiempo')
    plt.ylabel('y(t)')
    plt.grid
    plt.show()


resuelta3()
