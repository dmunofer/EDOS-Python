import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt


def ej1(y,x):
    dydt= (x**2*y-y)/(1+y)
    return dydt

y0=-1
t = np.linspace(0,25)

def resuelta():
    y = odeint(ej1,y0,t)
    plt.plot(y,t)
    plt.xlabel('tiempo')
    plt.ylabel('y(t)')
    plt.grid
    plt.show()

resuelta()