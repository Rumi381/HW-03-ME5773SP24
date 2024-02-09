#!/bin/bash


# Check if exactly one argument is provided
if [ "$#" -ne 1 ]; then
	echo "Usage: $0 N"
	echo "Computes the first N terms of the K-Fibonacci series, where K is fixed"
	exit 1
fi

N=$1  # The number of terms in the K-Fibonacci series
K=2   # Fixed number of previous terms to sum for the next term

# Initialize an array with K ones, assuming the series starts with K ones
fib=( $(for i in $(seq 1 $K); do echo 1; done) )

# Compute the K-Fibonacci series for a fixed K
for ((i=K; i<N; i++)); do
	sum=0
	# Sum the previous K terms
	for ((j=i-K; j<i; j++)); do
		sum=$((sum + fib[j]))
	done
	fib[i]=$sum
done

# Output the first N terms of the K-Fibonacci series for a fixed K
echo "${fib[@]:0:N}"
