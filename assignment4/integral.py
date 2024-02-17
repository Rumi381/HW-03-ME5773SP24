# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 17:34:30 2024

@author: mtthl
"""

import numpy as np
import math as mt
import numexpr as nx
import time

###############################################################################
#
# Global Data
#
###############################################################################

N = int( 1e9 )
deltax = 2 / N

###############################################################################
#
# 3.2
#
###############################################################################

F1 = 0

time_forloopst = time.time()

for i in range( N ):
    
    x_i = deltax * i - 1
    f_xi = mt.sqrt( 4 - 4 * ( x_i ** 2 ) )
    F1 = F1 + f_xi * deltax

time_forloopsp = time.time()
print( "For loop operation time: \t{x:.6f}".format( x = ( time_forloopsp - time_forloopst ) ) )

print( "F1: \t{x:.16e}".format( x = F1 ) )

###############################################################################
#
# 3.3
#
###############################################################################

i_vec = np.arange( 0 , N , 1 )
x_vec = ( 2 * i_vec / N ) - 1
F_vec = np.sqrt( 4 - 4 * ( x_vec ** 2 ) )
F2 = np.sum( F_vec ) * deltax

time_npsummation = time.time()
print( "Numpy calculation time: \t{x:.6f}".format( x = ( time_npsummation - time_forloopsp ) ) )

print( "F2: \t{x:.16e}".format( x = F2 ) )

###############################################################################
#
# 3.4
#
###############################################################################

x_vec = nx.evaluate('(2 * i_vec / N) - 1')
F_vec = nx.evaluate('(4 - 4 * (x_vec**2))**(1/2)')
F3 = nx.evaluate('sum(F_vec)') * deltax

time_nxsummation = time.time()
print( "Numbers Express calculation time: \t{x:.6f}".format( x = ( time_nxsummation - time_npsummation ) ) )

print( "F3: \t{x:.16e}".format( x = F3 ) )

