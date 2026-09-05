#!/bin/bash/

# Use of while loop to print number in decreasing order upto 2
read -p "Enter a number: " num

while [ $num -ge 2 ]
do
    echo "$num"
    num=$(($num - 1))
done


# Number of even numbers between a lower and upper range
read -p "Enter the lower range: " lower
read -p "Enter the upper range: " upper

while [ $lower -le $upper ]
do
    if [ $(($lower % 2)) -eq 0 ] 
    then
        echo -n "$lower, "
    fi
    lower=$(($lower + 1))
done
echo ""


# Reverse of a number
read -p "Enter a number to reverse: " numtwo
revNum=0

while [ "$numtwo" -gt 0 ]
do
    digit=$(($numtwo % 10))
    revNum=$(($revNum * 10 + $digit))
    numtwo=$(($numtwo / 10))
done
echo "Reversed Number: $revNum"
