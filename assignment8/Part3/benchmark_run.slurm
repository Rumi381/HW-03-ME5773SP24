#!/bin/bash
#SBATCH --job-name=matrix_mul_test
#SBATCH -N1
#SBATCH -n1
#SBATCH -c80
#SBATCH --time=1:00:00
#SBATCH --partition=compute1
#SBATCH --output=matrix_mul_test_%j.out
#SBATCH --error=matrix_mul_test_%j.err
#SBATCH --mail-user=matthew.holland@my.utsa.edu
#SBATCH --mail-type=ALL

# Load Anaconda module
ml anaconda3

# Activate the Anaconda environment
source activate HPC_ME5773

# Define matrix sizes to test
matrix_sizes="3 10 100 1000"

# Loop over matrix sizes
for size in $matrix_sizes; do
    echo "Running matrix multiplication with size $size"
    
    # Execute Python script with matrix size as argument
    python benchmark_matmult.py $size
    
    echo "----------------------------------------------"
done