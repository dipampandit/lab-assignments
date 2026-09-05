#!/bin/bash

# 1. Print numbers from 1 to 10

num=1
while [ $num -le 10 ]
do
    echo "$num"
    num=$((num + 1))
done

# ---

# 2. Print Numbers from 10 to 1

num2=10
while [ $num2 -ge 1 ]
do
    echo "$num2"
    num2=$((num2 - 1))
done

# ---

# 3. Print Even Numbers from 1 to 50

evennum=2
while [ $evennum -le 50 ]
do
    echo "$evennum"
    evennum=$((evennum + 2))
done

# ---

# 4. Print Odd Numbers from 1 to 50

oddnum=1
while [ $oddnum -le 50 ]
do
    echo "$oddnum"
    oddnum=$((oddnum + 2))
done

# ---

# 5. Sum of Numbers from 1 to N

read -p "Enter N to print sum of numbers: " num

count=1
sum=0

while [ $count -le $num ]
do
    sum=$((sum + count))
    count=$((count + 1))
done

echo "Sum: $sum"

# ---

# 6. Factorial of a Number

read -p "Enter a number to find factorial of: " num

count=1
fact=1

while [ $count -le $num ]
do
    fact=$((fact * count))
    count=$((count + 1))
done

echo "Factorial: $fact"

# ---

# 7. Multiplication Table

read -p "Enter a number to print multiplication table: " num

count=1

while [ $count -le 10 ]
do
    result=$((num * count))
    echo "$num x $count = $result"
    count=$((count + 1))
done

# ---

# 8. Reverse a Number

read -p "Enter a number to reverse: " num

temp=$num
revNum=0

while [ $temp -gt 0 ]
do
    digit=$((temp % 10))
    revNum=$((revNum * 10 + digit))
    temp=$((temp / 10))
done

echo "Reversed Number: $revNum"

# ---

# 9. Count Number of Digits

read -p "Enter a number to count number of digits: " num

temp=$num
result=0

while [ $temp -gt 0 ]
do
    temp=$((temp / 10))
    result=$((result + 1))
done

echo "Number of Digits: $result"

# ---

# 10. Sum of Digits

read -p "Enter a number to find sum of digits: " num

temp=$num
sum=0

while [ $temp -gt 0 ]
do
    digit=$((temp % 10))
    sum=$((sum + digit))
    temp=$((temp / 10))
done

echo "Sum of Digits: $sum"

# ---

# 11. Check Palindrome Number

read -p "Enter a number to check for palindrome: " num

temp=$num
palindrome=0

while [ $temp -gt 0 ]
do
    digit=$((temp % 10))
    palindrome=$((palindrome * 10 + digit))
    temp=$((temp / 10))
done

if [ $num -eq $palindrome ]; then
    echo "$num is a Palindrome"
else
    echo "$num is not a Palindrome"
fi

# ---

# 12. Check Armstrong Number

read -p "Enter a number to check for armstrong: " num

temp=$num
count=0
while [ $temp -gt 0 ]
do
    count=$((count + 1))
    temp=$((temp / 10))
done

temp=$num
sum=0
while [ $temp -gt 0 ]
do
    digit=$((temp % 10))
    power=1
    for ((i=0; i<count; i++))
    do
        power=$((power * digit))
    done
    sum=$((sum + power))
    temp=$((temp / 10))
done

if [ $num -eq $sum ]; then
    echo "$num is an Armstrong Number"
else
    echo "$num is not an Armstrong Number"
fi

# ---

# 13. Find Largest Digit

read -p "Enter a number to find the largest digit: " num

temp=$num
largest=0

while [ $temp -gt 0 ]
do
    digit=$((temp % 10))
    if [ $digit -gt $largest ]; then
        largest=$digit
    fi

    temp=$((temp / 10))
done

echo "Largest Digit: $largest"

# ---

# 14. Find Smallest Digit

read -p "Enter a number to find the smallest digit: " num

temp=$num
smallest=9

while [ $temp -gt 0 ]
do
    digit=$((temp % 10))

    if [ $digit -lt $smallest ]; then
        smallest=$digit
    fi

    temp=$((temp / 10))
done

echo "Smallest Digit: $smallest"

# ---

# 15. Fibonacci Series

read -p "Enter number of terms for fibonacci series: " terms

f0=0
f1=1
count=1

while [ $count -le $terms ]
do
    echo -n "$f0 "

    f2=$((f0 + f1))
    f0=$f1
    f1=$f2

    count=$((count + 1))
done

echo

# ---

# 16. Check Prime Number

read -p "Enter a number to check for prime: " num

divisor=2
flag=0

while [ $divisor -lt $num ]
do
    if [ $((num % divisor)) -eq 0 ]; then
        flag=1
        break
    fi
    divisor=$((divisor + 1))
done

if [ $num -le 1 ]; then
    echo "$num is not a Prime Number"
elif [ $flag -eq 0 ]; then
    echo "$num is a Prime Number"
else
    echo "$num is not a Prime Number"
fi

# ---

# 17. Print Prime Numbers from 1 to N

read -p "Enter N to print prime numbers: " num

prime=2

while [ $prime -le $num ]
do
    divisor=2
    flag=0

    while [ $divisor -lt $prime ]
    do
        if [ $((prime % divisor)) -eq 0 ]; then
            flag=1
            break
        fi
        divisor=$((divisor + 1))
    done

    if [ $flag -eq 0 ]; then
        echo -n "$prime "
    fi

    prime=$((prime + 1))
done

echo

# ---

# 18. Find GCD / HCF of Two Numbers

read -p "Enter First Number: " num1
read -p "Enter Second Number: " num2

while [ $num2 -ne 0 ]
do
    gcd_remainder=$((num1 % num2))
    num1=$num2
    num2=$gcd_remainder
done

echo "GCD/HCF: $num1"

# ---

# 19. Repeated Sum Until User Enters 0

sum=0

while true
do
    read -p "Enter a number (0 to stop): " num

    if [ $num -eq 0 ]; then
        break
    fi
    sum=$((sum + num))
done

echo "Total Sum: $sum"

# ---

# 20. Menu Driven Program Using While

choice=0

while [ $choice -ne 4 ]
do
    echo "----- MENU -----"
    echo "1. Add Two Numbers"
    echo "2. Subtract Two Numbers"
    echo "3. Multiply Two Numbers"
    echo "4. Exit"

    read -p "Enter your choice: " choice

    case $choice in
        1)
            read -p "Enter First Number: " num1
            read -p "Enter Second Number: " num2
            sum=$((num1 + num2))
            echo "Addition: $sum"
            ;;

        2)
            read -p "Enter First Number: " num1
            read -p "Enter Second Number: " num2
            minus=$((num1 - num2))
            echo "Subtraction: $minus"
            ;;

        3)
            read -p "Enter First Number: " num1
            read -p "Enter Second Number: " num2
            mult=$((num1 * num2))
            echo "Multiplication: $mult"
            ;;

        4)
            echo "Exiting Program"
            ;;

        *)
            echo "Invalid Choice"
            ;;
    esac
done
