import numpy as np
import searchUtilsTeam05 as search
import time

# print(dir(search))
# print(dir(search.searchutils))

# Create a large array with 10 million unique elements
x = np.linspace(-10, 10, 10**7, dtype=np.float64)

# The value to search for
# Ensure correct passing of 'n'
n = x.size  # Explicitly using .size to confirm the number of elements in numpy array

# The value to search for
search_value = x[-2]

print("Array size n:", n)  # Debugging: Confirm the size of the array
print("Search value:", search_value)  # Debugging: Output the search value

# Evaluate the CPU time of the Fortran linearSearch
start_time = time.time()
index_fortran_linear = search.searchutils.linearsearch(x, search_value)
end_time = time.time()
time_fortran_linear = end_time - start_time

# Evaluate the CPU time of the Fortran binarySearch
start_time = time.time()
index_fortran_binary = search.searchutils.binarysearch(x, search_value)
end_time = time.time()
time_fortran_binary = end_time - start_time

# Evaluate the CPU time of numpy's searchsorted
start_time = time.time()
index_numpy = np.searchsorted(x, search_value)
end_time = time.time()
time_numpy_searchsorted = end_time - start_time

# Output the results
print("Performance Evaluation:")
print(f"Linear Search (Fortran): Time = {time_fortran_linear:.6f} seconds, Index = {index_fortran_linear}")
print(f"Binary Search (Fortran): Time = {time_fortran_binary:.6f} seconds, Index = {index_fortran_binary}")
print(f"Searchsorted (NumPy): Time = {time_numpy_searchsorted:.6f} seconds, Index = {index_numpy}")

# Save the performance data to a document
with open("performance_evaluation_table.txt", "w") as file:
    file.write("Algorithm,Time (seconds),Index\n")
    file.write(f"Linear Search (Fortran),{time_fortran_linear:.6f},{index_fortran_linear}\n")
    file.write(f"Binary Search (Fortran),{time_fortran_binary:.6f},{index_fortran_binary}\n")
    file.write(f"Searchsorted (NumPy),{time_numpy_searchsorted:.6f},{index_numpy}\n")


# import numpy as np
# import searchUtilsTeam05 as search
# import time

# x = np.linspace(-10, 10, 10**7, dtype=np.float64)
# search_value = x[-2]

# start_time = time.time()
# index_fortran_linear = search.searchutils.linearsearch(x, search_value)
# end_time = time.time()
# print("Linear Search Index:", index_fortran_linear)
# print("Time taken for Linear Search (Fortran):", end_time - start_time, "seconds")
