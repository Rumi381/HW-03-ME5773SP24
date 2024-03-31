# -*- coding: utf-8 -*-
"""
Created on Sun Mar 31 15:03:28 2024

@author: Md Jalal Uddin Rumi
"""

from mpi4py import MPI
import math
import numpy as np
import time
from gauleg import gauleg, f

def compute_integral(n, x1, x2):
    x = np.zeros(n)
    w = np.zeros(n)
    gauleg(x1, x2, x, w, n)
    integral = sum(w[i] * f(x[i]) for i in range(n))
    return integral

def calculate_percent_error(integration_result):
    exact_value = 2 / math.exp(1)
    return abs((integration_result - exact_value) / exact_value) * 100

comm = MPI.COMM_WORLD
rank = comm.Get_rank()
size = comm.Get_size()

x1, x2 = -1.0, 1.0

if rank == 0:
    results = []
    active_workers = 0
    start_time = time.time()
    # Send initial tasks to workers
    for n in range(1, min(size, 21)):
        comm.send(n, dest=n, tag=1)
        active_workers += 1
    next_n = size
    # Collect results and send next task
    while active_workers > 0:
        status = MPI.Status()
        result = comm.recv(source=MPI.ANY_SOURCE, tag=2, status=status)
        results.append(result)
        active_workers -= 1
        if next_n <= 20:
            comm.send(next_n, dest=status.source, tag=1)
            active_workers += 1
            next_n += 1
    end_time = time.time()
    # Print header
    header = f"{'Quadrature no.':<15}{'Integration Result':<20}{'Percent error':<15}{'Run time (s)':<15}"
    print(header)
    print("-" * len(header))
    # Sort and print results
    results.sort(key=lambda x: x[0])
    for result in results:
        n, integral, runtime = result
        percent_error = calculate_percent_error(integral)
        print(f"{n:<15}{integral:<20.10f}{percent_error:<15.2f}{runtime:<15.6f}")
        print("-" * len(header))
    print(" " * len(header))
    print(f"{'Total runtime:':<15}{end_time - start_time:<20.6f}")
    # Send termination signal
    for i in range(1, size):
        comm.send(None, dest=i, tag=1)
else:
    while True:
        n = comm.recv(source=0, tag=1)
        if n is None:
            break
        start_time = time.time()
        integral = compute_integral(n, x1, x2)
        run_time = time.time() - start_time
        comm.send((n, integral, run_time), dest=0, tag=2)

