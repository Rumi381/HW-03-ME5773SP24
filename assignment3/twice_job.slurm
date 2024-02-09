#!/bin/bash
# ======================================================================

#SBATCH -J paralRun
# #SBATCH -o outFile.%j.txt    # Name of 'stdout' output file.
# #SBATCH -e errFile.%j.txt    # Name of 'stderr' error file.
#SBATCH -p  amdonly         # Partition
#SBATCH -N 1                 # Total number of nodes to be requested.
#SBATCH -n 4                 # Total number of tasks to be requested.
#SBATCH -c 8                 # Number of threads used by each task.
#SBATCH -t 00:05:00          # Maximum estimated run time (dd-hh:mm:ss)
#SBATCH --mail-type=ALL      # Mail events to notify (END, FAIL, ALL).
#SBATCH --mail-user mdjalaluddin.rumi@utsa.edu # Put your utsa-email here.
#

# Print start time stamp
tstart=$(date +%s) 
echo Starting job - `date`


srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK ./twice.sh 5 & 
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK ./twice.sh 2 & 
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK ./twice.sh 7 & 
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK ./twice.sh 6 & 
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK ./twice.sh 1 & 
srun --exclusive -N 1 -n 1 -c $SLURM_CPUS_PER_TASK ./twice.sh 3 & 

echo Waiting for all executions to complete

wait

# Print end time stamp
tend=$(date +%s)

# Calculate the difference in end and start times
tdiff=$((tend-tstart))

# Output calculation time.
echo "Calculations ended"
echo "Total CPU time $tdiff [s]"

# Annotate job details using sacct command
#sacct -j ${SLURM_JOB_ID} --format=JobID,State,Elapsed,Nodelist,NCPUS > run1.txt

