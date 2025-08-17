# Series:
# 1 - (2+3) + (4+5+6) - (7+8+9+10) + ...

n = int(input("Enter number of terms: "))
total = 0
num = 1
sign = 1
for i in range(1, n + 1):
    group_sum = 0
    print("(" if sign == -1 else "+(", end="") if i > 1 else "("
    for j in range(1, i + 1):
        group_sum += num
        print(num, end="+" if j != i else "")
        num += 1
    print(")", end=" ")
    total += sign * group_sum
    sign *= -1
print("\nSum =", total)
