#!/usr/bin/python3

import math
import numpy as np

###### undamped pendulum system ######
class _Undamped_Pendulum_:
    # conditions 
    def __init__(self,mass,gravity,length,period) -> None:
        self.m = mass
        self.g = gravity
        self.l = length
        self.p = period

    # Euler solver for this system   
    def Euler_solve(self,range_t,delta_t,theta_0,d_theta_0):
        # initial conditions
        y10 = theta_0
        y20 = d_theta_0

        # Create two lists to store the solution results
        y1_list = np.zeros(len(range_t))
        y2_list = np.zeros(len(range_t))

        # Stores the initial condition to the list
        y1_list[0] = y10
        y2_list[0] = y20

        # Back up the original state variables
        y1_backup = y10
        y2_backup = y20

        # Start iterative solution      
        for i in range(len(range_t)-1):
            # Update the first derivative
            d_y1 = y2_backup
            d_y2 = - self.g / self.l * math.sin(y1_backup)

            # Get the solution from the last interation
            y1_last = y1_backup
            y2_last = y2_backup

            # Solve the current solution
            y1 = y1_last + delta_t * d_y1
            y2 = y2_last + delta_t * d_y2

            # Store the solution results to the list
            y1_list[i+1] = y1
            y2_list[i+1] = y2

            # Save the current solution for the next iteration
            y1_backup = y1
            y2_backup = y2

        return [y1_list,y2_list]

###### damping pendulum system ######
class _Damping_Pendulum_:
    # conditions 
    def __init__(self,mass,gravity,length) -> None:
        self.m = mass
        self.g = gravity
        self.l = length
    
    # Euler solver for this system 
    def Euler_solve(self,range_t,delta_t,theta_0,d_theta_0,damp):
        # initial conditions
        y10 = theta_0
        y20 = d_theta_0

        # Create two lists to store the solution results
        y1_list = np.zeros(len(range_t))
        y2_list = np.zeros(len(range_t))

        # Stores the initial condition to the list
        y1_list[0] = y10
        y2_list[0] = y20

        # Back up the original state variables
        y1_backup = y10
        y2_backup = y20

        # Start iterative solution      
        for i in range(len(range_t)-1):
            # Update the first derivative
            d_y1 = y2_backup
            d_y2 = - self.g / self.l * math.sin(y1_backup) - damp * y2_backup

            # Get the solution from the last interation
            y1_last = y1_backup
            y2_last = y2_backup

            # Solve the current solution
            y1 = y1_last + delta_t * d_y1
            y2 = y2_last + delta_t * d_y2

            # Store the solution results to the list
            y1_list[i+1] = y1
            y2_list[i+1] = y2

            # Save the current solution for the next iteration
            y1_backup = y1
            y2_backup = y2

        return [y1_list,y2_list]

###### damping rod system ######
class _Damping_Rod_:
    # conditions 
    def __init__(self,mass,gravity,length,radius) -> None:
        self.m = mass
        self.g = gravity
        self.l = length
        self.r = radius
    
    # Euler solver for this system 
    def Euler_solve(self,range_t,delta_t,theta_0,d_theta_0,k):
        # initial conditions
        y10 = theta_0
        y20 = d_theta_0

        # Create two lists to store the solution results
        y1_list = np.zeros(len(range_t))
        y2_list = np.zeros(len(range_t))

        # Stores the initial condition to the list
        y1_list[0] = y10
        y2_list[0] = y20

        # Back up the original state variables
        y1_backup = y10
        y2_backup = y20

        coe = 6 * k * self.r * self.l / self.m

        # Start iterative solution      
        for i in range(len(range_t)-1):
            # Update the first derivative
            d_y1 = y2_backup
            
            d_y2 = - 3 * self.g / self.l * math.sin(y1_backup) - coe * y2_backup

            # Get the solution from the last interation
            y1_last = y1_backup
            y2_last = y2_backup

            # Solve the current solution
            y1 = y1_last + delta_t * d_y1
            y2 = y2_last + delta_t * d_y2

            # Store the solution results to the list
            y1_list[i+1] = y1
            y2_list[i+1] = y2

            # Save the current solution for the next iteration
            y1_backup = y1
            y2_backup = y2

        return [y1_list,y2_list]

###### undamped double pendulum system ######
class _Undamped_Double_Pendulum_:
    
    def __init__(self,M_wrap,L_wrap,gravity) -> None:
        self.m_1 = M_wrap[0]
        self.m_2 = M_wrap[1]
        self.l_1 = L_wrap[0]
        self.l_2 = L_wrap[1]
        self.g = gravity
    
    def diff_equation(self,t,X):
        # get state variables
        theta_1,theta_2,omega_1,omega_2 = X

        A = np.zeros((2, 2))
        b = np.zeros(2)

        A[0,0] = (self.m_1 + self.m_2) * self.l_1
        A[0,1] = self.m_2 * self.l_2 * np.cos(theta_1 - theta_2)
        A[1,0] = self.m_2 * self.l_1 * np.cos(theta_1 - theta_2)
        A[1,1] = self.m_2 * self.l_2

        b[0] = -self.m_2 * self.l_2 * omega_2**2 * np.sin(theta_1 - theta_2) - self.g * (self.m_1 + self.m_2) * np.sin(theta_1)
        b[1] = self.m_2 * self.l_1 * omega_1**2 * np.sin(theta_1 - theta_2) - self.m_2 * self.g * np.sin(theta_2)

        alpha_1, alpha_2 = np.linalg.solve(A, b)
        return np.array([omega_1, omega_2, alpha_1, alpha_2])

    def Runge_Kutta_solve(df,t,delta,init):
        num = len(init)
        z = np.zeros( (len(t), num) )
        z[0, :] = init
        for i in range(len(t) - 1):
            s0 = df(_Undamped_Double_Pendulum_,t[i], z[i, :])
            s1 = df(_Undamped_Double_Pendulum_,t[i] + delta / 2., z[i, :] + delta * s0 / 2.)
            s2 = df(_Undamped_Double_Pendulum_,t[i] + delta / 2., z[i, :] + delta * s1 / 2.)
            s3 = df(_Undamped_Double_Pendulum_,t[i+1], z[i, :] + delta * s2)
            z[i+1, :] = z[i, :] +  delta * (s0 + 2*(s1+s2) + s3) / 6.
        return t, z




