import time
import numpy as np
import h5py

# Define filenames for each matrix format
csv_files = ['A.csv', 'B.csv', 'C.csv', 'D.csv', 'E.csv']
npy_files = ['A.npy', 'B.npy', 'C.npy', 'D.npy', 'E.npy']
hdf5_file = 'matrix_db.hdf5'

# Function to load and time CSV files
def load_csv(filename):
    start_time = time.time()
    data = np.loadtxt(filename)
    print(f"{filename}: {time.time() - start_time} seconds")

# Function to load and time NPY files
def load_npy(filename):
    start_time = time.time()
    data = np.load(filename)
    print(f"{filename}: {time.time() - start_time} seconds")

# Function to load and time HDF5 datasets
def load_hdf5(filepath, dataset_path):
    with h5py.File(filepath, 'r') as f:
        db = f[dataset_path]
        start_time = time.time()
        data = db[...]
        print(f"{dataset_path}: {time.time() - start_time} seconds")

# Load and time CSV files
for filename in csv_files:
    load_csv(filename)

# Load and time NPY files
for filename in npy_files:
    load_npy(filename)

# Load and time HDF5 datasets
hdf5_datasets = ['integer_group/A', 'integer_group/B', 'integer_group/D', 'float_group/C', 'float_group/E']
for dataset_path in hdf5_datasets:
    load_hdf5(hdf5_file, dataset_path)
