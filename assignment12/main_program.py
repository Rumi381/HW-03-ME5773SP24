import cupy as cp
import time as time
import numpy as np

##############################################################################
#
# Define the kernels
#
###############################################################################

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

###############################################################################
#
# Formulate Stiffness Matrix
#
###############################################################################

# Create the inputs. Must be defined with corresponding 
# types as in the raw kernel.

t_start = time.time()
N = 30000

K = cp.empty((N,N),dtype = cp.float64)

# Define the execution grid.
block_dim = 16
grid_dim  = N//block_dim+1 # Guarantee we send at least 1 grid.

# We are required to create the holder of the result.
# print("-")
defK_kernel((grid_dim,grid_dim,1), (block_dim,block_dim,1), ( K, K.shape[0],K.shape[1])) 
# grid, block and arguments

t_end = time.time()

# Check the values in the matrix:
print("K:")
print(K)
print("----------------------------------------------------------------------")

print(f"Time spent creating the matrix:\t{t_end-t_start:.6f}-s")

print("----------------------------------------------------------------------")

###############################################################################
#
# Formulate Forces of Finite Element Problems
#
###############################################################################

f = cp.zeros( N , dtype = cp.float64 )
f[-1] = 1/N

t_force = time.time()

print("f:")
print(f)
print("----------------------------------------------------------------------")

print( "Time to formulate force vector:\t{x:.6f}-s".format( x = t_force - t_end ) )

print("----------------------------------------------------------------------")

###############################################################################
#
# Solve Finite Element Problem
#
###############################################################################

u = cp.linalg.solve( K , f )

t_solve = time.time()

print("u:")
print( u )
print("----------------------------------------------------------------------")

print( "Time to formulate solve finite element problem:\t{x:.6f}-s".format( x = t_solve - t_force ) )

print("----------------------------------------------------------------------")
