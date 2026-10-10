#!/bin/bash/

# Q1. To find the GCD and LCM of three positive numbers

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

read -p "Enter three positive integers: " a b c

g1=$(gcd "$a" "$b")
g=$(gcd "$g1" "$c")

l1=$((a / $(gcd "$a" "$b") * b))
lcm=$((l1 / $(gcd "$l1" "$c") * c))

echo "GCD = $g"
echo "LCM = $lcm"

# ---

# Q2. To check whether a given number is an Armstrong number, regardless of the number of digits.

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

    if (( sum == n )); then
        echo "$n is an Armstrong number."
    else
        echo "$n is not an Armstrong number."
    fi
}

read -p "Enter a non-negative integer: " n
armstrong "$n"

# ---

# Q3. To print all prime numbers between two given limits and calculate their sum.

is_prime() {
    n=$1

    (( n < 2 )) && return 1

    for ((i=2; i*i<=n; i++)); do
        (( n % i == 0 )) && return 1
    done

    return 0
}

read -p "Enter lower and upper limits: " low high

sum=0
echo "Prime numbers: "

for ((n=low; n<=high; n++)); do
    if is_prime "$n"; then
        echo -n "$n "
        sum=$((sum + n))
    fi
done

echo
echo "Sum of prime numbers = $sum"

# ---

EOF

# Q4. To find the second largest number among five numbers entered by the user, without using an array.

second_largest() {
    read -p "Enter five numbers: " a b c d e

    max1=$a
    max2=""

    for n in "$b" "$c" "$d" "$e"; do
        if (( n > max1 )); then
            max2=$max1
            max1=$n
        elif [[ -z $max2 ]] || (( n < max1 && n > max2 )); then
            max2=$n
        fi
    done

    if [[ -z $max2 ]]; then
        echo "No second-largest distinct number exists."
    else
        echo "Second-largest number = $max2"
    fi
}

second_largest

# ---

# Q5. To find the second smallest number among five numbers.

second_smallest() {
    read -p "Enter five numbers: " a b c d e

    min1=$a
    min2=""

    for n in "$b" "$c" "$d" "$e"; do
        if (( n < min1 )); then
            min2=$min1
            min1=$n
        elif [[ -z $min2 ]] || (( n > min1 && n < min2 )); then
            min2=$n
        fi
    done

    if [[ -z $min2 ]]; then
        echo "No second-smallest distinct number exists."
    else
        echo "Second-smallest number = $min2"
    fi
}

second_smallest

# ---

# Q6. To check whether a given number is a Strong number.

fact() {
    n=$1; f=1

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
        f=$(fact "$digit")
        sum=$((sum + f))
        temp=$((temp / 10))
    done

    if (( sum == n )); then
        echo "$n is a Strong number."
    else
        echo "$n is not a Strong number."
    fi
}

read -p "Enter a non-negative integer: " n
strong "$n"

# ---

# Q7. To find all perfect numbers between 1 and N.

is_perfect() {
    n=$1
    sum=0

    for ((i=1; i<=n/2; i++)); do
        if (( n % i == 0 )); then
            sum=$((sum + i))
        fi
    done

    (( n > 1 && sum == n ))
}

read -p "Enter N: " N

echo "Perfect numbers between 1 and $N:"
for ((n=1; n<=N; n++)); do
    if is_perfect "$n"; then
        echo -n "$n "
    fi
done

echo

# ---

# Q8. To check whether a given number is a Harshad number.

harshad() {
    n=$1
    temp=$n
    sum=0

    while (( temp > 0 )); do
        sum=$((sum + temp % 10))
        temp=$((temp / 10))
    done

    if (( n > 0 && n % sum == 0 )); then
        echo "$n is a Harshad number."
    else
        echo "$n is not a Harshad number."
    fi
}

read -p "Enter a positive integer: " n
harshad "$n"

# ---

# Q9. To find the largest prime factor of a given number.

largest_prime_factor() {
    n=$1
    largest=0

    while (( n % 2 == 0 )); do
        largest=2
        n=$((n / 2))
    done

    for ((i=3; i*i<=n; i+=2)); do
        while (( n % i == 0 )); do
            largest=$i
            n=$((n / i))
        done
    done

    if (( n > 1 )); then
        largest=$n
    fi

    echo "$largest"
}

read -p "Enter an integer greater than 1: " n
result=$(largest_prime_factor "$n")

echo "Largest prime factor = $result"

# ---

# Q10. To generate the fibonacci series up to N terms and calculate the sum of the series.

fibonacci() {
    n=$1
    a=0
    b=1
    sum=0

    echo "Fibonacci series:"

    for ((i=1; i<=n; i++)); do
        echo -n "$a "
        sum=$((sum + a))

        next=$((a + b))
        a=$b
        b=$next
    done

    echo
    echo "Sum of the series = $sum"
}

read -p "Enter the number of terms: " n
fibonacci "$n"

# ---

# Q11. To convert a decimal number into binary without using bc or any built-in conversion method.

decimal_to_binary() {
    n=$1

    if (( n == 0 )); then
        echo "0"
        return
    fi

    binary=""

    while (( n > 0 )); do
        remainder=$((n % 2))
        binary="${remainder}${binary}"
        n=$((n / 2))
    done

    echo "$binary"
}

read -p "Enter a non-negative decimal integer: " n
echo "Binary = $(decimal_to_binary "$n")"

# ---

# Q12. To Calculate x^y using repeated multiplication without using the ^ operator.

power() {
    x=$1
    y=$2
    result=1

    for ((i=1; i<=y; i++)); do
        result=$((result * x))
    done

    echo "$result"
}

read -p "Enter base x and non-negative exponent y: " x y
echo "$x ^ $y = $(power "$x" "$y")"
