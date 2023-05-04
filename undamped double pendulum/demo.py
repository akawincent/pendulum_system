#!/usr/bin/python3

import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
import sys
sys.path.append(".") 
from System import _Undamped_Double_Pendulum_
 
m_1 = 1                             # mass of ball_1 (up)
m_2 = 1                             # mass of ball_2 (down)
l_1 = 1                             # length of rope_1 (up)
l_2 = 1                             # length of rope_2 (down)
g = 9.8                             # Gravitational acceleration

# wrap
M = np.array([m_1,m_2])
L = np.array([l_1,l_2])

# system condition
_Undamped_Double_Pendulum_.__init__(_Undamped_Double_Pendulum_,M,L,g)

if __name__ == '__main__':

    # initial conditions
    theta_1_init = math.pi/3  
    theta_2_init = math.pi/2 + math.pi/6 + math.pi/180
    omega_1_init = 0
    omega_2_init = 0
    init = np.array([theta_1_init,theta_2_init,omega_1_init,omega_2_init])

    # time step size
    delta_t = 0.01

    # time sequence
    t = list(np.arange(0,50+delta_t,delta_t,dtype='float32'))

    # solution sequence
    theta_1_list = np.zeros(len(t))
    theta_2_list = np.zeros(len(t))
    omega_1_list = np.zeros(len(t))
    omega_2_list = np.zeros(len(t))

    # solve
    t,z = _Undamped_Double_Pendulum_.Runge_Kutta_solve(_Undamped_Double_Pendulum_.diff_equation,t,delta_t ,init)
    
    theta_1_list = z[:,0]
    theta_2_list = z[:,1]
    omega_1_list = z[:,2]
    omega_2_list = z[:,3]

    # trajectory
    x1 = l_1 * np.sin(theta_1_list)
    y1 = - l_1 * np.cos(theta_1_list)
    x2 = x1 + l_2 * np.sin(theta_2_list)
    y2 = y1 - l_2 * np.cos(theta_2_list)

    # calculate mechanical energy
    energy_k = 0.5 * m_1 * (omega_1_list * l_1)**2 \
             + 0.5 * m_2 * (omega_1_list * l_1)**2 \
             + 0.5 * m_2 * (omega_2_list * l_2)**2 \
             + 0.5 * m_2 * (2 * l_1 * l_2 * omega_1_list * omega_2_list * np.cos(theta_1_list - theta_2_list))
    energy_p = m_1 * g * y1 + m_2 * g * y2
    energy_m = energy_k + energy_p

    # display trajectory
    plt.figure(1)
    plt.title("Motion trajectory of the double pendulum system")
    font = {'family' : 'Times New Roman','weight' : 'normal','size'   : 12,}
    plt.xlabel(r'$ x $' "$(\mathrm{m})$",font)
    plt.ylabel(r'$ y $' "$(\mathrm{m})$",font)
    plt.plot(x1,y1)
    plt.plot(x2,y2)
    plt.grid()
    plt.legend(['up','down'],loc='upper left',title="ball")

    # display energy 
    plt.figure(2)
    plt.title("System mechanical energy")
    plt.xlabel(r'$ t $' "$(\mathrm{s})$",font)
    plt.ylabel(r'$ E $' "$(\mathrm{J})$",font)
    #plt.ylim(10,12.5)
    plt.plot(t,energy_m)
    plt.grid()

    # phase graph
    plt.figure(3)
    plt.title("Phase diagram of up ball")
    plt.xlabel(r'$\theta_1$' "$(\mathrm{degree})$")
    plt.ylabel(r'$\dot {\theta}_1$' "$(\mathrm{degree} / \mathrm{s})$")
    plt.scatter(theta_1_list[0] * 180 / np.pi, omega_1_list[0] * 180 / np.pi, s = 100,marker='p', color='r')
    plt.plot(theta_1_list * 180 / np.pi,omega_1_list * 180 / np.pi)
    plt.grid() 

    plt.figure(4)
    plt.title("Phase diagram of down ball")
    plt.xlabel(r'$\theta_2$' "$(\mathrm{degree})$")
    plt.ylabel(r'$\dot {\theta}_2$' "$(\mathrm{degree} / \mathrm{s})$")
    plt.scatter(theta_2_list[0] * 180 / np.pi, omega_2_list[0] * 180 / np.pi, s = 100,marker='p', color='r')
    plt.plot(theta_2_list * 180 / np.pi,omega_2_list * 180 / np.pi)
    plt.grid() 

    # animation of double pendulum motion
    fig = plt.figure(dpi=144)
    plt.title("Double pendulum system motion demonstration video")
    plt.xlabel(r'$ x $' "$(\mathrm{m})$",font)
    plt.ylabel(r'$ y $' "$(\mathrm{m})$",font)
    ax = fig.gca()
    ax.set_xlim(-3, 3)
    ax.set_ylim(-3, 2)
    ax.set_aspect("equal")
    ax.grid()

    pendumlum, = ax.plot([], [], "-o", lw=2)
    time_mark = ax.text(0.05, 0.9, '', transform=ax.transAxes)

    def init():
        x = [0.0, x1[0], x2[0]]
        y = [0.0, y1[0], y2[0]]
        pendumlum.set_data(x, y)
        time_mark.set_text('')
        return pendumlum, time_mark

    def update(num):
        x = [0.0, x1[num], x2[num]]
        y = [0.0, y1[num], y2[num]]

        pendumlum.set_data(x, y)
        time_mark.set_text('time = %.1fs' % (num*delta_t))
        return pendumlum, time_mark


    ani = FuncAnimation(fig, update, range(1, len(y1)), 
                    interval=delta_t*50, blit=True, init_func=init)
    
    #ani.save('dp.mp4', writer='ffmpeg')
    #ani.save("dp.gif", writer="pillow")
    plt.show()
