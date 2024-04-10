"""
Original Author(s):     Dr Aristizabal, Dr Millwater (UTSA)

Modified by:            Matthew Holland

Date:   2024/04/09

This script performs the Euler integration for the HW 8 assignment.

"""

import numpy as np
import math
import time
from numba import prange , njit , jit

@jit( nopython = True )
def int_funct( y , t ):
    """
    Function to be integrated. 

    INPUTS:
    - y: double
    - t: double
    
    OUTPUTS:
    - f :   The output values of the function based on the inputs y & t
    
    """
    # Implement your function here
    f = np.sin( t )
    
    return f

@jit( nopython = True )
def euler_integration( y0 , t0 , dt , tmax ):
    """
    This function implements the Euler method to solve
    an ordinary differential equation given an initial
    condition (y0) and a constant time increment (dt).
    The integration is performed until the maximum 
    compute time is reached.

    The function to be integrated is defined in 
    
     int_funct(y_i, t_i )
                 
    INPUTS:
    - y0: double, Initial value.
    - t0: double, Initial time.
    - dt: double, time increment.
    - tmax: double, Maximum evaluation time.
    
    OUTPUTS:
    - y: array float64, Contains all solutions for each time increment
    - t: array float64, Contains the corresponding time evaluations for each function

       y[i] contains the Euler's solution to the function at time t[i]

    """
    
    # Dummy call of the integration function
    #toss = int_funct( y0 , t0 )

    # Compute the number of evaluations.
    nevals = int((tmax-t0)/dt)
    
    # Initialize arrays.
    y = np.zeros(nevals+1) 
    t = np.arange( t0 , tmax , dt )
    dy_dt = np.zeros(nevals+1)

    # Save initial condition.
    y[0] = y0 
    t[0] = t0

    # Implement the for loop required to perform Euler's integration
    #----------
    for i in range( 1 , nevals+1 ):
        #print("\ti:\t{x}".format(x=i))
        dy_dt[i] = int_funct( y[i-1] , t[i-1] )
        #print("\t\ty:\t{x}".format(x=y[i-1]))
        #print("\t\tt:\t{x}".format(x=t[i-1]))
        #print("\t\tdy/dt:\t{x}".format(x=dy_dt))
        y[i] = dy_dt[i] * dt + y[i-1] 

    #----------
    # Do not modify after this line.

    return  y, t

if __name__ == '__main__':

    #    
    # Define your 
    #
    y0 = -1         
    # Initial value.
    t0 = 0        
    # Initial time.
    dt = 1e-6      
    # Euler's method requires VERY small time increments.
    tmax = 10     
    # Maximum integration time.
    
    # Measure performance in this call.
    t_start = time.time()

    toss0 , toss1 = euler_integration( y0 , t0 , dt , 4 * dt )
    # Dummy call

    y, t = euler_integration(y0, t0, dt, tmax)

    t_end = time.time()

    y_an  = -np.cos(t[-1]) # Analytical solution

    print("Solution for time t={0:.4f}: y(t)={1:.8f} ".format( t[-1],y[-1]))
    print("Analytical solution : y(t)={0:.8f} error: {1:.4e} ".format(y_an ,abs(y_an-y[-1])))
    
    print('CPU time {0}'.format(t_end-t_start))
