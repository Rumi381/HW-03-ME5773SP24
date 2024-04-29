import module as md
import numpy as np
import time


N = int( 10e3 )
print( "N:{x}".format( x = N ) )

t_matrxcreate = time.time()

A = np.zeros( ( N , N ) )
A = A + 2 * np.identity( N ) - np.roll( np.identity( N ) , -1 , axis = 0 ) - np.roll( np.identity( N ) , 1 , axis = 0 )
A[-1,-1] = 1
A[-1,0] = 0
A[0,-1] = 0

b = np.zeros( ( N , N ) )
b[-1,-1] = 1 / N

# A =  np.array([[    -5.86,   3.99,  -5.93,  -2.82,   7.69, ],
#                [   3.99,   4.46,   2.58,   4.42,   4.61, ],
#                [    -5.93,   2.58,  -8.52,   8.57,   7.69, ],
#                [    -2.82,   4.42,   8.57,   3.72,   8.07, ],
#                [    7.69,   4.61,   7.69,   8.07,   9.83, ]])

# b = np.array([[    1.32,  -6.33,  -8.77, ],
#               [    2.22,   1.69,  -8.33, ],
#               [   0.12,  -1.56,   9.54, ],
#               [   -6.41,  -9.49,   9.56, ],
#               [   6.33,  -3.67,   7.48, ]])




print('Solving sytem of linear equations with mkl_solver function')
print('            ')
print('Matrices before solution')
print('            ')
print('Matrix A')
print(A)
print('======================')
print('Matrix B')
print(b)


t_start = time.time()
res = md.mkl_solver( A,b )
t_end = time.time()

print('            ')
print('Matrices after solution')
print('            ')
print('Matrix A')
print(A)
print('======================')
print('Matrix B')
print(b)

print('======================')
print('Time spent with mkl_solver function: {0:.6f} s'.format(t_end-t_start))



print('            ')
print('======================================================================')
print('======================================================================')
print('            ')




print('Solving sytem of linear equations with mkl_solver function')
print('            ')
print('Matrices before solution')
print('            ')
print('Matrix A')
print(A)
print('======================')
print('Matrix B')
print(b)


t_start = time.time()
res = md.mkl_solver_symm( A,b )
t_end = time.time()

print('            ')
print('Matrices after solution')
print('            ')
print('Matrix A')
print(A)
print('======================')
print('Matrix B')
print(b)

print('======================')
print('Time spent with mkl_solver_symm function: {0:.6f} s'.format(t_end-t_start))

