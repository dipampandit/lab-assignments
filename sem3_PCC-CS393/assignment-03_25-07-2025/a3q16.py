age = int(input("Enter age: "))
weight = float(input("Enter weight (kg): "))
print("Eligible to donate blood" if age >= 18 and weight > 50 else "Not eligible")
