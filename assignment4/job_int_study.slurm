#!/bin/bash
#SBATCH -J numerical_int_study
#SBATCH -o numerical_int_study_output%j.txt
#SBATCH -e errFile_%j.txt
#SBATCH -p compute1
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 80
#SBATCH -t 24:00:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user mdjalaluddin.rumi@utsa.edu

module load anaconda3
conda activate envTeam5
echo Establishing Anaconda environment

for nx_threads in 1 2 4 8; do
  for op_threads in 1 2 4 8; do

    export OMP_NUM_THREADS=$op_threads
    export NUMEXP_NUM_THREADS=$nx_threads
    python integral.py &
    echo "Running with $op_threads OMP Threads"
    echo "Running with $nx_threads NumExp Threads" 
    wait
    
  done
done
    
