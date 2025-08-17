# Series:
# 1 + 2^2 + 3^3 + 4^4 + ... + n^n

n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += i ** i
    print(f"{i}^{i}", end=" + " if i != n else "")
print("\nSum =", total)
