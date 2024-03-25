#!/bin/bash
#SBATCH -J sparse_run1
#SBATCH -o stdout_%j.txt
#SBATCH -e errFile_%j.txt
#SBATCH -p compute1
#SBATCH -N 5
#SBATCH -n 40
#SBATCH -c 2
#SBATCH -t 00:30:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user matthew.holland@my.utsa.edu

module load anaconda3
source activate HPC_ME5773

echo Establishing Anaconda environment

workers=(1 2 4 8 16 20 40)

for num_workers in "${workers[@]}"
do
	echo "Running with $num_workers workers"
	python FE_system_group05.py -n $num_workers >& $SLURM_JOB_ID-$num_workers-$method.log
done

conda deactivate

