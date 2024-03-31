# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:02:28 2024

@author: Md Jalal Uddin Rumi
"""

from mpi4py import MPI
import math
import numpy as np
import time
from gauleg import gauleg, f  # Importing gauleg and f functions from gauleg.py file assuming it is in the same directory

def compute_integral(n, x1, x2):
    x = np.zeros(n)
    w = np.zeros(n)
    gauleg(x1, x2, x, w, n)
    integral = sum(w[i] * f(x[i]) for i in range(n))
    return integral

def calculate_percent_error(integration_result):
    # Placeholder for the actual percent error calculation
    exact_value = 2/math.exp(1)
    return abs((integration_result - exact_value) / exact_value) * 100


comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

x1, x2 = -1.0, 1.0  # Define integration limits

if rank == 0:
    results = []
    start_time = time.time()
    for n in range(1, 21):
        comm.send(n, dest=n % (size - 1) + 1, tag=1)
    for n in range(1, 21):
        result = comm.recv(source=MPI.ANY_SOURCE, tag=2)
        results.append(result)
    end_time = time.time()
    
    # Print header
    header = f"{'Quadrature no.':<15} {'Integration Result':<20} {'Percent error':<15} {'Run time (s)':<15}"
    print(header)
    print("-" * len(header))
    
    # Sort the results by quadrature number for consistent ordering
    results.sort(key=lambda x: x[0])
    
    # Print each row in the table format
    for result in results:
        quadrature_no = result[0]
        integration_result = result[1]
        percent_error = calculate_percent_error(result[1])  # You'll need to define this function
        run_time = result[2]
        print(f"{quadrature_no:<15} {integration_result:<20.10f} {percent_error:<15.2f} {run_time:<15.6f}")
        print("-" * len(header))
    print(" " * len(header))
    print("Total runtime: ", end_time - start_time)
else:
    while True:
        n = comm.recv(source=0, tag=1)
        if n is None:  # Break loop if None is received
            break
        start_time = time.time()
        integral = compute_integral(n, x1, x2)
        end_time = time.time()
        comm.send((n, integral, end_time - start_time), dest=0, tag=2)

# Ensure to send a termination signal (None) to all workers when done
if rank == 0:
    for i in range(1, size):
        comm.send(None, dest=i, tag=1)
