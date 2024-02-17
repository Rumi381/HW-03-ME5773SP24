#!/bin/bash
#SBATCH -J linalg_study
#SBATCH -o stdout_%j.txt
#SBATCH -e errFile_%j.txt
#SBATCH -p compute1
#SBATCH -N 1
#SBATCH -n 1
#SBATCH -c 80
#SBATCH -t 00:05:00
#SBATCH --mail-type=ALL
#SBATCH --mail-user matthew.holland@my.utsa.edu


module load anaconda3
conda activate envTeam5
echo Establishing Anaconda environment

export MKL_NUM_THREADS=1
python linalg.py &
echo Running with Single Thread
wait

export MKL_NUM_THREADS=2
python linalg.py &
echo Running with Two Threads
wait

export MKL_NUM_THREADS=4
python linalg.py &
echo Running with Four Threads
wait

export MKL_NUM_THREADS=8
python linalg.py &
echo Running with Eight Threads
wait

export MKL_NUM_THREADS=16
python linalg.py &
echo Running with Sixteen Threads
wait

export MKL_NUM_THREADS=20
python linalg.py &
echo Running with Twenty Threads
wait

export MKL_NUM_THREADS=40
python linalg.py &
echo Running with Forty Threads
wait

