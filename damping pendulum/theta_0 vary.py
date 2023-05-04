#!/usr/bin/python3

import math
import numpy as np
import matplotlib.pyplot as plt
import sys
sys.path.append(".") 
from System import _Damping_Pendulum_
      
m = 1                               # mass
g = 9.8                             # Gravitational acceleration
l = 1                               # length of rope
T = 2 * math.pi * np.sqrt(l/g)      # The period of a undamping pendulum system

# system condition
_Damping_Pendulum_.__init__(_Damping_Pendulum_,m,g,l)

if __name__ == '__main__':
    # initial conditions
    d_theta_0 = 0
    theta_0 = math.pi * np.array([1/6,1/4,1/3,1/2],dtype = 'float32')

    # fix a relatively small step size
    delta_t = 0.0001

    # time sequence
    t = list(np.arange(0,10*T,delta_t,dtype='float32'))
    t = t/T

    # damping coefficient
    damping = 0.8

    # sequence of numerical solutions
    theta_list = np.zeros(len(t))
    d_theta_list = np.zeros(len(t))

    initial_0 = np.zeros(4)
    initial_1 = np.zeros(4)

    for k in range(4):
        # Solve!
        [theta_list,d_theta_list] = _Damping_Pendulum_.Euler_solve(_Damping_Pendulum_,t,delta_t,theta_0[k],d_theta_0,damping)
        theta_list = theta_list * 180 / math.pi
        d_theta_list = d_theta_list * 180 / math.pi
        initial_0[k] = theta_list[0]
        initial_1[k] = d_theta_list[0]
        
        # display image
        plt.figure(1)
        plt.title("Phase diagram of damping pendulum system when " r'$\mu$=' '%1.1f' %damping) 
        plt.xlabel(r'$\theta$' "$(\mathrm{degree})$")
        plt.ylabel(r'$\dot {\theta}$' "$(\mathrm{degree} / \mathrm{s})$")
        #plt.scatter(theta_list[0], d_theta_list[0], s = 100,marker='p')
        plt.plot(theta_list,d_theta_list)
        plt.legend(['30°','45°','60°','90°'],loc='upper left',title=r"$\theta_0 \;(\mathrm{degree})$")
    for j in range(4):
        plt.scatter(initial_0[j],initial_1[j], s = 100,marker='p')
    plt.grid()         
    plt.show()