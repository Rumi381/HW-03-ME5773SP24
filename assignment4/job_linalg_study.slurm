#!/bin/bash
#SBATCH -J linalg_study
#SBATCH -o linalg_study_output_%j.txt
#SBATCH -e errFile_%j.txt
#SBATCH -p compute1
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 80
#SBATCH -t 00:05:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user mdjalaluddin.rumi@utsa.edu

# Load Anaconda3 module
module load anaconda3

# Activate the envTeam5 environment
conda activate envTeam5
echo Establishing Anaconda environment


# Array of MKL_NUM_THREADS values
threads=(1 2 4 8 16 20 40)

# Loop through each MKL_NUM_THREADS value
for t in "${threads[@]}"; do
	echo "Running with MKL_NUM_THREADS=$t"
	# Set the MKL_NUM_THREADS environment variable
	export MKL_NUM_THREADS=$t

	# Execute the Python script
	python3 linalg.py

	echo "---------------------------------------------"
done


