# Series:
# 1 + 3 + 6 + 10 + 15 + ...

n = int(input("Enter n: "))
total = 0
current = 0
for i in range(1, n + 1):
    current += i
    total += current
    print(current, end=" + " if i != n else "")
print("\nSum =", total)
