#!/bin/bash

# Check Even or Odd

read -p "Enter a number: " evenodd

if [ $((evenodd % 2)) -eq 0 ]; then
    echo "$evenodd is Even"
else
    echo "$evenodd is Odd"
fi

# ---

# Find Largest of Two Numbers

read -p "Enter First Number: " num1
read -p "Enter Second Number: " num2

if [ $num1 -gt $num2 ]; then
    echo "Largest Number: $num1"
else
    echo "Largest Number: $num2"
fi

# ---

# Check Leap Year

read -p "Enter Year: " leap_year

if [ $((leap_year % 400)) -eq 0 ] || { [ $((leap_year % 4)) -eq 0 ] && [ $((leap_year % 100)) -ne 0 ]; }
then
    echo "$leap_year is a Leap Year"
else
    echo "$leap_year is not a Leap Year"
fi

# ---

# Check Vowel or Consonant

read -p "Enter an alphabet: " char2

if [[ $char2 == "a" || $char2 == "e" || $char2 == "i" || $char2 == "o" || $char2 == "u" || $char2 == "A" || $char2 == "E" || $char2 == "I" || $char2 == "O" || $char2 == "U" ]]; then
    echo "$char2 is a Vowel"
else
    echo "$char2 is a Consonant"
fi

# ---

# Check Voting Eligibility

read -p "Enter Age: " voting_age

if [ $voting_age -ge 18 ]; then
    echo "Person is Eligible to Vote"
else
    echo "Person is Not Eligible to Vote"
fi

# ---

# Check Type of Triangle

read -p "Enter Side 1: " side1
read -p "Enter Side 2: " side2
read -p "Enter Side 3: " side3

if [ $side1 -eq $side2 ] && [ $side2 -eq $side3 ]; then
    echo "Triangle is Equilateral"
elif [ $side1 -eq $side2 ] || [ $side2 -eq $side3 ] || [ $side1 -eq $side3 ]; then
    echo "Triangle is Isosceles"
else
    echo "Triangle is Scalene"
fi

# ---

# Check Divisibility by 5 and 11

read -p "Enter a number: " num511

if [ $((num511 % 5)) -eq 0 ] && [ $((num511 % 11)) -eq 0 ]; then
    echo "$num511 is divisible by both 5 and 11"
else
    echo "$num511 is not divisible by both 5 and 11"
fi

# ---

# Check Multiple of 3 or 7

read -p "Enter a number: " mult37

if [ $((mult37 % 3)) -eq 0 ] || [ $((mult37 % 7)) -eq 0 ]; then
    echo "$mult37 is a multiple of 3 or 7"
else
    echo "$mult37 is not a multiple of 3 or 7"
fi

# ---

# Check Century Year

read -p "Enter Year: " century_year

if [ $((century_year % 100)) -eq 0 ]; then
    echo "$century_year is a Century Year"
else
    echo "$century_year is not a Century Year"
fi

# ---

# Check Senior Citizen Eligibility

read -p "Enter Age: " senior_age

if [ $senior_age -ge 60 ]; then
    echo "Person is Eligible for Senior Citizen Benefits"
else
    echo "Person is Not Eligible for Senior Citizen Benefits"
fi

# ---

# Check Positive and Divisible by 2

read -p "Enter a number: " pos2

if [ $pos2 -gt 0 ] && [ $((pos2 % 2)) -eq 0 ]; then
    echo "$pos2 is positive and divisible by 2"
else
    echo "$pos2 does not satisfy the condition"
fi

# ---

# Check Whether Sum is Even or Odd

read -p "Enter First Number: " sum_one
read -p "Enter Second Number: " sum_two

sum_result=$((sum_one + sum_two))

if [ $((sum_result % 2)) -eq 0 ]; then
    echo "Sum = $sum_result"
    echo "Sum is Even"
else
    echo "Sum = $sum_result"
    echo "Sum is Odd"
fi

# ---

# Check Pass or Fail

read -p "Enter Marks: " student_marks

if [ $student_marks -ge 40 ]; then
    echo "Student has Passed"
else
    echo "Student has Failed"
fi

# ---

# Check Divisibility by 2 and 3

