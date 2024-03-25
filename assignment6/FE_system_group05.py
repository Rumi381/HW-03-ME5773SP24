# =====================================================================================
# This file defines a system of Finite Element Equations for a simple spring system.
# 
# The purpose of this is to provide a base file that ME5773 students can use to apply
# the concepts of parallelization with Python's multiprocessing module.
#
# Author: Mauricio Aristizabal, PhD
# Last modified: 03/19/2024
#
# =====================================================================================

# =====================================================================================
# Required Libraries
import numpy as np
import scipy as sp # Install scipy using "conda install scipy"
import time
from multiprocessing import Pool
import os
import gc
import multiprocessing
from numba import njit , prange
import sys
import numbers
# =====================================================================================

gc.collect()

num_cores = multiprocessing.cpu_count()
threads_per_core = os.cpu_count()
num_threads = num_cores * threads_per_core

def assemble(e_list, Ke_list, fe_list, Kg, fg):
    """
    DESCRIPTION: Assemble an element's system matrix and rhs into a global 
                 system of equations for 1D Finite Element problem.
                 
                 This assembly function only supports linear elastic problems
                 of springs assembled in the form:
                
            x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x

    
    INPUTS:
        -e: (integer) Element index.
        -Ke: (Float array, Shape: (2,2) ) Elemental stiffness matrix.
        -fe: (Float array, Shape: (2,) )  Elemental force vector.
        -Kg: (Float array, Shape: (Ndof,Ndof) ) Global stiffness matrix.
        -fg: (Float array, Shape: (Ndof,) )     Global force vector.
    
    OUTPUTS:
        - Kg: Updated global stiffness matrix.
        - fg: Updated global force vector.

    """
    
    for e, Ke, fe in zip(e_list, Ke_list, fe_list):
        for i in range(2):
            for j in range(2):
                Kg[ e + i , e + j]  += Ke[ i , j ]
            # end for
        # end for
    return Kg, fg

def elasticElement(e_list,k_list):
    """
    DESCRIPTION: Assemble an element's system of equation into a global 
                 system of equations for 1D Finite Element problem.
                 
                 This assembly function only supports linear elastic problems
                 of springs assembled in the form:
                
            x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x
            
    
    INPUTS:
        -e: (integer) Element index.
        -k_list: (List of floats, len: Ne ) Element stiffness values. Ne: Number of elements.
        
    OUTPUTS:
        - Ke: Elemental stifness matrix
        - fe: Elemental force vector.

    """
    
    Ke_list = [k_list[e] * np.array([[1, -1], [-1, 1]]) for e in e_list]
    fe_list = [np.array([0.0, 0.0]) for _ in e_list]
    
    return Ke_list, fe_list

# end function

def process_element(args):
    e_list, k_list = args
    # Unpack the input arguments and then return the elasticElement result.
    #   This function exists basically just to be a worker.
    return elasticElement(e_list, k_list)

def combine_results(result, element_batch, Kg, fg):
    Ke_list, fe_list = result
    e_list = element_batch[0]
    Kg, fg = assemble(e_list, Ke_list, fe_list, Kg, fg)
    # Puts all the results of each batch into the final stiffness matrix and
    #   force vector. This function also exists basically just to be a worker.
    return ( Kg, fg )

def elasticFEProblem( Ndof, Ne1, Ne2, k_list , elements_per_task = 0 , num_threads = 1 ):
    """
    DESCRIPTION: This function assembles the global stiffness matrix for a sequence 
                 of spring elements, aranged in the following manner:
                
            x-^^-x-^^-x-^^-x...x-^^-x-^^-x-^^-x

    INPUTS:
        -Ndof: Total number of degrees of freedom.
        -k_list: (List of floats, len: Ne ) Element stiffness values. Ne: Number of elements.
        -Ne1: Starting element to be evaluated.
        -Ne2: Final element to be evaluated.
    
    OUTPUTS:
        -Kg: (Float array, Shape: (Ndof,Ndof) ) Global stiffness matrix.
        -fg: (Float array, Shape: (Ndof,) )     Global force vector.

    """
    print("\n\tSetting up problem with {x} number of tasks\n".format( x = num_threads ) )
    
    if not ( elements_per_task > 0 ):
        elements_per_task = Ndof // num_threads
    
    # Create the global matrix.
    Kg = np.zeros((Ndof,Ndof))
    fg = np.zeros((Ndof,))
    
    t_0 = time.time()
    
    element_batches = [ ( list( range( start, min( start + elements_per_task , Ne2 ) ) ) , k_list ) for start in range( Ne1 , Ne2 , elements_per_task ) ]
    # Create sections/batches of the elements rather than handing all the
    #   elements at once. Each element will contain 
    
    Ne = len(k_list) # Number of elements.
    Nu = Ne+1        # Number of nodes.
    
    t_1_2 = time.time()
    
    with Pool() as pool:
        results = pool.map( process_element , element_batches )
    # Apply each batch to a pooled worker of process_element which allows us
    #   to process one batch at a time per worker. The results are stored in 
    #   results to pass into a combination loop later.

    t_1 = time.time()

    for i in range( len( results ) ):
        result = results[i]
        # print("i:\t{x}".format(x=i))
        Ke_list, fe_list = result
        e_list = element_batches[i][0]
        Kg, fg = assemble(e_list, Ke_list, fe_list, Kg, fg)
    # Combine the results of each pooled worker
        
    t_2 = time.time()
    
    print("Result creation time:\t{x}".format(x=(t_1-t_0)))
    print("Result attachment time:\t{x}".format(x=(t_2-t_1)))
    print("Element Batch Definition Time:\t{x}".format(x=(t_1_2-t_0)))

    return Kg, fg , element_batches , results

# end function


if __name__ == '__main__':

    # Total number of degrees of freedom to be generated
    Ndof = 50000
    Ne   = Ndof-1 # number of elements.
    
    
    num_threads = int( sys.argv[2] )
    
    print("Number of Threads:\t{x}".format(x=num_threads))

    print('Number of Degrees of freedom: {0}'.format(Ndof))
    

    # List of elemental stiffness values.
    #
    # This should be created such that each element 
    # may have a different stiffness value.

    k_list  = [1]*Ne
    
    t_start = time.time()
    
    # Create the global system
    Kg, fg , batches , batch_results = elasticFEProblem( Ndof, 0, Ne, k_list , num_threads = num_threads ) 

    t_end   = time.time()
    
    # print(Kg)

    print('Total time to assemble:',t_end-t_start)

# end if __main__