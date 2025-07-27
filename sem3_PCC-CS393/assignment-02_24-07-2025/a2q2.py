P = float(input("Enter Principal amount: "))
R = float(input("Enter Rate of interest (%): "))
T = float(input("Enter Time (in years): "))

# Simple Interest
SI = (P * R * T) / 100
print("Simple Interest:", SI)

# Compound Interest
CI = P * ((1 + R/100)**T - 1)
print("Compound Interest:", CI)
