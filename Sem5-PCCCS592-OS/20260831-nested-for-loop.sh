# nested while loop

: <<'EOF'

echo "Enter four numbers: "
read a b c d

for i in $(seq $a $b)
do
    for j in $(seq $c $d)
    do
        echo -n "$j "
    done
    echo " "
done


# echo "Enter four numbers: "
# read a b c d

# while [ $a -le $b ]
# do
#     i=$a
#     while [ $c -le $d ]
#     do
#         echo -n "$j "
#         c=$((c+1))
#     done
#     echo " "
#     i=$((i+1))
# done

---

# Fibonacci Series upto N terms

f0=0
f1=1
f2=0

read -p "Enter the Nth term: " n

echo -n "$f0 $f1 "
for i in $(seq 2 $n)
do
    f2=$((f1+f0))
    echo -n "$f2 "
    f0=$f1
    f1=$f2
    i=$((i+1))
done

---

# Whether a number is even or not

read -p "Enter a number: " num
if [ $((num % 2)) -eq 0 ]; then
    echo "$num is an even number"
else
    echo "$num is not an even number"
fi

---

# Armstrong number

read -p "Enter a number to check if it is an Armstrong number or not: " num

count=0
n=$num
while [ $n -gt 0 ]
do
    count=$((count+1))
    n=$((n / 10))
done

sum=0
n=$num
while [ $n -gt 0 ]
do
    temp=$((n % 10))
    new=$((temp ** count))
    sum=$((sum+new))
    n=$((n / 10))
done

if [ $sum -eq $num ]; then
    echo "$num is an Armstrong Number"
else
    echo "$num is not an Armstrong Number"
fi

---

# Reverse a number

read -p "Enter a number to reverse: " num

numCpy=$num
revNum=0
while [ $num -gt 0 ]
do
    temp=$((num % 10))
    revNum=$((revNum * 10 + temp))
    num=$((num / 10))
done
echo "Reverse of $numCpy is $revNum"

---

EOF

