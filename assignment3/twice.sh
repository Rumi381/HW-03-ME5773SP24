#!/bin/bash

# Check if exactly one argument is provided
if [ $# -ne 1 ]; then
	echo "Usage: $0 <N>"
	exit 1
fi


# Check if the input is a positive integer
if ! [[ $1 =~ ^[0-9]+$ ]]; then
	echo "Error: The input must be a positive integer."
	exit 2
fi

N=$1
waitTime=$((2*N))

# Sleep for 2N seconds
sleep $waitTime

# Output the message
echo "Terminated a task that takes $waitTime seconds."
