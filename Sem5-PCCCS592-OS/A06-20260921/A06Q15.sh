#!/bin/bash/

# Q15. Write a Bash shell script using multiple functions to create a menu-driven number-processing program with options for prime check, Armstrong check, Strong number check, perfect number check, palindrome check, factorial, fibonacci series, GCD, LCM, and reverse of a number.


is_prime() {
    n=$1

    (( n < 2 )) && return 1

    for ((i=2; i*i<=n; i++)); do
        (( n % i == 0 )) && return 1
    done

    return 0
}

armstrong() {
    n=$1
    temp=$n
    digits=${#n}
    sum=0

    while (( temp > 0 )); do
        digit=$((temp % 10))
        power=1

        for ((i=1; i<=digits; i++)); do
            power=$((power * digit))
        done

        sum=$((sum + power))
        temp=$((temp / 10))
    done

    (( sum == n ))
}

factorial_digit() {
    n=$1
    f=1

    for ((i=1; i<=n; i++)); do
        f=$((f * i))
    done

    echo "$f"
}

strong() {
    n=$1
    temp=$n
    sum=0

    while (( temp > 0 )); do
        digit=$((temp % 10))
        f=$(factorial_digit "$digit")
        sum=$((sum + f))
        temp=$((temp / 10))
    done

    (( sum == n ))
}

perfect() {
    n=$1
    sum=0

    for ((i=1; i<=n/2; i++)); do
        if (( n % i == 0 )); then
            sum=$((sum + i))
        fi
    done

    (( n > 1 && sum == n ))
}

reverse_num() {
    n=$1
    rev=0

    while (( n > 0 )); do
        rev=$((rev * 10 + n % 10))
        n=$((n / 10))
    done

    echo "$rev"
}

palindrome() {
    n=$1
    rev=$(reverse_num "$n")

    (( n == rev ))
}

factorial() {
    n=$1
    f=1

    for ((i=1; i<=n; i++)); do
        f=$((f * i))
    done

    echo "$f"
}

fibonacci() {
    n=$1
    a=0
    b=1
    sum=0

    for ((i=1; i<=n; i++)); do
        echo -n "$a "
        sum=$((sum + a))
        next=$((a + b))
        a=$b
        b=$next
    done

    echo
    echo "Sum = $sum"
}

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

while true; do
    echo
    echo "1. Prime check"
    echo "2. Armstrong check"
    echo "3. Strong number check"
    echo "4. Perfect number check"
    echo "5. Palindrome check"
    echo "6. Factorial"
    echo "7. Fibonacci series and sum"
    echo "8. GCD"
    echo "9. LCM"
    echo "10. Reverse a number"
    echo "11. Exit"

    read -p "Enter your choice: " choice

    case $choice in
        1)
            read -p "Enter number: " n
            if is_prime "$n"; then
                echo "$n is prime."
            else
                echo "$n is not prime."
            fi
            ;;

        2)
            read -p "Enter number: " n
            if armstrong "$n"; then
                echo "$n is an Armstrong number."
            else
                echo "$n is not an Armstrong number."
            fi
            ;;

        3)
            read -p "Enter number: " n
            if strong "$n"; then
                echo "$n is a Strong number."
            else
                echo "$n is not a Strong number."
            fi
            ;;

        4)
            read -p "Enter number: " n
            if perfect "$n"; then
                echo "$n is a Perfect number."
            else
                echo "$n is not a Perfect number."
            fi
            ;;

        5)
            read -p "Enter number: " n
            if palindrome "$n"; then
                echo "$n is a Palindrome."
            else
                echo "$n is not a Palindrome."
            fi
            ;;

        6)
            read -p "Enter a non-negative integer: " n
            echo "Factorial = $(factorial "$n")"
            ;;

        7)
            read -p "Enter number of terms: " n
            fibonacci "$n"
            ;;

        8)
            read -p "Enter two positive integers: " a b
            echo "GCD = $(gcd "$a" "$b")"
            ;;

        9)
            read -p "Enter two positive integers: " a b
            echo "LCM = $(lcm "$a" "$b")"
            ;;

        10)
            read -p "Enter a non-negative integer: " n
            echo "Reverse = $(reverse_num "$n")"
            ;;

        11)
            echo "Exiting program."
            break
            ;;

        *)
            echo "Invalid choice. Please try again."
            ;;
    esac
done