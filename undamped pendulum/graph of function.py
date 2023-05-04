#!/usr/bin/python3

import math
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(".") 
from System import _Undamped_Pendulum_
      
m = 1                               # mass
g = 9.8                             # Gravitational acceleration
l = 1                               # length of rope
T = 2 * math.pi * np.sqrt(l/g)      # The period of a undamping pendulum system

# system condition
_Undamped_Pendulum_.__init__(_Undamped_Pendulum_,m,g,l,T)

if __name__ == '__main__':

    # initial conditions
    theta_0 = math.pi/60    
    d_theta_0 = 0

    # different step size
    delta_t = 0.001

    # time sequence
    t = list(np.arange(0,5*T,delta_t,dtype='float32'))
    t = t/T

    # solution sequence
    theta_list = np.zeros(len(t))
    d_theta_list = np.zeros(len(t))

    # Solve!
    [theta_list,d_theta_list] = _Undamped_Pendulum_.Euler_solve(_Undamped_Pendulum_,t,delta_t,theta_0,d_theta_0)
    theta_list = theta_list * 180 / math.pi

    plt.figure(1)
    plt.title("Graph of " r'$\theta(t)$' " at small angles")
    plt.xlabel("dimensionless time  t/" r'$\tau$')
    plt.ylabel(r'$\theta$' "$(\mathrm{degree})$")
    plt.plot(t,theta_list)
    plt.grid()
    plt.show()