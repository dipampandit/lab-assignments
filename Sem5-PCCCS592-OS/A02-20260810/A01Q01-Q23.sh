#!/bin/bash

# Check Even or Odd

read -p "Enter a number: " evenodd_number

if [ $((evenodd_number % 2)) -eq 0 ]
then
    echo "$evenodd_number is Even"
else
    echo "$evenodd_number is Odd"
fi

# ---

# Find Largest of Two Numbers

read -p "Enter First Number: " largest2_first
read -p "Enter Second Number: " largest2_second

if [ $largest2_first -gt $largest2_second ]
then
    echo "Largest Number: $largest2_first"
else
    echo "Largest Number: $largest2_second"
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

read -p "Enter an alphabet: " vowel_character

if [[ $vowel_character == "a" || $vowel_character == "e" || $vowel_character == "i" || $vowel_character == "o" || $vowel_character == "u" || $vowel_character == "A" || $vowel_character == "E" || $vowel_character == "I" || $vowel_character == "O" || $vowel_character == "U" ]]
then
    echo "$vowel_character is a Vowel"
else
    echo "$vowel_character is a Consonant"
fi

# ---

# Check Voting Eligibility

read -p "Enter Age: " voting_age

if [ $voting_age -ge 18 ]
then
    echo "Person is Eligible to Vote"
else
    echo "Person is Not Eligible to Vote"
fi

# ---

# Check Type of Triangle

read -p "Enter Side 1: " triangle_type_side1
read -p "Enter Side 2: " triangle_type_side2
read -p "Enter Side 3: " triangle_type_side3

if [ $triangle_type_side1 -eq $triangle_type_side2 ] && [ $triangle_type_side2 -eq $triangle_type_side3 ]
then
    echo "Triangle is Equilateral"
elif [ $triangle_type_side1 -eq $triangle_type_side2 ] || [ $triangle_type_side2 -eq $triangle_type_side3 ] || [ $triangle_type_side1 -eq $triangle_type_side3 ]
then
    echo "Triangle is Isosceles"
else
    echo "Triangle is Scalene"
fi

# ---

# Check Type of Triangle

read -p "Enter Side 1: " triangle_type_side1
read -p "Enter Side 2: " triangle_type_side2
read -p "Enter Side 3: " triangle_type_side3

if [ $triangle_type_side1 -eq $triangle_type_side2 ] && [ $triangle_type_side2 -eq $triangle_type_side3 ]
then
    echo "Triangle is Equilateral"
elif [ $triangle_type_side1 -eq $triangle_type_side2 ] || [ $triangle_type_side2 -eq $triangle_type_side3 ] || [ $triangle_type_side1 -eq $triangle_type_side3 ]
then
    echo "Triangle is Isosceles"
else
    echo "Triangle is Scalene"
fi

# ---

# Check Multiple of 3 or 7

read -p "Enter a number: " multiple_number

if [ $((multiple_number % 3)) -eq 0 ] || [ $((multiple_number % 7)) -eq 0 ]
then
    echo "$multiple_number is a multiple of 3 or 7"
else
    echo "$multiple_number is not a multiple of 3 or 7"
fi

# ---

# Check Century Year

read -p "Enter Year: " century_year

if [ $((century_year % 100)) -eq 0 ]
then
    echo "$century_year is a Century Year"
else
    echo "$century_year is not a Century Year"
fi

# ---

# Check Senior Citizen Eligibility

read -p "Enter Age: " senior_age

if [ $senior_age -ge 60 ]
then
    echo "Person is Eligible for Senior Citizen Benefits"
else
    echo "Person is Not Eligible for Senior Citizen Benefits"
fi

# ---

# Check Positive and Divisible by 2

read -p "Enter a number: " positive_even_number

if [ $positive_even_number -gt 0 ] && [ $((positive_even_number % 2)) -eq 0 ]
then
    echo "$positive_even_number is positive and divisible by 2"
else
    echo "$positive_even_number does not satisfy the condition"
fi

# ---

# Check Whether Sum is Even or Odd

read -p "Enter First Number: " sumcheck_first
read -p "Enter Second Number: " sumcheck_second

sumcheck_result=$((sumcheck_first + sumcheck_second))

if [ $((sumcheck_result % 2)) -eq 0 ]
then
    echo "Sum = $sumcheck_result"
    echo "Sum is Even"
else
    echo "Sum = $sumcheck_result"
    echo "Sum is Odd"
fi

# ---

# Check Pass or Fail

read -p "Enter Marks: " student_marks

