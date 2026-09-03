#!/bin/bash

# Area and Perimeter of Rectangle, Triangle, Circle and Rhombus

# Rectangle

read -p "Enter length: " rect_length
read -p "Enter breadth: " rect_breadth

area_rect=$(echo "$rect_length * $rect_breadth" | bc)
perimeter_rect=$(echo "2 * ($rect_length + $rect_breadth)" | bc)

echo "Area of Rectangle: $area_rect"
echo "Perimeter of Rectangle: $perimeter_rect"


# Triangle

read -p "Enter Base: " tri_base
read -p "Enter Height: " tri_height

area_triangle=$(echo "0.5 * $tri_base * $tri_height" | bc)

read -p "Enter Side 1: " tri_side1
read -p "Enter Side 2: " tri_side2
read -p "Enter Side 3: " tri_side3

perimeter_triangle=$(echo "$tri_side1 + $tri_side2 + $tri_side3" | bc)

echo "Area of Triangle: $area_triangle"
echo "Perimeter of Triangle: $perimeter_triangle"


# Circle

read -p "Enter Radius: " circle_radius

circle_pi=3.14159

area_circle=$(echo "$circle_pi * $circle_radius * $circle_radius" | bc)
perimeter_circle=$(echo "2 * $circle_pi * $circle_radius" | bc)

echo "Area of Circle: $area_circle"
echo "Perimeter of Circle: $perimeter_circle"


# Rhombus

read -p "Enter Side Length: " rhombus_side
read -p "Enter Diagonal 1: " rhombus_diag1
read -p "Enter Diagonal 2: " rhombus_diag2

area_rhombus=$(echo "0.5 * $rhombus_diag1 * $rhombus_diag2" | bc)
perimeter_rhombus=$(echo "4 * $rhombus_side" | bc)

echo "Area of Rhombus: $area_rhombus"
echo "Perimeter of Rhombus: $perimeter_rhombus"

# ---

# Calculate the simple & compound interest given principal amount, time of period and rate of interest.

read -p "Enter Principal Amount: " interest_principal
read -p "Enter Time Period: " interest_time
read -p "Enter Rate of Interest: " interest_rate

simple_interest=$(echo "($interest_principal * $interest_time * $interest_rate) / 100" | bc)

compound_amount=$(echo "$interest_principal * (1 + $interest_rate / 100)^$interest_time" | bc -l)
compound_interest=$(echo "$compound_amount - $interest_principal" | bc -l)

echo "Simple Interest: $simple_interest"
echo "Compound Interest: $compound_interest"

# ---

# Calculate the BMI

read -p "Enter Weight in kg: " bmi_weight
read -p "Enter Height in meters: " bmi_height

bmi_value=$(echo "$bmi_weight / ($bmi_height * $bmi_height)" | bc -l)

echo "BMI: $bmi_value"

# ---

# Addition and subtraction of two complex number.

read -p "Enter Real Part of First Number: " complex1_real
read -p "Enter Imaginary Part of First Number: " complex1_imag

read -p "Enter Real Part of Second Number: " complex2_real
read -p "Enter Imaginary Part of Second Number: " complex2_imag

complex_add_real=$(echo "$complex1_real + $complex2_real" | bc)
complex_add_imag=$(echo "$complex1_imag + $complex2_imag" | bc)

complex_sub_real=$(echo "$complex1_real - $complex2_real" | bc)
complex_sub_imag=$(echo "$complex1_imag - $complex2_imag" | bc)

echo "Addition: $complex_add_real + ${complex_add_imag}i"
echo "Subtraction: $complex_sub_real + ${complex_sub_imag}i"

# ---

# Assign an integer number and a floating-point number into different variables and print the same.

integer_value=25
floating_value=15.75

echo "Integer Number: $integer_value"
echo "Floating-Point Number: $floating_value"

# ---

# Add two integer numbers and print the result.

read -p "Enter First Integer: " integer_first
read -p "Enter Second Integer: " integer_second

integer_sum=$((integer_first + integer_second))

echo "Sum: $integer_sum"

# ---

# Compute the average of three numbers.

read -p "Enter First Number: " avg_first
read -p "Enter Second Number: " avg_second
read -p "Enter Third Number: " avg_third

average_result=$(echo "($avg_first + $avg_second + $avg_third) / 3" | bc -l)

echo "Average: $average_result"

# ---

# Compare two integer values:
# a. Using conditional operator.

read -p "Enter First Integer: " conditional_first
read -p "Enter Second Integer: " conditional_second

conditional_result=$((conditional_first > conditional_second ? conditional_first : conditional_second))

echo "Greater Number: $conditional_result"


# b. Using logical operators only.

read -p "Enter First Integer: " logical_first
read -p "Enter Second Integer: " logical_second

[ $logical_first -gt $logical_second ] && echo "$logical_first is greater than $logical_second"

[ $logical_first -lt $logical_second ] && echo "$logical_first is smaller than $logical_second"

[ $logical_first -eq $logical_second ] && echo "Both numbers are equal"

# ---

# Calculate the remainder of a division.

read -p "Enter Dividend: " remainder_dividend
read -p "Enter Divisor: " remainder_divisor

remainder_result=$((remainder_dividend % remainder_divisor))

echo "Remainder: $remainder_result"

# ---

# Find the root of a quadratic equation

read -p "Enter coefficient a: " quadratic_a
read -p "Enter coefficient b: " quadratic_b
read -p "Enter coefficient c: " quadratic_c

quadratic_discriminant=$(echo "$quadratic_b * $quadratic_b - 4 * $quadratic_a * $quadratic_c" | bc)

if [ $quadratic_discriminant -gt 0 ]
then
    quadratic_root1=$(echo "scale=4; (-$quadratic_b + sqrt($quadratic_discriminant)) / (2 * $quadratic_a)" | bc -l)
    quadratic_root2=$(echo "scale=4; (-$quadratic_b - sqrt($quadratic_discriminant)) / (2 * $quadratic_a)" | bc -l)

    echo "Root 1: $quadratic_root1"
    echo "Root 2: $quadratic_root2"

elif [ $quadratic_discriminant -eq 0 ]
then
    quadratic_root=$(echo "scale=4; -$quadratic_b / (2 * $quadratic_a)" | bc -l)

    echo "Both roots are equal."
    echo "Root: $quadratic_root"

else
    echo "Roots are imaginary/complex."
fi
