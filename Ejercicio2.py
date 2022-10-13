import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt
from math import *



def ej2(y,x):
    dydt= (y*log(y))/(sin(x))
    return dydt

y0=exp
x=pi/2

def resuelta2():
    resuelta=odeint(ej2,y0,x)
    plt.xlabel('tiempo')
    plt.ylabel('y(t)')
    plt.show()

resuelta2()
