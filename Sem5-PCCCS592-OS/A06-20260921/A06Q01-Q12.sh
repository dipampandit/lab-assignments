#!/bin/bash/

: << 'EOF'

# Q1. To find the GCD and LCM of three positive numbers

gcd() {

}

lcm() {

}

a=2; b=3; c=6
gcd "a" "b" "c"
lcm "a" "b" "c"

# ---

# Q2. To check whether a given number is an Armstrong number, regardless of the number of digits.

check_armstrong() {
    count=0
    temp=$num

    while [ $temp -gt 0 ]
    do
        count=$((count + 1))
        temp=$((temp / 10))
    done

    sum=0
    temp=$num
    while [ $temp -gt 0 ]
    do
        digit=$((temp % 10))
        power=1
        for ((c=0; c<count; c++))
        do
            power=$((power * digit))
        done
        sum=$((sum + power))
        temp=$((temp / 10))
    done

    if [ $sum -eq $num ]; then
        echo "$num is an Armstrong number"
    else
        echo "$num is not an Armstrong number"
    fi
}

read -p "Enter a number to check for Armstrong: " num
check_armstrong num

# ---

# Q3. To print all prime numbers between two given limits and calculate their sum.

is_prime() {
    if [ $num -le 1 ]; then
        exit 0
    fi

    
}

# ---
EOF
# Q12. To calculate x^y using repeated multiplication without using the ^ operator.

repMultiply() {
    answer=1
    for ((i=0; i<y; i++))
    do
        answer=$((answer * x))
    done
    echo "Repeated Multiplication of $x, $y times is $answer"
}

x=2; y=3
repMultiply "x" "y"

# ---

# Q