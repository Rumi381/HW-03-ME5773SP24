#!/bin/bash

# Check if exactly one argument is provided
if [ $# -ne 1 ]; then
	echo "Usage: $0 <N>"
	echo "Where N is the upper limit for the factorial calculation."
	exit 1
fi


# Check if the input is a positive integer
if ! [[ $1 =~ ^[0-9]+$ ]]; then
	echo "Error: The input must be a positive integer."
	exit 2
fi

N=$1
fact=1

for (( i=1; i<=N; i++ ))
do
	fact=$((fact*i))
	echo "$i! = $fact"
done
