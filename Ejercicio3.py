import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import *
import sympy

def ej3(y,x):
    dydt = sympy(2*(x-2)**2*(y/(x-2)))
    return dydt

t = np.linspace(0,5)
def resuelta3():
    resuelta= odeint(ej3,t)
    plt.xlabel('tiempo')
    plt.ylabel('y(t)')
    plt.show()

resuelta3()
