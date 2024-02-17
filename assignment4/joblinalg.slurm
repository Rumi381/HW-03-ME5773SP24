#!/bin/bash

# SBATCH -J linalg_study
# SBATCH -o stdout_%j.txt
# SBATCH -e errFile_%j.txt

# SBATCH -p compute1
# SBATCH -N 1
# SBATCH -n 1
# SBATCH -c 80
# SBATCH -t 00:05:00

# SBATCH --mail-type=ALL
# SBATCH --mail-user matthew.holland@my.utsa.edu

module load anaconda
source activate envTeam5
echo Establishing Anaconda environment

export MKL_NUM_THREADS = 1
python linalg.py &
echo Running with Single Thread

export MKL_NUM_THREADS = 2
python linalg.py &
echo Running with Two Threads

export MKL_NUM_THREADS = 4
python linalg.py &
echo Running with Four Threads

export MKL_NUM_THREADS = 8
python linalg.py &
echo Running with Eight Threads

export MKL_NUM_THREADS = 16
python linalg.py &
echo Running with Sixteen Threads

export MKL_NUM_THREADS = 20
python linalg.py &
echo Running with Twenty Threads

export MKL_NUM_THREADS = 40
python linalg.py &
echo Running with Forty Threads

