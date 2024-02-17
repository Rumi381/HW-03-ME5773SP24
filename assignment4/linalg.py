# -*- coding: utf-8 -*-
"""
Created on Fri Feb 16 16:05:07 2024

@author: mtthl
"""

import numpy as np
import time

###############################################################################
#
# 2.1
#
###############################################################################

N = int( 10e3 )
print( "N:{x}".format( x = N ) )

t_matrxcreate = time.time()

K = np.zeros( ( N , N ) )
K = K + 2 * np.identity( N ) - np.roll( np.identity( N ) , -1 , axis = 0 ) - np.roll( np.identity( N ) , 1 , axis = 0 )
K[-1,-1] = 1
K[-1,0] = 0
K[0,-1] = 0

f = np.zeros( N )
f[-1] = 1 / N

t_matrxformed = time.time()
print( "Time to create matrices: {x:.9f}".format( x = ( t_matrxformed - t_matrxcreate ) ) )

u = np.linalg.solve( K , f )

t_matrxsolve = time.time()
print( "Time to solve matrices: {x:.9f}".format( x = ( t_matrxsolve - t_matrxformed ) ) )

print( "\nArray u:\n" )
print( u )

print( "\nu\u2099: {x}".format( x = int( u[-1] ) ) )
