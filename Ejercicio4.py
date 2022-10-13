import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import *



def ej4(y,t):
    dydt=3*t**2+y/(2*t)
    return dydt
y=1
t = np.linspace(0,5)
def resuelta4():
    resuelta= odeint(ej4,y,t)
    plt.plot(resuelta,t)
    plt.xlabel('tiempo')
    plt.ylabel('y(t)')
    plt.grid
    plt.show()

resuelta4()