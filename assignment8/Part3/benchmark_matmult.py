# -*- coding: utf-8 -*-
"""
Created on Tue Apr  9 18:17:22 2024

@author: mtthl

This script benchmarks the performance of the cython-created matmult function


"""

import numpy as np
import matmult
import sys
import time

if len(sys.argv) != 2:
    print("Usage: python script_name.py <matrix_size>")
    sys.exit(1)

try:
    N = int(sys.argv[1])
except ValueError:
    print("Matrix size must be an integer.")
    sys.exit(1)

# Create the matrices
A = np.random.rand(N, N)
B = np.random.rand(N, N)

# Repeat multiplication and average timings for accuracy
num_repeats = 10
times_np = []
times_cy = []

for _ in range(num_repeats):
    t_st_np = time.time()
    C_np = np.dot(A, B)
    t_sp_np = time.time()
    times_np.append(t_sp_np - t_st_np)

    t_st_cy = time.time()
    C_cy = matmult.cMatMult(A, B)
    t_sp_cy = time.time()
    times_cy.append(t_sp_cy - t_st_cy)

avg_time_np = sum(times_np) / num_repeats
avg_time_cy = sum(times_cy) / num_repeats

print("\nMatrix Size:", N)
print("NumPy Multiplication Average Time:", avg_time_np)
print("Cython Multiplication Average Time:", avg_time_cy)



