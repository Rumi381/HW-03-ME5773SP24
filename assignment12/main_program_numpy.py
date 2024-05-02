#import cupy as cp
import time as time
import numpy as np

##############################################################################
#
# Define the kernels
#
###############################################################################

"""
defK_kernel = cp.RawKernel(r'''extern "C" __global__
void defK( double* K, int ncols, int nrows) {
    /*
    This function defines a (simple and hypothetical) stiffness matrix (in row-
        major format) defined by the prompt in Assignment 12.
    
    INPUTS: 
    - K: Pointer to the memory in K.
    - nrows: Number of rows of the matrix
    - ncols: Number of columns of the matrix
    
    */
    
    // Define global indices of the threads along each direction.
    int i = blockDim.x * blockIdx.x + threadIdx.x;
    int j = blockDim.y * blockIdx.y + threadIdx.y;   
    
    // Check that the i, j location lies within the matrix dimensions.
    if ( ( i < nrows) && ( j < ncols ) ){

        long long g_indx = i * ncols + j ;    
        // Calculate the global index within the matrix
        
        if (i==j){

            if (i<(nrows-1)){
                K[g_indx] = 4.0;
            } else {
                K[g_indx] = 2.0;
            }
        
        } else { 
            
            if ((i==(j+1))||(i==(j-1))) {
                    K[g_indx] = -2.0;
                    }
        
        }
        
    }

}''', 'defK')
            
"""

###############################################################################
#
# Formulate Stiffness Matrix
#
###############################################################################

# Create the inputs. Must be defined with corresponding 
# types as in the raw kernel.

t_start = time.time()
N = 30000

#K = cp.empty((N,N),dtype = cp.float64)

K = np.eye( N ) * 4

K[-1,-1] = 2

off_val = -2
for i in range(N-1):
    K[i,i+1] = off_val
    K[i+1,i] = off_val


# Define the execution grid.
block_dim = 16
grid_dim  = N//block_dim+1 # Guarantee we send at least 1 grid.

# We are required to create the holder of the result.
# print("-")
#defK_kernel((grid_dim,grid_dim,1), (block_dim,block_dim,1), ( K, K.shape[0],K.shape[1])) 
# grid, block and arguments

t_end = time.time()

# Check the values in the matrix:
print("K:")
print(K)
print("----------------------------------------------------------------------")

print( "Time spent creating the matrix:\t{x:.6f}-s".format( x = t_end - t_start ) )

print("----------------------------------------------------------------------")

###############################################################################
#
# Formulate Forces of Finite Element Problems
#
###############################################################################

f = np.ones( N , dtype = np.float64 ) / N
f[0:N-1] = 0
# Don't ask

t_force = time.time()

print("f:")
print(f)

print("Last entry in f:")
print(f[N-1])

print("First entry in f:")
print(f[0])

print("----------------------------------------------------------------------")

print( "Time to formulate force vector:\t{x:.6f}-s".format( x = t_force - t_end ) )

print("----------------------------------------------------------------------")

###############################################################################
#
# Solve Finite Element Problem
#
###############################################################################

u = np.linalg.solve( K , f )

t_solve = time.time()

print("u:")
print( u )

print("Last entry in u:")
print(u[-1])

print("----------------------------------------------------------------------")

print( "Time to formulate solve finite element problem:\t{x:.6f}-s".format( x = t_solve - t_force ) )

print("----------------------------------------------------------------------")