read -p "Enter a number: " div23

if [ $((div23 % 2)) -eq 0 ] && [ $((div23 % 3)) -eq 0 ]; then
    echo "$div23 is divisible by both 2 and 3"
else
    echo "$div23 is not divisible by both 2 and 3"
fi

# ---

# Check Character

read -p "Enter a character: " char

if [[ $char =~ ^[a-zA-Z]$ ]]
then
    if [[ $char == "a" || $char == "e" || $char == "i" || $char == "o" || $char == "u" || $char == "A" || $char == "E" || $char == "I" || $char == "O" || $char == "U" ]]
    then
        echo "$char is a Vowel"
    else
        echo "$char is a Consonant"
    fi
else
    echo "$char is Not an Alphabet"
fi

# ---

# Check Blood Donation Eligibility

read -p "Enter Age: " blood_age
read -p "Enter Weight in kg: " blood_weight

if [ $blood_age -ge 18 ] && [ $blood_weight -ge 50 ]; then
    echo "Person is Eligible to Donate Blood"
else
    echo "Person is Not Eligible to Donate Blood"
fi

# ---

# Display Grade

read -p "Enter Marks: " grade_marks

if [ $grade_marks -ge 90 ] && [ $grade_marks -le 100 ]; then
    echo "Grade: A"
elif [ $grade_marks -ge 80 ]; then
    echo "Grade: B"
elif [ $grade_marks -ge 70 ]; then
    echo "Grade: C"
elif [ $grade_marks -ge 60 ]; then
    echo "Grade: D"
elif [ $grade_marks -ge 40 ]; then
    echo "Grade: E"
elif [ $grade_marks -ge 0 ]; then
    echo "Grade: F"
else
    echo "Invalid Marks"
fi

# ---

# Check Positive, Negative or Zero

read -p "Enter a number: " sign_number

if [ $sign_number -gt 0 ]; then
    echo "$sign_number is Positive"
elif [ $sign_number -lt 0 ]; then
    echo "$sign_number is Negative"
else
    echo "Number is Zero"
fi

# ---

# Find Largest of Three Numbers

read -p "Enter First Number: " largest_one
read -p "Enter Second Number: " largest_two
read -p "Enter Third Number: " largest_three

if [ $largest_one -ge $largest_two ] && [ $largest_one -ge $largest_three ]; then
    echo "Largest Number: $largest_one"
elif [ $largest_two -ge $largest_one ] && [ $largest_two -ge $largest_three ]; then
    echo "Largest Number: $largest_two"
else
    echo "Largest Number: $largest_three"
fi

# ---

# Check Weekday or Weekend

read -p "Enter Day Number (1-7): " day

if [ $day -ge 1 ] && [ $day -le 5 ]; then
    echo "It is a Weekday"
elif [ $day -eq 6 ] || [ $day -eq 7 ]; then
    echo "It is a Weekend"
else
    echo "Invalid Day Number"
fi

# ---

# Find Smallest of Three Numbers

read -p "Enter First Number: " smallest_one
read -p "Enter Second Number: " smallest_two
read -p "Enter Third Number: " smallest_three

if [ $smallest_one -le $smallest_two ] && [ $smallest_one -le $smallest_three ]; then
    echo "Smallest Number: $smallest_one"
elif [ $smallest_two -le $smallest_one ] && [ $smallest_two -le $smallest_three ]; then
    echo "Smallest Number: $smallest_two"
else
    echo "Smallest Number: $smallest_three"
fi

# ---

# Check Temperature

read -p "Enter Temperature: " temp

if [ $temp -le 0 ]; then
    echo "Temperature is Freezing"
elif [ $temp -gt 0 ] && [ $temp -lt 30 ]; then
    echo "Temperature is Moderate"
else
    echo "Temperature is Hot"
fi

# ---

# Compare Two Numbers

read -p "Enter First Number: " comp_one
read -p "Enter Second Number: " comp_two

if [ $comp_one -eq $comp_two ]; then
    echo "Both numbers are Equal"
elif [ $comp_one -gt $comp_two ]; then
    echo "$comp_one is Greater than $comp_two"
else
    echo "$comp_two is Greater than $comp_one"
fi
