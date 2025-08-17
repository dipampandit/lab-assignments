# Series:
# 1 + (1+2) + (1+2+3) + ... + (1+2+...+n)

n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    s = 0
    for j in range(1, i + 1):
        s += j
    total += s
    print("(", end="")
    for j in range(1, i + 1):
        print(j, end="+" if j != i else "")
    print(")", end=" + " if i != n else "")
print("\nSum =", total)
