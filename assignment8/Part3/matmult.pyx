# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 17:26:39 2024

@author: mtthl

This Cython code provides a matrix mutiplication function that is Numpy-like

"""

# cython: language_level=3
import numpy as np
cimport numpy as np

###############################################################################
#
# Functions
#
###############################################################################

def cMatMult(np.ndarray[np.float64_t, ndim=2] A, np.ndarray[np.float64_t, ndim=2] B):
    """
    This function performs matrix multiplication in Cython.

    Parameters
    ----------
    A : np.ndarray[np.float64_t, ndim=2]
        The first matrix to be multiplied. Has dimensions (n x m)
    B : np.ndarray[np.float64_t, ndim=2]
        The second matrix to be multiplied. Has dimensions (m x p)

    Returns
    -------
    C : np.ndarray[np.float64_t, ndim=2]
        The product matrix. Has dimensions (n x p)
    """
    
    # Find dimensions from input arrays
    cdef int n = A.shape[0]
    cdef int m = A.shape[1]
    cdef int p = B.shape[1]
    
    # Define variables for iteration
    cdef int i, j, k
    cdef float total_sum
    cdef np.ndarray[np.float64_t, ndim=2] C = np.zeros((n, p), dtype=np.float64)
    
    # Perform matrix multiplication
    for i in range(n):
        for j in range(p):
            total_sum = 0
            for k in range(m):
                total_sum += A[i, k] * B[k, j]
            C[i, j] = total_sum
            
    return C
     
        
