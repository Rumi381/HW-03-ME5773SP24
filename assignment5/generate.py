import time
import numpy as np
import h5py

def create_matrix(shape, dtype, fill, min_val=None, max_val=None, order='C'):
    if fill == 'arbitrary':
        return np.random.randint(min_val, max_val+1, size=shape, dtype=dtype)
    elif fill == 'exact':
        return np.full(shape, min_val, dtype=dtype)
    elif fill == 'sequential':
        return np.linspace(min_val, max_val, num=np.prod(shape), dtype=dtype).reshape(shape, order=order)

def save_to_csv(matrix, filename, fmt):
    start_time = time.time()
    np.savetxt(filename, matrix, fmt=fmt)
    print(f"{filename}: {time.time() - start_time} seconds")

def save_to_npy(matrix, filename):
    start_time = time.time()
    np.save(filename, matrix)
    print(f"{filename}: {time.time() - start_time} seconds")

# Create matrices
A = create_matrix((5000, 5000), np.int64, 'arbitrary', 2, 9, 'F')
B = create_matrix((5000, 5000), np.int8, 'arbitrary', 100, 127)
C = create_matrix((5000, 5000), np.float64, 'exact', 0.33333)
D = create_matrix((10, 10), np.int16, 'sequential', 1001, 1100, 'F')
E = create_matrix((2, 2), np.float32, 'sequential', 350.0, 350.3)

# Export to CSV
save_to_csv(A, 'A.csv', '%d')
save_to_csv(B, 'B.csv', '%d')
save_to_csv(C, 'C.csv', '%.18e')
save_to_csv(D, 'D.csv', '%d')
save_to_csv(E, 'E.csv', '%.7e')

# Export to .npy
save_to_npy(A, 'A.npy')
save_to_npy(B, 'B.npy')
save_to_npy(C, 'C.npy')
save_to_npy(D, 'D.npy')
save_to_npy(E, 'E.npy')

# Export to HDF5
with h5py.File('matrix_db.hdf5', 'w') as f:
    int_group = f.create_group('integer_group')
    int_group.attrs['description'] = 'Contains integer matrices'
    
    start_time = time.time()
    int_group.create_dataset('A', data=A, compression='gzip', chunks=(500, 500))
    print(f"matrix_db.hdf5/A: {time.time() - start_time} seconds")
    
    start_time = time.time()
    int_group.create_dataset('B', data=B, compression='gzip', chunks=(1000, 1000))
    print(f"matrix_db.hdf5/B: {time.time() - start_time} seconds")
    
    start_time = time.time()
    int_group.create_dataset('D', data=D, compression='gzip')
    print(f"matrix_db.hdf5/D: {time.time() - start_time} seconds")
    
    float_group = f.create_group('float_group')
    start_time = time.time()
    float_group.create_dataset('C', data=C, compression='gzip')
    print(f"matrix_db.hdf5/C: {time.time() - start_time} seconds")
    
    start_time = time.time()
    float_group.create_dataset('E', data=E)
    print(f"matrix_db.hdf5/E: {time.time() - start_time} seconds")
