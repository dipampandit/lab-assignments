#!/bin/bash/

# Q14. Write a Bash shell script using multiple functions to find the GCD, LCM, prime factors, and number of factors of a given positive integer.

gcd() {
    a=$1
    b=$2

    while (( b != 0 )); do
        r=$((a % b))
        a=$b
        b=$r
    done

    echo "$a"
}

lcm() {
    a=$1
    b=$2
    g=$(gcd "$a" "$b")
    echo "$((a / g * b))"
}

prime_factors() {
    n=$1
    echo -n "Prime factors: "

    for ((i=2; i*i<=n; i++)); do
        while (( n % i == 0 )); do
            echo -n "$i "
            n=$((n / i))
        done
    done

    if (( n > 1 )); then
        echo -n "$n"
    fi

    echo
}

count_factors() {
    n=$1
    count=0

    for ((i=1; i*i<=n; i++)); do
        if (( n % i == 0 )); then
            if (( i * i == n )); then
                count=$((count + 1))
            else
                count=$((count + 2))
            fi
        fi
    done

    echo "$count"
}

read -p "Enter two positive integers for GCD and LCM: " a b
read -p "Enter a positive integer for factorization: " n

echo "GCD = $(gcd "$a" "$b")"
echo "LCM = $(lcm "$a" "$b")"
prime_factors "$n"
echo "Number of factors = $(count_factors "$n")"