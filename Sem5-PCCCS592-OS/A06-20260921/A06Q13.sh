#!/bin/bash/

# Q13. Script using multiple functions to calculate the factorial, sum of digits, reverse, and number of digits of a given integer

factorial() {
    num=$fact_num
    product=1
    for ((i=num; i>0; i--))
    do
        product=$((product * i))
    done

    echo "Factorial of $fact_num: $product"
}

sum_of_digits() {
    num=$sum_num
    sum=0
    while [ $num -gt 0 ]
    do
        digit=$((num % 10))
        sum=$((sum + digit))
        num=$((num / 10))
    done

    echo "Sum of digits: $sum"
}

reverse_number() {
    num=$rev_num
    revNum=0
    while [ $num -gt 0 ]
    do
        digit=$((num % 10))
        revNum=$((revNum * 10 + digit))
        num=$((num / 10))
    done

    echo "Reverse Number: $revNum"
}

number_of_digits() {
    num=$sumdigit_num
    count=0
    while [ $num -gt 0 ]
    do
        count=$((count + 1))
        num=$((num / 10))
    done

    echo "Number of digits: $count"
}

fact_num=5
sum_num=12345
rev_num=54321
sumdigit_num=1234567

factorial "fact_num"
sum_of_digits "sum_num"
reverse_number "rev_num"
number_of_digits "sumdigit_num"
