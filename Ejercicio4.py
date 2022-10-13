import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import *
import sympy


def ej4(y,t):
    dydt=sympy(3*t**2+y)/(2*t)
    return dydt

t = np.linspace(0,5)
def resuelta4():
    resuelta= odeint(ej4,t)
    plt.xlabel('tiempo')
    plt.ylabel('y(t)')
    plt.show()

resuelta4()