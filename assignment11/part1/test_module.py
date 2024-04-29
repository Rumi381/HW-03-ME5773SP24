import numpy as np
import searchUtilsTeam05 as search

# Create test arrays
sorted_array = np.array([1.0, 2.0, 3.0, 4.0, 5.0], dtype=np.float64)
unsorted_array = np.array([4.0, 1.0, 3.0, 5.0, 2.0], dtype=np.float64)

# Test linearSearch
print("Testing linearSearch...")
index = search.searchutils.linearsearch(sorted_array, len(sorted_array), 3.0)
print(f"Index of 3.0 in sorted_array: {index}")

index = search.searchutils.linearsearch(unsorted_array, len(unsorted_array), 3.0)
print(f"Index of 3.0 in unsorted_array: {index}")

# Test binarySearch (only makes sense for sorted array)
print("Testing binarySearch...")
index = search.searchutils.binarysearch(sorted_array, len(sorted_array), 3.0)
print(f"Index of 3.0 in sorted_array: {index}")
