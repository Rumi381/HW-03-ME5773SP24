#!/bin/bash
#SBATCH -J sparse_run1
#SBATCH -o stdout_%j.txt
#SBATCH -e errFile_%j.txt
#SBATCH -p compute1
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 40
#SBATCH -t 00:30:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user matthew.holland@my.utsa.edu

module load anaconda3
source activate HPC_ME5773

echo Establishing Anaconda environment

workers=(1 2 4 8 16 20 40)
methods=("base" "lil" "csr")

export MKL_NUM_THREADS=128

for method in "${methods[@]}"
do
  for num_workers in "${workers[@]}"
  do
	  echo "Running with $num_workers workers"
	  python FE_system_sparse_group05_parallel.py -n $num_workers -m $method >& $SLURM_JOB_ID-$num_workers-$method.log
  done
done

conda deactivate

