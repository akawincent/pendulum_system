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
    theta_0 = math.pi * np.array([1/60,1/15,1/6,1/4,1/2],dtype = 'float32') 
    d_theta_0 = 0

    # fix a relatively small step size
    delta_t = 0.001
    # time sequence
    t = list(np.arange(0,5*T,delta_t,dtype='float32'))
    t = t/T
    # sequence of numerical solutions
    theta_list = np.zeros(len(t))
    d_theta_list = np.zeros(len(t))
    # sequence of linear approximate analytic solutions
    linear_theta_list = np.zeros(len(t))

    for k in range(5):

        # analytic solutions
        linear_theta_list = theta_0[k] * np.cos(math.sqrt(g/l) * t)
        linear_theta_list = linear_theta_list * 180 / math.pi
    
        # numerical solutions
        [theta_list,d_theta_list] = _Undamped_Pendulum_.Euler_solve(_Undamped_Pendulum_,t,delta_t,theta_0[k],d_theta_0)
        theta_list = theta_list * 180 / math.pi
    
        plt.figure(1)
        plt.title("Numerical solution of the original nonlinear equation")
        plt.xlabel("dimensionless time  t/" r'$\tau$')
        plt.ylabel(r'$\theta$' "$(\mathrm{degree})$")
        plt.plot(t,theta_list)
        plt.grid()
        plt.legend(['3°','12°','30°','45°','90°'],loc='upper left',title=r"$\theta_0 \;(\mathrm{degree})$")

        plt.figure(2)
        plt.title("Analytical solutions to linear approximation equations")
        plt.xlabel("dimensionless time  t/" r'$\tau$')
        plt.ylabel(r'$\theta$' "$(\mathrm{degree})$")
        plt.plot(t,linear_theta_list,ls = '-.')
        plt.grid()
        plt.legend(['3°','12°','30°','45°','90°'],loc='upper left',title=r"$\theta_0 \;(\mathrm{degree})$")

plt.show()