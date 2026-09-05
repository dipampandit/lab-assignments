#!/bin/bash

# 1. Write a Shell script using case to take a number from 1 to 7 and display the corresponding day of the week.

read -p "Enter a number (1-7): " day

case $day in
    1) echo "Monday" ;;
    2) echo "Tuesday" ;;
    3) echo "Wednesday" ;;
    4) echo "Thursday" ;;
    5) echo "Friday" ;;
    6) echo "Saturday" ;;
    7) echo "Sunday" ;;
    *) echo "Invalid choice" ;;
esac

# ---

# 2. Write a Shell script using case to take a character as input and determine whether it is a vowel, consonant, or invalid input.

read -p "Enter a character: " char

case $char in
    a|e|i|o|u|A|E|I|O|U)
        echo "It is a Vowel"
        ;;
    [a-zA-Z])
        echo "It is a Consonant"
        ;;
    *)
        echo "Invalid Input"
        ;;
esac

# ---

# 3. Write a Shell script using case to create a menu with options for displaying the date, current directory, logged-in user, and calendar.

echo "----- MENU -----"
echo "1. Display Date"
echo "2. Current Directory"
echo "3. Logged-in User"
echo "4. Calendar"

read -p "Enter your choice: " menu

case $menu in
    1) date ;;
    2) pwd ;;
    3) whoami ;;
    4) cal ;;
    *) echo "Invalid choice" ;;
esac

# ---

# 4. Write a Shell script using case to take a filename as input and identify whether it is a .txt, .pdf, .jpg, .png, or .sh file.

read -p "Enter filename: " filename

case $filename in
    *.txt) echo "It is a .txt file" ;;
    *.pdf) echo "It is a .pdf file" ;;
    *.jpg) echo "It is a .jpg file" ;;
    *.png) echo "It is a .png file" ;;
    *.sh) echo "It is a .sh file" ;;
    *) echo "Unknown file type" ;;
esac

# ---

# 5. Write a Shell script using case to take a character and check whether it is a vowel, consonant, digit, or special character.

read -p "Enter a character: " ch

case $ch in
    a|e|i|o|u|A|E|I|O|U)
        echo "$ch is a vowel"
        ;;
    [0-9])
        echo "$ch is a digit"
        ;;
    [a-zA-Z])
        echo "$ch is a consonant"
        ;;
    *)
        echo "$ch is a special character"
        ;;
esac

# ---

# 6. Write a Shell script using case to take a traffic-light colour (red, yellow, green) and display the appropriate instruction.

read -p "Enter Traffic Light Colour: " colour

case $colour in
    red|RED|Red)
        echo "Stop"
        ;;
    yellow|YELLOW|Yellow)
        echo "Get Ready"
        ;;
    green|GREEN|Green)
        echo "Go"
        ;;
    *)
        echo "Invalid Colour"
        ;;
esac

# ---

# 7. Write a Shell script using case to take a month number and display the number of days in that month.

read -p "Enter Month Number (1-12): " month

case $month in
    1|3|5|7|8|10|12)
        echo "31 Days"
        ;;
    4|6|9|11)
        echo "30 Days"
        ;;
    2)
        echo "28 or 29 Days"
        ;;
    *)
        echo "Invalid Month Number"
        ;;
esac

# ---

# 8. Write a Shell script using case to take a grade (A, B, C, D, F) and display the corresponding result.

read -p "Enter Grade (A/B/C/D/F): " grade

case $grade in
    A|a) echo "Excellent" ;;
    B|b) echo "Very Good" ;;
    C|c) echo "Good" ;;
    D|d) echo "Pass" ;;
    F|f) echo "Fail" ;;
    *) echo "Invalid Grade" ;;
esac

# ---

# 9. Write a Shell script using case that takes a number from 1 to 5 and displays the corresponding menu item:
#  1 → Start
#  2 → Stop
#  3 → Restart
#  4 → Status
#  5 → Exit
#  For any other number, display "Invalid choice".

echo "----- MENU -----"
echo "1. Start"
echo "2. Stop"
echo "3. Restart"
echo "4. Status"
echo "5. Exit"

read -p "Enter your choice: " service

case $service in
    1) echo "Start" ;; 
    2) echo "Stop" ;;
    3) echo "Restart" ;;
    4) echo "Status" ;;
    5) echo "Exit" ;;
    *) echo "Invalid choice" ;;
esac
