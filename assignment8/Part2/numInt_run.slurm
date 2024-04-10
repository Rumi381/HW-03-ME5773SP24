#!/bin/bash
#SBATCH --job-name=numInt_numba
#SBATCH -N1
#SBATCH -n1
#SBATCH -c80
#SBATCH --time=1:00:00
#SBATCH --partition=compute1
#SBATCH --output=numInt_numba_%j.out
#SBATCH --error=numInt_numba_%j.err
#SBATCH --mail-user=matthew.holland@my.utsa.edu
#SBATCH --mail-type=ALL

# Load Anaconda module
ml anaconda3

# Activate the Anaconda environment
source activate HPC_ME5773

# Define the values of NUMBA_NUM_THREADS
NUMBA_NUM_THREADS_VALUES="1 2 4 8 16 20"

# Loop over each value and run the script
for THREADS in $NUMBA_NUM_THREADS_VALUES
do
    export NUMBA_NUM_THREADS=$THREADS
    python numInt_numba.py
done
