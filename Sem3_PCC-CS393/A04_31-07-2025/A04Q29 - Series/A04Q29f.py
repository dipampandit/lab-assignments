# Series:
# 1 + 1/2 + 1/3 + 1/4 + ... + 1/n

n = int(input("Enter n: "))
total = 0
for i in range(1, n + 1):
    total += 1 / i
    print(f"1/{i}" if i != 1 else "1", end=" + " if i != n else "")
print("\nSum =", total)
