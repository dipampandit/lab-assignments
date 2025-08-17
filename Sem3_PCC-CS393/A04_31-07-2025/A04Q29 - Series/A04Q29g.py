# Series:
# 1 + 1/2 + 1/4 + 1/8 + 1/16 + ... up to n terms

n = int(input("Enter n: "))
total = 0
den = 1
for i in range(n):
    total += 1 / den
    print(f"1/{den}" if den != 1 else "1", end=" + " if i != n - 1 else "")
    den *= 2
print("\nSum =", total)
