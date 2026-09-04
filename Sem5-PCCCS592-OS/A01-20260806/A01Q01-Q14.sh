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

read -p "Enter Principal Amount: " principal
read -p "Enter Time Period: " time
read -p "Enter Rate of Interest: " rate

simple_interest=$(echo "($principal * $time * $rate) / 100" | bc)

compound_amount=$(echo "$principal * (1 + $rate / 100)^$time" | bc -l)
compound_interest=$(echo "$compound_amount - $principal" | bc -l)

echo "Simple Interest: $simple_interest"
echo "Compound Interest: $compound_interest"

# ---

# Calculate the BMI

read -p "Enter Weight in kg: " bmi_weight
read -p "Enter Height in meters: " bmi_height

bmi=$(echo "$bmi_weight / ($bmi_height * $bmi_height)" | bc -l)

echo "BMI: $bmi"

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

read -p "Enter First Number: " num1
read -p "Enter Second Number: " num2
read -p "Enter Third Number: " num3

average=$(echo "($num1 + $num2 + $num3) / 3" | bc -l)

echo "Average: $average"

# ---

# Compare two integer values:
# a. Using conditional operator.

read -p "Enter First Integer: " cond1
read -p "Enter Second Integer: " cond2

cond_result=$((cond1 > cond2 ? cond1 : cond2))

echo "Greater Number: $cond_result"


# b. Using logical operators only.

read -p "Enter First Integer: " logical1
read -p "Enter Second Integer: " logical2

[ $logical1 -gt $logical2 ] && echo "$logical1 is greater than $logical2"

[ $logical1 -lt $logical2 ] && echo "$logical1 is smaller than $logical2"

[ $logical1 -eq $logical2 ] && echo "Both numbers are equal"

# ---

# Calculate the remainder of a division.

read -p "Enter Dividend: " dividend
read -p "Enter Divisor: " divisor

remainder=$((dividend % divisor))

echo "Remainder: $remainder"

# ---

# Find the root of a quadratic equation

read -p "Enter coefficient a: " a
read -p "Enter coefficient b: " b
read -p "Enter coefficient c: " c

d=$(echo "$b * $b - 4 * $a * $c" | bc)

if [ $d -gt 0 ]
then
    root1=$(echo "scale=4; (-$b + sqrt($d)) / (2 * $a)" | bc -l)
    root2=$(echo "scale=4; (-$b - sqrt($d)) / (2 * $a)" | bc -l)

    echo "Root 1: $root1"
    echo "Root 2: $root2"

elif [ $d -eq 0 ]
then
    root=$(echo "scale=4; -$b / (2 * $a)" | bc -l)

    echo "Both roots are equal."
    echo "Root: $root"

else
    echo "Roots are imaginary/complex."
fi
