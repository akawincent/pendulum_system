#!/usr/bin/python3

import math
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(".") 
from System import _Damping_Rod_
  
m = 1                               # mass
g = 9.8                             # Gravitational acceleration
l = 1                               # length of rod
a = 0.1                             # radius
T = 2 * math.pi * np.sqrt(l/g)      # The period of a undamping pendulum system

# system condition
_Damping_Rod_.__init__(_Damping_Rod_,m,g,l,a)

if __name__ == '__main__':
    # initial conditions
    theta_0 = math.pi * np.array([1/6,1/4,1/3,1/2],dtype = 'float32')
    d_theta_0 = 0

    # fix a relatively small step size
    delta_t = 0.001
    # time sequence
    t = list(np.arange(0,5*T,delta_t,dtype='float32'))
    t = t/T
    # sequence of numerical solutions
    theta_list = np.zeros(len(t))
    d_theta_list = np.zeros(len(t))

    # coefficient
    k = 1

    for i in range(4):
    
        # numerical solutions
        [theta_list,d_theta_list] = _Damping_Rod_.Euler_solve(_Damping_Rod_,t,delta_t,theta_0[i],d_theta_0,k)
        theta_list = theta_list * 180 / math.pi
    
        plt.figure(1)
        plt.title("Graph of " r'$\theta(t)$' " with different " r'$\theta_0$')
        plt.xlabel("dimensionless time  t/" r'$\tau$')
        plt.ylabel(r'$\theta$' "$(\mathrm{degree})$")
        plt.plot(t,theta_list)
        
plt.legend(['30°','45°','60°','90°'],loc='upper right',title=r"$\theta_0 \;(\mathrm{degree})$")
plt.grid()
plt.show()