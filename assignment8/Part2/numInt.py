"""
Original Author(s):     Dr Aristizabal, Dr Millwater (UTSA)

Modified by:            Matthew Holland

Date:   2024/04/09

This script performs the numerical integration for the HW 8 assignment.

"""

import numpy as np
import time

def myfunct(x):
    """
    Defines the function to be integrated.

    INPUTS:
    - x: double, evaluation point.

    OUTPUTS:
    - double, evaluated function.
    
    """

    return np.sin(x*x)+x/2

# end function

def integral_riemann(a,b,N):
    """
    Implements the Riemann integration for the function
    myfunct(x).

    INPUTS:
    - a: double, Lower integration limit.
    - b: double, Upper integration limit.
    - N: Int, Number of integration regions.

    OUTPUTS:
    - double, evaluated integral.
    
    """
    dx = (b-a)/N
    F = 0
    
    for i in range(N):
        x = a + i*dx
        F += myfunct(x)*dx
    # end for 

    return F

# end function

if __name__ == '__main__':

    # If needed, add dummy call to the integral_riemann
    # function here

    # Evaluate the CPU time and integration here.

    t_start = time.time()
    a = 0
    b = 2
    N = 100_000_000 # 10**8 
    F = integral_riemann(a,b,N)
    t_end = time.time()


    print('Integral {0:f}'.format(F))
    print('CPU time:{0:.6f}s'.format(t_end-t_start))

# end if