if [ $student_marks -ge 40 ]
then
    echo "Student has Passed"
else
    echo "Student has Failed"
fi

# ---

# Check Divisibility by 2 and 3

read -p "Enter a number: " divisible23_number

if [ $((divisible23_number % 2)) -eq 0 ] && [ $((divisible23_number % 3)) -eq 0 ]
then
    echo "$divisible23_number is divisible by both 2 and 3"
else
    echo "$divisible23_number is not divisible by both 2 and 3"
fi

# ---

# Check Character

read -p "Enter a character: " character_check

if [[ $character_check =~ ^[a-zA-Z]$ ]]
then
    if [[ $character_check == "a" || $character_check == "e" || $character_check == "i" || $character_check == "o" || $character_check == "u" || $character_check == "A" || $character_check == "E" || $character_check == "I" || $character_check == "O" || $character_check == "U" ]]
    then
        echo "$character_check is a Vowel"
    else
        echo "$character_check is a Consonant"
    fi
else
    echo "$character_check is Not an Alphabet"
fi

# ---

# Check Blood Donation Eligibility

read -p "Enter Age: " blood_age
read -p "Enter Weight in kg: " blood_weight

if [ $blood_age -ge 18 ] && [ $blood_weight -ge 50 ]
then
    echo "Person is Eligible to Donate Blood"
else
    echo "Person is Not Eligible to Donate Blood"
fi

# ---

# Display Grade

read -p "Enter Marks: " grade_marks

if [ $grade_marks -ge 90 ] && [ $grade_marks -le 100 ]
then
    echo "Grade: A"
elif [ $grade_marks -ge 80 ]
then
    echo "Grade: B"
elif [ $grade_marks -ge 70 ]
then
    echo "Grade: C"
elif [ $grade_marks -ge 60 ]
then
    echo "Grade: D"
elif [ $grade_marks -ge 40 ]
then
    echo "Grade: E"
elif [ $grade_marks -ge 0 ]
then
    echo "Grade: F"
else
    echo "Invalid Marks"
fi

# ---

# Check Positive, Negative or Zero

read -p "Enter a number: " sign_number

if [ $sign_number -gt 0 ]
then
    echo "$sign_number is Positive"
elif [ $sign_number -lt 0 ]
then
    echo "$sign_number is Negative"
else
    echo "Number is Zero"
fi

# ---

# Find Largest of Three Numbers

read -p "Enter First Number: " largest3_first
read -p "Enter Second Number: " largest3_second
read -p "Enter Third Number: " largest3_third

if [ $largest3_first -ge $largest3_second ] && [ $largest3_first -ge $largest3_third ]
then
    echo "Largest Number: $largest3_first"
elif [ $largest3_second -ge $largest3_first ] && [ $largest3_second -ge $largest3_third ]
then
    echo "Largest Number: $largest3_second"
else
    echo "Largest Number: $largest3_third"
fi

# ---

# Check Weekday or Weekend

read -p "Enter Day Number (1-7): " day_number

if [ $day_number -ge 1 ] && [ $day_number -le 5 ]
then
    echo "It is a Weekday"
elif [ $day_number -eq 6 ] || [ $day_number -eq 7 ]
then
    echo "It is a Weekend"
else
    echo "Invalid Day Number"
fi

# ---

# Find Smallest of Three Numbers

read -p "Enter First Number: " smallest3_first
read -p "Enter Second Number: " smallest3_second
read -p "Enter Third Number: " smallest3_third

if [ $smallest3_first -le $smallest3_second ] && [ $smallest3_first -le $smallest3_third ]
then
    echo "Smallest Number: $smallest3_first"
elif [ $smallest3_second -le $smallest3_first ] && [ $smallest3_second -le $smallest3_third ]
then
    echo "Smallest Number: $smallest3_second"
else
    echo "Smallest Number: $smallest3_third"
fi

# ---

# Check Temperature

read -p "Enter Temperature: " temperature_value

if [ $temperature_value -le 0 ]
then
    echo "Temperature is Freezing"
elif [ $temperature_value -gt 0 ] && [ $temperature_value -lt 30 ]
then
    echo "Temperature is Moderate"
else
    echo "Temperature is Hot"
fi

# ---

# Compare Two Numbers

read -p "Enter First Number: " compare_first
read -p "Enter Second Number: " compare_second

if [ $compare_first -eq $compare_second ]
then
    echo "Both numbers are Equal"
elif [ $compare_first -gt $compare_second ]
then
    echo "$compare_first is Greater than $compare_second"
else
    echo "$compare_second is Greater than $compare_first"
fi
